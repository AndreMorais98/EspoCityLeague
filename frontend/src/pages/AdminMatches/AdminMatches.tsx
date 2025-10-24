import React, { useState, useEffect, useRef } from 'react';
import { apiService } from '../../services/api';
import { analyzeStagesByDate, Stage, Match } from '../../utils/stageUtils';
import { useUser } from '../../contexts/UserContext';
import './AdminMatches.scss';

interface Team {
  id: number;
  name: string;
  logo_url?: string;
}

interface MatchWithScores extends Match {
  home_team: Team;
  away_team: Team;
}

export default function AdminMatches() {
  const { user } = useUser();
  const [stages, setStages] = useState<Stage[]>([]);
  const [selectedStageId, setSelectedStageId] = useState<number | null>(null);
  const [upcomingStageId, setUpcomingStageId] = useState<number | null>(null);
  const [pastStageIds, setPastStageIds] = useState<Set<number>>(new Set());
  const [matches, setMatches] = useState<MatchWithScores[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [editingMatch, setEditingMatch] = useState<number | null>(null);
  const [homeScore, setHomeScore] = useState<string>('');
  const [awayScore, setAwayScore] = useState<string>('');
  const [submitting, setSubmitting] = useState(false);
  const [updatingStats, setUpdatingStats] = useState(false);
  const stageTabsRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (user?.is_superuser) {
      loadStages();
    }
  }, [user]);

  useEffect(() => {
    if (selectedStageId && user?.is_superuser) {
      loadStageMatches(selectedStageId);
    }
  }, [selectedStageId, user]);

  // Scroll to upcoming stage when stages are loaded
  useEffect(() => {
    if (upcomingStageId && stageTabsRef.current) {
      const upcomingTab = stageTabsRef.current.querySelector(`[data-stage-id="${upcomingStageId}"]`) as HTMLElement;
      if (upcomingTab) {
        upcomingTab.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });
      }
    }
  }, [upcomingStageId, stages]);

  const loadStages = async () => {
    try {
      setLoading(true);
      const stagesData = await apiService.getStages();
      setStages(stagesData);
      
      if (stagesData.length > 0) {
        // Analyze all stages to determine which are upcoming and which are past (lightweight)
        const { upcomingStageId: nextUpcomingStageId, pastStageIds } = analyzeStagesByDate(stagesData);
        
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

  const handleEditClick = (match: MatchWithScores) => {
    setEditingMatch(match.id);
    setHomeScore(match.home_score?.toString() || '');
    setAwayScore(match.away_score?.toString() || '');
  };

  const handleCancelEdit = () => {
    setEditingMatch(null);
    setHomeScore('');
    setAwayScore('');
  };

  const handleSaveScores = async (matchId: number) => {
    if (homeScore === '' || awayScore === '') {
      setError('Please enter both home and away scores');
      return;
    }

    const homeScoreNum = parseInt(homeScore);
    const awayScoreNum = parseInt(awayScore);

    if (isNaN(homeScoreNum) || isNaN(awayScoreNum) || homeScoreNum < 0 || awayScoreNum < 0) {
      setError('Please enter valid non-negative numbers');
      return;
    }

    setSubmitting(true);
    setError(null);

    try {
      await apiService.updateMatchScores(matchId, {
        home_score: homeScoreNum,
        away_score: awayScoreNum
      });

      // Reload matches to get updated data
      if (selectedStageId) {
        await loadStageMatches(selectedStageId);
      }
      
      setEditingMatch(null);
      setHomeScore('');
      setAwayScore('');
    } catch (err: any) {
      console.error('Error updating match scores:', err);
      setError(err.message || 'Failed to update match scores');
    } finally {
      setSubmitting(false);
    }
  };

  const handleUpdateStats = async () => {
    setUpdatingStats(true);
    setError(null);

    try {
      await apiService.updateTieBreakingStats();
      // Show success message or handle success
      console.log('Tie-breaking stats updated successfully');
    } catch (err: any) {
      console.error('Error updating tie-breaking stats:', err);
      setError(err.message || 'Failed to update tie-breaking stats');
    } finally {
      setUpdatingStats(false);
    }
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

  const isMatchFinished = (match: MatchWithScores): boolean => {
    return match.home_score !== null && match.away_score !== null;
  };

  if (loading && stages.length === 0) {
    return (
      <div className="admin-matches-container">
        <div className="loading">Loading...</div>
      </div>
    );
  }

  if (error && stages.length === 0) {
    return (
      <div className="admin-matches-container">
        <div className="error">{error}</div>
      </div>
    );
  }

  // Check if user is admin
  if (!user?.is_superuser) {
    return (
      <div className="admin-matches-container">
        <div className="access-denied">
          <h2>Access Denied</h2>
          <p>This page is only accessible to administrators.</p>
        </div>
      </div>
    );
  } else {
    return (
      <div className="admin-matches-container">
        <div className="admin-matches-header">
          <h1 className="page-title">Match Results Management</h1>
          <p className="page-subtitle">Update match scores and results</p>
          <div className="header-actions">
            <button
              className="update-stats-button"
              onClick={handleUpdateStats}
              disabled={updatingStats}
            >
              {updatingStats ? 'Updating...' : 'Update Tie-Breaking Stats'}
            </button>
          </div>
        </div>

        {stages.length > 0 && (
          <div className="stage-tabs" ref={stageTabsRef}>
            {stages
              .sort((a, b) => {
                // Sort stages chronologically by date
                return new Date(a.date).getTime() - new Date(b.date).getTime();
              })
              .map((stage, index) => (
              <button
                key={stage.id}
                data-stage-id={stage.id}
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

        {error && (
          <div className="error-message">{error}</div>
        )}

        {loading && matches.length === 0 ? (
          <div className="loading">Loading matches...</div>
        ) : matches.length === 0 ? (
          <div className="no-matches">
            <p>No matches available for this stage yet.</p>
          </div>
        ) : (
          <div className="matches-list">
            {matches.map((match) => (
              <div key={match.id} className={`match-card ${isMatchFinished(match) ? 'finished' : 'pending'}`}>
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
                    <span className={`match-status ${isMatchFinished(match) ? 'finished' : 'pending'}`}>
                      {isMatchFinished(match) ? 'Finished' : 'Pending'}
                    </span>
                  </div>
                </div>

                <div className="match-scores">
                  {editingMatch === match.id ? (
                    <div className="score-editor">
                      <div className="score-inputs">
                        <input
                          type="number"
                          min="0"
                          value={homeScore}
                          onChange={(e) => setHomeScore(e.target.value)}
                          className="score-input"
                          placeholder="0"
                          disabled={submitting}
                        />
                        <span className="score-separator">-</span>
                        <input
                          type="number"
                          min="0"
                          value={awayScore}
                          onChange={(e) => setAwayScore(e.target.value)}
                          className="score-input"
                          placeholder="0"
                          disabled={submitting}
                        />
                      </div>
                      <div className="score-actions">
                        <button
                          className="save-button"
                          onClick={() => handleSaveScores(match.id)}
                          disabled={submitting || homeScore === '' || awayScore === ''}
                        >
                          {submitting ? 'Saving...' : 'Save'}
                        </button>
                        <button
                          className="cancel-button"
                          onClick={handleCancelEdit}
                          disabled={submitting}
                        >
                          Cancel
                        </button>
                      </div>
                    </div>
                  ) : (
                    <div className="score-display">
                      {isMatchFinished(match) ? (
                        <div className="final-score">
                          <span className="score">{match.home_score}</span>
                          <span className="score-separator">-</span>
                          <span className="score">{match.away_score}</span>
                        </div>
                      ) : (
                        <div className="pending-score">No score</div>
                      )}
                      <button
                        className="edit-button"
                        onClick={() => handleEditClick(match)}
                        disabled={submitting}
                      >
                        {isMatchFinished(match) ? 'Edit' : 'Add Score'}
                      </button>
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    );
  }
}
