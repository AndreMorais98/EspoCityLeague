import React, { useState, useEffect } from 'react';
import { apiService } from '../../services/api';
import { analyzeStagesByDate, Stage, Match } from '../../utils/stageUtils';
import './OthersBets.scss';

interface Team {
  id: number;
  name: string;
  logo_url?: string;
}


interface Bet {
  id: number;
  user: {
    id: number;
    username: string;
  };
  match: Match;
  home_score_prediction: number;
  away_score_prediction: number;
  points_awarded: number;
}


export default function OthersBets() {
  const [stages, setStages] = useState<Stage[]>([]);
  const [selectedStageId, setSelectedStageId] = useState<number | null>(null);
  const [upcomingStageId, setUpcomingStageId] = useState<number | null>(null);
  const [pastStageIds, setPastStageIds] = useState<Set<number>>(new Set());
  const [bets, setBets] = useState<Bet[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadStages();
  }, []);

  useEffect(() => {
    if (selectedStageId) {
      loadStageBets(selectedStageId);
    }
  }, [selectedStageId]);

  const loadStages = async () => {
    setLoading(true);
    try {
      const stagesData = await apiService.getStages();
      setStages(stagesData);
      
      if (stagesData.length > 0) {
        // Analyze all stages in one go (lightweight - no API calls)
        const { upcomingStageId: nextUpcomingStageId, pastStageIds } = analyzeStagesByDate(stagesData);
        
        setUpcomingStageId(nextUpcomingStageId);
        setSelectedStageId(nextUpcomingStageId || stagesData[0].id);
        setPastStageIds(pastStageIds);
      }
    } catch (err) {
      setError('Failed to load stages.');
      console.error('Error loading stages:', err);
    } finally {
      setLoading(false);
    }
  };

  const loadStageBets = async (stageId: number) => {
    setLoading(true);
    try {
      const betsData = await apiService.getStageBets(stageId);
      setBets(betsData);
    } catch (err) {
      setError('Failed to load bets for this stage.');
      console.error('Error loading bets:', err);
    } finally {
      setLoading(false);
    }
  };

  const groupBetsByMatch = () => {
    const grouped = bets.reduce((acc, bet) => {
      const matchId = bet.match.id;
      if (!acc[matchId]) {
        acc[matchId] = {
          match: bet.match,
          bets: [],
        };
      }
      acc[matchId].bets.push(bet);
      return acc;
    }, {} as Record<number, { match: Match; bets: Bet[] }>);

    return Object.values(grouped).sort((a, b) => 
      new Date(a.match.kickoff_at).getTime() - new Date(b.match.kickoff_at).getTime()
    );
  };

  const formatMatchDate = (dateString: string): string => {
    const date = new Date(dateString);
    const options: Intl.DateTimeFormatOptions = {
      day: 'numeric',
      month: 'short',
      hour: '2-digit',
      minute: '2-digit',
      hour12: false,
    };
    return date.toLocaleDateString('en-US', options).replace(',', '');
  };

  const getPointsClass = (points: number) => {
    if (points === 3) return 'green';
    if (points === 1) return 'yellow';
    return 'red';
  };

  const getBetCardClass = (bet: Bet) => {
    const hasScore = bet.match.home_score !== null && bet.match.away_score !== null;
    if (!hasScore) return 'bet-card';
    
    const points = bet.points_awarded;
    if (points === 3) return 'bet-card border-green';
    if (points === 1) return 'bet-card border-yellow';
    return 'bet-card border-red';
  };

  if (loading && stages.length === 0) {
    return (
      <div className="others-bets-container">
        <div className="loading">Loading...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="others-bets-container">
        <div className="error">{error}</div>
      </div>
    );
  }

  return (
    <div className="others-bets-container">
      <div className="others-bets-header">
        <h1 className="page-title">Community Predictions</h1>
        <p className="page-subtitle">See what others have predicted</p>
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

      {loading && bets.length === 0 ? (
        <div className="loading">Loading predictions...</div>
      ) : bets.length === 0 ? (
        <div className="no-bets">
          <p>No predictions available for this stage yet.</p>
        </div>
      ) : (
        <div className="matches-list">
          {groupBetsByMatch().map(({ match, bets: matchBets }) => (
            <div key={match.id} className="match-section">
              <div className="match-header">
                <div className="match-teams">
                  <div className="team">
                    {match.home_team.logo_url && (
                      <img src={match.home_team.logo_url} alt={match.home_team.name} className="team-logo" />
                    )}
                    <span className="team-name">{match.home_team.name}</span>
                  </div>
                  <span className="vs">VS</span>
                  <div className="team">
                    {match.away_team.logo_url && (
                      <img src={match.away_team.logo_url} alt={match.away_team.name} className="team-logo" />
                    )}
                    <span className="team-name">{match.away_team.name}</span>
                  </div>
                </div>
                <div className="match-info">
                  <span className="match-date">{formatMatchDate(match.kickoff_at)}</span>
                  {match.home_score !== null && match.away_score !== null && (
                    <span className="match-score">
                      Final: {match.home_score} - {match.away_score}
                    </span>
                  )}
                </div>
              </div>

              <div className="bets-grid">
                {matchBets.map((bet) => (
                  <div key={bet.id} className={getBetCardClass(bet)}>
                    <div className="bet-user">
                      <div className="user-avatar">
                        {bet.user.username.substring(0, 1).toUpperCase()}
                      </div>
                      <span className="user-name">{bet.user.username}</span>
                    </div>
                    <div className="bet-prediction">
                      <span className="prediction-score">
                        {bet.home_score_prediction} - {bet.away_score_prediction}
                      </span>
                      {match.home_score !== null && match.away_score !== null && (
                        <span className={`bet-points ${getPointsClass(bet.points_awarded)}`}>
                          +{bet.points_awarded}
                        </span>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
