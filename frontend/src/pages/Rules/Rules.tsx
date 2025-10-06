import React from 'react';
import './Rules.scss';

export default function Rules() {
  return (
    <div className="rules">
      <div className="rules__header">
        <h1>Game Rules</h1>
        <p className="rules__subtitle">How to win the Espo City League</p>
      </div>

      <div className="rules__content">
        {/* Scoring System */}
        <section className="rules__section">
          <div className="section__header">
            <div className="section__icon">🏆</div>
            <h2>Scoring System</h2>
          </div>
          
          <div className="scoring-cards">
            <div className="scoring-card perfect">
              <div className="card__header">
                <div className="card__icon">🎯</div>
                <div className="card__points">+3</div>
              </div>
              <div className="card__title">Perfect Prediction</div>
              <div className="card__description">
                Victory + Correct Score
              </div>
              <div className="card__example">
                You bet: 2-1, Result: 2-1 ✅
              </div>
            </div>

            <div className="scoring-card good">
              <div className="card__header">
                <div className="card__icon">✅</div>
                <div className="card__points">+1</div>
              </div>
              <div className="card__title">Correct Winner</div>
              <div className="card__description">
                Victory Only
              </div>
              <div className="card__example">
                You bet: 2-1, Result: 3-0 ✅
              </div>
            </div>

            <div className="scoring-card wrong">
              <div className="card__header">
                <div className="card__icon">❌</div>
                <div className="card__points">0</div>
              </div>
              <div className="card__title">Wrong Prediction</div>
              <div className="card__description">
                Defeat
              </div>
              <div className="card__example">
                You bet: 2-1, Result: 1-2 ❌
              </div>
            </div>
          </div>
        </section>

        {/* Tiebreaker System */}
        <section className="rules__section">
          <div className="section__header">
            <div className="section__icon">⚖️</div>
            <h2>Tiebreaker System</h2>
          </div>
          
          <div className="tiebreaker-info">
            <p className="tiebreaker__intro">
              In case of a tie in total points, the following criteria will be used to determine the winner:
            </p>
            
            <div className="tiebreaker-steps">
              <div className="tiebreaker-step">
                <div className="step__number">1º</div>
                <div className="step__content">
                  <div className="step__title">Most Correct Results</div>
                  <div className="step__description">
                    Player with the highest number of perfect predictions (3 points)
                  </div>
                </div>
              </div>

              <div className="tiebreaker-step">
                <div className="step__number">2º</div>
                <div className="step__content">
                  <div className="step__title">Lone Wolf</div>
                  <div className="step__description">
                    Player with the most victories when others got it wrong
                  </div>
                </div>
              </div>

              <div className="tiebreaker-step">
                <div className="step__number">3º</div>
                <div className="step__content">
                  <div className="step__title">Fewest Defeats</div>
                  <div className="step__description">
                    Player with the least number of wrong predictions
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}