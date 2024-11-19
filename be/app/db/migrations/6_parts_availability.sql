CREATE TABLE parts_availability (
    id SERIAL PRIMARY KEY,
    mobile_phone_id INTEGER REFERENCES mobile_phones(id) ON DELETE CASCADE,
    part_name VARCHAR(255),
    available BOOLEAN,
    price DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
