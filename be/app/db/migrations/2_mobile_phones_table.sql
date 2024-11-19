CREATE TABLE mobile_phones (
    id SERIAL PRIMARY KEY,
    brand VARCHAR(255),
    model VARCHAR(255),
    screen_size DECIMAL(3,1),
    storage_size INTEGER,
    price DECIMAL(10,2),
    resale_value DECIMAL(10,2),
    repair_cost_estimate DECIMAL(10,2),
    image_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
