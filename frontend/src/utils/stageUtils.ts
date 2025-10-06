import { apiService } from '../services/api';

export interface Stage {
  id: number;
  name: string;
  date: string;
}

export interface Match {
  id: number;
  home_team: {
    id: number;
    name: string;
    logo_url?: string;
  };
  away_team: {
    id: number;
    name: string;
    logo_url?: string;
  };
  kickoff_at: string;
  home_score?: number | null;
  away_score?: number | null;
  stage: {
    id: number;
    name: string;
  };
}

export interface StageAnalysis {
  upcomingStageId: number | null;
  pastStageIds: Set<number>;
}

/**
 * Analyzes all stages to determine which are upcoming and which are past
 * @param stages Array of stages to analyze
 * @returns Object containing upcoming stage ID and set of past stage IDs
 */
export const analyzeStages = async (stages: Stage[]): Promise<StageAnalysis> => {
  const now = new Date();
  let upcomingStageId: number | null = null;
  const pastStageIds = new Set<number>();
  
  for (const stage of stages) {
    try {
      const matchesData = await apiService.getStageMatches(stage.id);
      
      if (matchesData.length === 0) {
        continue; // Skip stages with no matches
      }
      
      // Check if all matches are finished (past stage)
      const allMatchesFinished = matchesData.every((match: Match) => {
        const kickoffDate = new Date(match.kickoff_at);
        return kickoffDate < now && match.home_score !== null && match.away_score !== null;
      });
      
      if (allMatchesFinished) {
        pastStageIds.add(stage.id);
      } else {
        // Check if this stage has any upcoming matches
        const hasUpcomingMatches = matchesData.some((match: Match) => {
          const kickoffDate = new Date(match.kickoff_at);
          return kickoffDate > now;
        });
        
        // Set as upcoming stage if it's the first one with upcoming matches
        if (hasUpcomingMatches && !upcomingStageId) {
          upcomingStageId = stage.id;
        }
      }
    } catch (err) {
      console.warn(`Failed to load matches for stage ${stage.id}:`, err);
    }
  }
  
  // If no stage has upcoming matches, use the last stage
  if (!upcomingStageId && stages.length > 0) {
    upcomingStageId = stages[stages.length - 1].id;
  }
  
  return { upcomingStageId, pastStageIds };
};

/**
 * Determines if a match is currently live
 * @param match The match to check
 * @returns true if the match is currently live
 */
export const isMatchLive = (match: Match): boolean => {
  const now = new Date();
  const kickoff = new Date(match.kickoff_at);
  const matchEnd = new Date(kickoff.getTime() + 120 * 60000); // 120 minutes after kickoff
  
  return now >= kickoff && now <= matchEnd && match.home_score === null;
};
