import React, { useState } from 'react';
import { apiService } from '../../services/api';
import { useUser } from '../../contexts/UserContext';
import './MatchCard.scss';

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
  user_bet?: {
    id: number;
    home_score_prediction: number;
    away_score_prediction: number;
    points_awarded: number;
  } | null;
}

interface MatchCardProps {
  match: Match;
  isLive?: boolean;
  onBetPlaced?: () => void;
}

export default function MatchCard({ match, isLive = false, onBetPlaced }: MatchCardProps) {
  const { user } = useUser();
  const [homePredict, setHomePredict] = useState<string>('');
  const [awayPredict, setAwayPredict] = useState<string>('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const kickoffDate = new Date(match.kickoff_at);
  const now = new Date();
  const hasStarted = now >= kickoffDate;
  const hasScore = match.home_score !== null && match.away_score !== null;
  const hasBet = !!match.user_bet;

  const startTime = kickoffDate.toLocaleTimeString('en-US', {
    hour: 'numeric',
    minute: '2-digit',
    hour12: false,
  });

  const handlePredictSubmit = async () => {
    if (!user || homePredict === '' || awayPredict === '') {
      return;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      const betData = {
        user_id: user.id,
        match_id: match.id,
        home_score_prediction: parseInt(homePredict),
        away_score_prediction: parseInt(awayPredict),
      };

      if (hasBet && match.user_bet) {
        // Update existing bet
        await apiService.updateBet(match.user_bet.id, {
          home_score_prediction: parseInt(homePredict),
          away_score_prediction: parseInt(awayPredict),
        });
      } else {
        // Create new bet
        await apiService.createBet(betData);
      }

      setHomePredict('');
      setAwayPredict('');
      if (onBetPlaced) {
        onBetPlaced();
      }
    } catch (err: any) {
      setError(err.message || 'Failed to place bet');
    } finally {
      setIsSubmitting(false);
    }
  };

  // Get the card border class based on points
  const getCardClass = () => {
    if (!hasScore || !match.user_bet) return 'match-card';
    
    const points = match.user_bet.points_awarded;
    if (points === 3) return 'match-card border-green';
    if (points === 1) return 'match-card border-yellow';
    return 'match-card border-red';
  };

  return (
    <div className={getCardClass()}>
      <div className="match-card-header">
        {isLive && <span className="live-badge">Live</span>}
      </div>

      <div className="match-content">
        <div className="team">
          <div className="team-logo">
            {match.home_team.logo_url ? (
              <img src={match.home_team.logo_url} alt={match.home_team.name} />
            ) : (
              <div className="placeholder-logo">
                {match.home_team.name.substring(0, 3).toUpperCase()}
              </div>
            )}
          </div>
          <span className="team-name">{match.home_team.name}</span>
        </div>

        <div className="match-info">
          {hasScore ? (
            <div className="score-display">
              <span className="score">{match.home_score}</span>
              <span className="score-separator">:</span>
              <span className="score">{match.away_score}</span>
            </div>
          ) : (
            <div className="time-display">
              <span className="start-label">{hasStarted ? 'Started' : 'Start in'}</span>
              <span className="start-time">{startTime}</span>
            </div>
          )}
        </div>

        <div className="team">
          <div className="team-logo">
            {match.away_team.logo_url ? (
              <img src={match.away_team.logo_url} alt={match.away_team.name} />
            ) : (
              <div className="placeholder-logo">
                {match.away_team.name.substring(0, 3).toUpperCase()}
              </div>
            )}
          </div>
          <span className="team-name">{match.away_team.name}</span>
        </div>
      </div>

      {/* Show user's prediction if they have bet */}
      {hasBet && match.user_bet && (
        <div className="bet-info-section">
          <div className="bet-prediction">
            <span className="bet-label">Your Prediction:</span>
            <span className="bet-score">
              {match.user_bet.home_score_prediction} - {match.user_bet.away_score_prediction}
            </span>
            {hasScore && (
              <span className={`points-text ${
                match.user_bet.points_awarded === 3 ? 'green' : 
                match.user_bet.points_awarded === 1 ? 'yellow' : 
                'red'
              }`}>
                +{match.user_bet.points_awarded}
              </span>
            )}
          </div>
        </div>
      )}

      {/* Show prediction input only if match hasn't started and no bet placed yet */}
      {!hasStarted && !hasBet && (
        <div className="score-input-section">
          <div className="score-inputs">
            <input
              type="number"
              min="0"
              placeholder="0"
              value={homePredict}
              onChange={(e) => setHomePredict(e.target.value)}
              className="score-input"
              disabled={isSubmitting}
            />
            <span className="input-separator">-</span>
            <input
              type="number"
              min="0"
              placeholder="0"
              value={awayPredict}
              onChange={(e) => setAwayPredict(e.target.value)}
              className="score-input"
              disabled={isSubmitting}
            />
          </div>
          {error && <div className="error-message">{error}</div>}
          <button
            className="predict-button"
            onClick={handlePredictSubmit}
            disabled={isSubmitting || homePredict === '' || awayPredict === ''}
          >
            {isSubmitting ? 'Submitting...' : 'Predict'}
          </button>
        </div>
      )}
    </div>
  );
}
