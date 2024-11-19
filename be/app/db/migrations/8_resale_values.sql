CREATE TABLE resale_values (
    id SERIAL PRIMARY KEY,
    mobile_phone_id INTEGER REFERENCES mobile_phones(id) ON DELETE CASCADE,
    predicted_resale_value DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
