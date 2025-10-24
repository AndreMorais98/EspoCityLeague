import React, { useState, useEffect, useRef } from 'react';
import { apiService } from '../../services/api';
import { useUser } from '../../contexts/UserContext';
import './CreateMatch.scss';

interface Team {
  id: number;
  name: string;
  logo_url?: string;
}

interface Stage {
  id: number;
  name: string;
  date: string;
}

interface CreateMatchData {
  home_team_id: number;
  away_team_id: number;
  stage_id: number;
  kickoff_at: string;
  place?: string;
}

export default function CreateMatch() {
  const { user } = useUser();
  const [teams, setTeams] = useState<Team[]>([]);
  const [stages, setStages] = useState<Stage[]>([]);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);
  const dataLoadedRef = useRef(false);

  // Form state
  const [formData, setFormData] = useState<CreateMatchData>({
    home_team_id: 0,
    away_team_id: 0,
    stage_id: 0,
    kickoff_at: '',
    place: ''
  });

  useEffect(() => {
    if (user?.is_superuser && !dataLoadedRef.current) {
      loadData();
    }
  }, [user?.is_superuser]);

  const loadData = async () => {
    try {
      setLoading(true);
      dataLoadedRef.current = true; // Prevent duplicate calls
      const [teamsData, stagesData] = await Promise.all([
        apiService.getTeams(),
        apiService.getStages()
      ]);
      setTeams(teamsData);
      setStages(stagesData);
    } catch (err) {
      setError('Failed to load teams and stages');
      console.error('Error loading data:', err);
      dataLoadedRef.current = false; // Reset flag on error to allow retry
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'home_team_id' || name === 'away_team_id' || name === 'stage_id' 
        ? parseInt(value) 
        : value
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (formData.home_team_id === formData.away_team_id) {
      setError('Home team and away team cannot be the same');
      return;
    }

    if (!formData.home_team_id || !formData.away_team_id || !formData.stage_id || !formData.kickoff_at) {
      setError('Please fill in all required fields');
      return;
    }

    setSubmitting(true);
    setError(null);
    setSuccess(null);

    try {
      await apiService.createMatch(formData);
      setSuccess('Match created successfully!');
      
      // Reset form
      setFormData({
        home_team_id: 0,
        away_team_id: 0,
        stage_id: 0,
        kickoff_at: '',
        place: ''
      });
    } catch (err: any) {
      console.error('Error creating match:', err);
      setError(err.message || 'Failed to create match');
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return (
      <div className="create-match-container">
        <div className="loading">Loading...</div>
      </div>
    );
  }

  if (!user?.is_superuser) {
    return (
      <div className="create-match-container">
        <div className="access-denied">
          <h2>Access Denied</h2>
          <p>This page is only accessible to administrators.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="create-match-container">
      <div className="create-match-header">
        <h1 className="page-title">Create New Match</h1>
        <p className="page-subtitle">Add a new match to the league</p>
      </div>

      <form className="create-match-form" onSubmit={handleSubmit}>
        <div className="form-section">
          <h3 className="section-title">Match Details</h3>
          
          <div className="form-row">
            <div className="form-group">
              <label htmlFor="home_team_id" className="form-label">
                Home Team *
              </label>
              <select
                id="home_team_id"
                name="home_team_id"
                value={formData.home_team_id}
                onChange={handleInputChange}
                className="form-select"
                required
              >
                <option value={0}>Select Home Team</option>
                {teams.map(team => (
                  <option key={team.id} value={team.id}>
                    {team.name}
                  </option>
                ))}
              </select>
            </div>

            <div className="vs-separator">VS</div>

            <div className="form-group">
              <label htmlFor="away_team_id" className="form-label">
                Away Team *
              </label>
              <select
                id="away_team_id"
                name="away_team_id"
                value={formData.away_team_id}
                onChange={handleInputChange}
                className="form-select"
                required
              >
                <option value={0}>Select Away Team</option>
                {teams.map(team => (
                  <option key={team.id} value={team.id}>
                    {team.name}
                  </option>
                ))}
              </select>
            </div>
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="stage_id" className="form-label">
                Stage *
              </label>
              <select
                id="stage_id"
                name="stage_id"
                value={formData.stage_id}
                onChange={handleInputChange}
                className="form-select"
                required
              >
                <option value={0}>Select Stage</option>
                {stages.map(stage => (
                  <option key={stage.id} value={stage.id}>
                    {stage.name}
                  </option>
                ))}
              </select>
            </div>

            <div className="form-group">
              <label htmlFor="kickoff_at" className="form-label">
                Kickoff Date & Time *
              </label>
              <input
                type="datetime-local"
                id="kickoff_at"
                name="kickoff_at"
                value={formData.kickoff_at}
                onChange={handleInputChange}
                className="form-input"
                required
              />
            </div>
          </div>

          <div className="form-group">
            <label htmlFor="place" className="form-label">
              Venue (Optional)
            </label>
            <input
              type="text"
              id="place"
              name="place"
              value={formData.place}
              onChange={handleInputChange}
              className="form-input"
              placeholder="e.g., Stadium Name, City"
            />
          </div>
        </div>

        {error && (
          <div className="error-message">{error}</div>
        )}

        {success && (
          <div className="success-message">{success}</div>
        )}

        <div className="form-actions">
          <button
            type="submit"
            className="submit-button"
            disabled={submitting}
          >
            {submitting ? 'Creating...' : 'Create Match'}
          </button>
        </div>
      </form>
    </div>
  );
}
