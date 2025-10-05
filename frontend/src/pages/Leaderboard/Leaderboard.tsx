import React, { useEffect, useState } from 'react';
import { User } from '../../services/auth';
import { useUser } from '../../contexts/UserContext';
import { apiService } from '../../services/api';
import './Leaderboard.scss';

const getRankIcon = (rank: number) => {
  switch (rank) {
    case 1:
      return '🥇';
    case 2:
      return '🥈';
    case 3:
      return '🥉';
    default:
      return `#${rank}`;
  }
};


export default function Leaderboard() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const { user: currentUser, updateUserScore } = useUser();

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const data = await apiService.getLeaderboard();
        setUsers(data);
      } catch (error) {
        console.error('Failed to fetch leaderboard:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, []);

  const topThree = users.slice(0, 3); 
  const remainingUsers = users.slice(3);

  if (loading) {
    return (
      <div className="leaderboard">
        <div className="leaderboard__loading">Loading leaderboard...</div>
      </div>
    );
  }

  return (
    <div className="leaderboard">
      <div className="leaderboard__header">
        <h1 className="leaderboard__title">Leaderboard</h1>
      </div>


      {/* Top 3 Podium */}
      {topThree.length > 0 && (
        <div className="leaderboard__podium">
          {/* 2nd Place - Left */}
          {topThree[1] && (
            <div
              key={topThree[1].id}
              className="podium__card second"
            >
              <div className="podium__rank">{getRankIcon(2)}</div>
              <div className="podium__avatar">
                <div className="avatar">
                  {topThree[1].username.charAt(0).toUpperCase()}
                </div>
              </div>
              <div className="podium__name">{topThree[1].username}</div>
              <div className="podium__points">
                <span className="points__earned">{topThree[1].score.toLocaleString()} points</span>
              </div>
            </div>
          )}
          
          {/* 1st Place - Center */}
          {topThree[0] && (
            <div
              key={topThree[0].id}
              className="podium__card first"
            >
              <div className="podium__rank">{getRankIcon(1)}</div>
              <div className="podium__avatar">
                <div className="avatar">
                  {topThree[0].username.charAt(0).toUpperCase()}
                </div>
              </div>
              <div className="podium__name">{topThree[0].username}</div>
              <div className="podium__points">
                <span className="points__earned">{topThree[0].score.toLocaleString()} points</span>
              </div>
            </div>
          )}
          
          {/* 3rd Place - Right */}
          {topThree[2] && (
            <div
              key={topThree[2].id}
              className="podium__card third"
            >
              <div className="podium__rank">{getRankIcon(3)}</div>
              <div className="podium__avatar">
                <div className="avatar">
                  {topThree[2].username.charAt(0).toUpperCase()}
                </div>
              </div>
              <div className="podium__name">{topThree[2].username}</div>
              <div className="podium__points">
                <span className="points__earned">{topThree[2].score.toLocaleString()} points</span>
              </div>
            </div>
          )}
        </div>
      )}

      {/* Remaining Users Table */}
      {remainingUsers.length > 0 && (
        <div className="leaderboard__table">
          <div className="table__header">
            <div className="table__col rank">Rank</div>
            <div className="table__col username">User name</div>
            <div className="table__col points">Points</div>
          </div>
          
          {remainingUsers.map((user, index) => {
            const rank = index + 4; // Starting from rank 4
            
            return (
              <div key={user.id} className="table__row">
                <div className="table__col rank">
                  <span className="rank__number">{rank}</span>
                </div>
                <div className="table__col username">
                  <div className="user__info">
                    <div className="user__avatar">
                      {user.username.charAt(0).toUpperCase()}
                    </div>
                    <div className="user__details">
                      <span className="user__name">{user.username}</span>
                      <span className="user__handle">@{user.username.toLowerCase()}</span>
                    </div>
                  </div>
                </div>
                <div className="table__col points">
                  <span className="points__count">{user.score.toLocaleString()}</span>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
