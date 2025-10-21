import { getAuthToken, User } from './auth';

const API_BASE_URL = process.env.BACKEND_URL || 'https://espocity-league.mooo.com/api';
/* const API_BASE_URL = process.env.BACKEND_URL || 'http://localhost:8000/api';*/

interface ApiResponse<T> {
  data: T;
  error?: string;
}

class ApiService {
  private cache = new Map<string, { data: any; timestamp: number }>();
  private readonly CACHE_DURATION = 60*60*1000; // 5 seconds

  private async makeRequest<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    const token = getAuthToken();
    const url = `${API_BASE_URL}${endpoint}`;

    const defaultHeaders: HeadersInit = {
      'Content-Type': 'application/json',
    };

    if (token) {
      defaultHeaders['Authorization'] = `Bearer ${token}`;
    }

    const response = await fetch(url, {
      ...options,
      headers: {
        ...defaultHeaders,
        ...options.headers,
      },
    });

    if (!response.ok) {
      throw new Error(`API request failed: ${response.status} ${response.statusText}`);
    }

    return response.json();
  }

  async getCurrentUser(): Promise<User> {
    return this.makeRequest<User>('/auth/me');
  }

  async updateCurrentUser(updateData: { username?: string; phone?: string; password?: string }): Promise<User> {
    return this.makeRequest<User>('/auth/me', {
      method: 'PUT',
      body: JSON.stringify(updateData),
    });
  }

  // Leaderboard endpoints
  async getLeaderboard(): Promise<User[]> {
    const cacheKey = 'leaderboard';
    const cached = this.cache.get(cacheKey);
    
    if (cached && Date.now() - cached.timestamp < this.CACHE_DURATION) {
      return cached.data;
    }
    
    const data = await this.makeRequest<User[]>('/leaderboard');
    this.cache.set(cacheKey, { data, timestamp: Date.now() });
    return data;
  }

  // Bets endpoints
  async getBets(): Promise<any[]> {
    return this.makeRequest<any[]>('/bets');
  }

  async getBetById(id: number): Promise<any> {
    return this.makeRequest<any>(`/bets/${id}`);
  }

  async getUserBets(userId: number): Promise<any[]> {
    return this.makeRequest<any[]>(`/bets/user/${userId}`);
  }

  async createBet(betData: { user_id: number; match_id: number; home_score_prediction: number; away_score_prediction: number }): Promise<any> {
    return this.makeRequest<any>('/bets', {
      method: 'POST',
      body: JSON.stringify(betData),
    });
  }

  async updateBet(betId: number, betData: { home_score_prediction: number; away_score_prediction: number }): Promise<any> {
    return this.makeRequest<any>(`/bets/${betId}`, {
      method: 'PATCH',
      body: JSON.stringify(betData),
    });
  }

  // Teams endpoints
  async getTeams(): Promise<any[]> {
    return this.makeRequest<any[]>('/teams');
  }

  async getTeamById(id: number): Promise<any> {
    return this.makeRequest<any>(`/teams/${id}`);
  }

  // Matches endpoints
  async getMatches(): Promise<any[]> {
    return this.makeRequest<any[]>('/matches');
  }

  async getMatchesByDate(date: string): Promise<any[]> {
    return this.makeRequest<any[]>(`/matches?date=${date}`);
  }

  async getMatchById(id: number): Promise<any> {
    return this.makeRequest<any>(`/matches/${id}`);
  }

  // Stages endpoints
  async getStages(): Promise<any[]> {
    const cacheKey = 'stages';
    const cached = this.cache.get(cacheKey);
    
    if (cached && Date.now() - cached.timestamp < this.CACHE_DURATION) {
      return cached.data;
    }
    
    const data = await this.makeRequest<any[]>('/stages');
    this.cache.set(cacheKey, { data, timestamp: Date.now() });
    return data;
  }

  async getStageById(id: number): Promise<any> {
    return this.makeRequest<any>(`/stages/${id}`);
  }

  async getStageMatches(stageId: number): Promise<any[]> {
    return this.makeRequest<any[]>(`/stages/${stageId}/matches`);
  }

  async getStageBets(stageId: number): Promise<any[]> {
    return this.makeRequest<any[]>(`/stages/${stageId}/bets`);
  }

  // Admin endpoints
  async updateMatchScores(matchId: number, scores: { home_score: number; away_score: number }): Promise<any> {
    return this.makeRequest<any>(`/matches/${matchId}/scores`, {
      method: 'PATCH',
      body: JSON.stringify(scores),
    });
  }
}

export const apiService = new ApiService();
