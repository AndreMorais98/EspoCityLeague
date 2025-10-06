import React from 'react';
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
}

interface MatchCardProps {
  match: Match;
  isLive?: boolean;
}

export default function MatchCard({ match, isLive = false }: MatchCardProps) {
  const kickoffDate = new Date(match.kickoff_at);
  const startTime = kickoffDate.toLocaleTimeString('pt-PT', {
    hour: 'numeric',
    minute: '2-digit',
    hour12: false,
  });

  const hasScore = match.home_score !== null && match.away_score !== null;

  return (
    <div className="match-card">
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
              <span className="start-label">Start in</span>
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

      {!hasScore && (
        <div className="score-input-section">
          <div className="score-inputs">
            <input
              type="number"
              min="0"
              placeholder="0"
              className="score-input"
            />
            <span className="input-separator">-</span>
            <input
              type="number"
              min="0"
              placeholder="0"
              className="score-input"
            />
          </div>
          <button className="predict-button">Predict</button>
        </div>
      )}
    </div>
  );
}

