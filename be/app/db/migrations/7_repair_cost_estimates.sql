CREATE TABLE repair_cost_estimates (
    id SERIAL PRIMARY KEY,
    mobile_phone_id INTEGER REFERENCES mobile_phones(id) ON DELETE CASCADE,
    repair_type VARCHAR(255),
    estimated_cost DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
