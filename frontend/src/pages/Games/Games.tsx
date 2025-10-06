import React, { useState, useEffect } from 'react';
import { apiService } from '../../services/api';
import MatchCard from '../../components/MatchCard/MatchCard';
import './Games.scss';

interface Stage {
  id: number;
  name: string;
  date: string;
}

interface Team {
  id: number;
  name: string;
  logo_url?: string;
}

interface Match {
  id: number;
  home_team: Team;
  away_team: Team;
  kickoff_at: string;
  home_score?: number | null;
  away_score?: number | null;
  stage: {
    id: number;
    name: string;
  };
}

export default function Games() {
  const [stages, setStages] = useState<Stage[]>([]);
  const [selectedStageId, setSelectedStageId] = useState<number | null>(null);
  const [matches, setMatches] = useState<Match[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadStages();
  }, []);

  useEffect(() => {
    if (selectedStageId) {
      loadStageMatches(selectedStageId);
    }
  }, [selectedStageId]);

  const loadStages = async () => {
    try {
      setLoading(true);
      const stagesData = await apiService.getStages();
      setStages(stagesData);
      if (stagesData.length > 0) {
        setSelectedStageId(stagesData[0].id);
      }
    } catch (err) {
      setError('Failed to load stages');
      console.error('Error loading stages:', err);
    } finally {
      setLoading(false);
    }
  };

  const loadStageMatches = async (stageId: number) => {
    try {
      setLoading(true);
      const matchesData = await apiService.getStageMatches(stageId);
      setMatches(matchesData);
    } catch (err) {
      setError('Failed to load matches');
      console.error('Error loading matches:', err);
    } finally {
      setLoading(false);
    }
  };

  const isMatchLive = (match: Match): boolean => {
    const now = new Date();
    const kickoff = new Date(match.kickoff_at);
    const matchEnd = new Date(kickoff.getTime() + 120 * 60000); // 120 minutes after kickoff
    
    return now >= kickoff && now <= matchEnd && match.home_score === null;
  };

  const groupMatchesByDate = (matches: Match[]) => {
    const grouped = matches.reduce((acc, match) => {
      const date = new Date(match.kickoff_at);
      const dateKey = date.toISOString().split('T')[0]; // YYYY-MM-DD format
      
      if (!acc[dateKey]) {
        acc[dateKey] = [];
      }
      acc[dateKey].push(match);
      
      return acc;
    }, {} as Record<string, Match[]>);

    // Sort dates chronologically
    return Object.entries(grouped).sort(([dateA], [dateB]) => 
      new Date(dateA).getTime() - new Date(dateB).getTime()
    );
  };

  const formatDateHeader = (dateString: string): string => {
    const date = new Date(dateString);
    const options: Intl.DateTimeFormatOptions = {
      day: 'numeric',
      month: 'long',
      weekday: 'long',
    };
    return date.toLocaleDateString('en-US', options);
  };

  if (loading && stages.length === 0) {
    return (
      <div className="games-container">
        <div className="games-loading">Loading...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="games-container">
        <div className="games-error">{error}</div>
      </div>
    );
  }

  return (
    <div className="games-container">
      <div className="games-header">
        <h1 className="games-title">Matches</h1>
        <p className="games-subtitle">Make your predictions for upcoming matches</p>
      </div>

      {stages.length > 0 && (
        <div className="stage-tabs">
          {stages.map((stage) => (
            <button
              key={stage.id}
              className={`stage-tab ${
                selectedStageId === stage.id ? 'active' : ''
              }`}
              onClick={() => setSelectedStageId(stage.id)}
            >
              {stage.name}
            </button>
          ))}
        </div>
      )}

      {loading && matches.length === 0 ? (
        <div className="games-loading">Loading matches...</div>
      ) : matches.length === 0 ? (
        <div className="no-matches">
          <p>No matches available for this stage yet.</p>
        </div>
      ) : (
        <div className="matches-by-date">
          {groupMatchesByDate(matches).map(([dateKey, dateMatches]) => (
            <div key={dateKey} className="date-section">
              <h2 className="date-header">{formatDateHeader(dateKey)}</h2>
              <div className="matches-grid">
                {dateMatches.map((match) => (
                  <MatchCard
                    key={match.id}
                    match={match}
                    isLive={isMatchLive(match)}
                  />
                ))}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
