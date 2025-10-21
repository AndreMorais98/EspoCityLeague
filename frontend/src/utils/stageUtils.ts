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
 * Analyzes stages based on their dates to determine which are likely upcoming/past
 * This is a lightweight approach that doesn't require loading all matches
 * Uses a 3-day buffer to account for matches that might extend beyond stage date
 * @param stages Array of stages to analyze
 * @returns Object containing upcoming stage ID and set of past stage IDs
 */
export const analyzeStagesByDate = (stages: Stage[]): StageAnalysis => {
  const now = new Date();
  let upcomingStageId: number | null = null;
  const pastStageIds = new Set<number>();
  
  // Sort stages by date to process them chronologically
  const sortedStages = [...stages].sort((a, b) => 
    new Date(a.date).getTime() - new Date(b.date).getTime()
  );
  
  for (const stage of sortedStages) {
    const stageDate = new Date(stage.date);
    // Add 3 days buffer to account for matches that might extend beyond stage date
    const stageEndDate = new Date(stageDate.getTime() + 3 * 24 * 60 * 60 * 1000);
    
    // If stage end date (with buffer) is in the past, consider it a past stage
    if (stageEndDate < now) {
      pastStageIds.add(stage.id);
    } else {
      // If stage date is in the future and we haven't found an upcoming stage yet
      if (!upcomingStageId) {
        upcomingStageId = stage.id;
      }
    }
  }
  
  // If no upcoming stage found (all stages are in the past), use the last stage
  if (!upcomingStageId && stages.length > 0) {
    upcomingStageId = stages[stages.length - 1].id;
  }
  
  return { upcomingStageId, pastStageIds };
};

/**
 * Analyzes all stages to determine which are upcoming and which are past
 * This loads matches for each stage - use sparingly as it's expensive
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
