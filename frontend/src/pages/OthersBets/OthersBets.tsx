import React, { useEffect, useState } from 'react';

interface Bet {
  id: number;
  user_id: number;
  match_id: number;
  predicted_home: number;
  predicted_away: number;
  points_awarded: number;
}

export default function OthersBets() {
  const [bets, setBets] = useState<Bet[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string|undefined>();

  useEffect(() => {
    const load = async () => {
      try {
        const base = (import.meta as any).env?.VITE_API_BASE_URL || 'http://localhost:8000';
        const res = await fetch(`${base}/bets`);
        if (!res.ok) throw new Error(`Failed: ${res.status}`);
        const data = await res.json();
        setBets(data);
      } catch (e: any) {
        setError(e.message);
      } finally {
        setLoading(false);
      }
    };
    load();
  }, []);

  if (loading) return <div>Loading bets...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h2>Others' Bets</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>User</th>
            <th>Match</th>
            <th>Predicted</th>
            <th>Points</th>
          </tr>
        </thead>
        <tbody>
          {bets.map(b => (
            <tr key={b.id}>
              <td>{b.id}</td>
              <td>{b.user_id}</td>
              <td>{b.match_id}</td>
              <td>{b.predicted_home} - {b.predicted_away}</td>
              <td>{b.points_awarded}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
