CREATE TABLE mobile_phone_recommendations (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    mobile_phone_id INTEGER REFERENCES mobile_phones(id) ON DELETE CASCADE,
    recommendation_score DECIMAL(5,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
