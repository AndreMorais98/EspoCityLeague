import React, { useState, useEffect } from 'react';
import { apiService } from '../../services/api';
import { analyzeStages, isMatchLive, Stage, Match } from '../../utils/stageUtils';
import MatchCard from '../../components/MatchCard/MatchCard';
import './Games.scss';

interface Team {
  id: number;
  name: string;
  logo_url?: string;
}

interface MatchWithBet extends Match {
  user_bet?: {
    id: number;
    home_score_prediction: number;
    away_score_prediction: number;
    points_awarded: number;
  } | null;
}

export default function Games() {
  const [stages, setStages] = useState<Stage[]>([]);
  const [selectedStageId, setSelectedStageId] = useState<number | null>(null);
  const [upcomingStageId, setUpcomingStageId] = useState<number | null>(null);
  const [pastStageIds, setPastStageIds] = useState<Set<number>>(new Set());
  const [matches, setMatches] = useState<MatchWithBet[]>([]);
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
        // Analyze all stages in one go
        const { upcomingStageId: nextUpcomingStageId, pastStageIds } = await analyzeStages(stagesData);
        
        setUpcomingStageId(nextUpcomingStageId);
        setSelectedStageId(nextUpcomingStageId || stagesData[0].id);
        setPastStageIds(pastStageIds);
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


  const groupMatchesByDate = (matches: MatchWithBet[]) => {
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

  const calculateTotalPoints = (): number => {
    return matches.reduce((total, match) => {
      if (match.user_bet && match.home_score !== null && match.away_score !== null) {
        return total + match.user_bet.points_awarded;
      }
      return total;
    }, 0);
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
        <div className="header-content">
          <div>
            <h1 className="games-title">Matches</h1>
            <p className="games-subtitle">Make your predictions for upcoming matches</p>
          </div>
          {matches.length > 0 && (
            <div className="total-points">
              <span className="points-label">Stage Total:</span>
              <span className="points-value">{calculateTotalPoints()} pts</span>
            </div>
          )}
        </div>
      </div>

      {stages.length > 0 && (
        <div className="stage-tabs">
          {stages.map((stage) => (
            <button
              key={stage.id}
              className={`stage-tab ${
                selectedStageId === stage.id ? 'active' : ''
              } ${upcomingStageId === stage.id ? 'upcoming' : ''} ${
                pastStageIds.has(stage.id) ? 'past' : ''
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
                    onBetPlaced={() => selectedStageId && loadStageMatches(selectedStageId)}
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
