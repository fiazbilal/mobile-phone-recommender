CREATE TABLE mobile_phone_data (
    id SERIAL PRIMARY KEY,
    brand VARCHAR(255),
    model VARCHAR(255),
    screen_size DECIMAL(3,1),
    storage_size INTEGER,
    price DECIMAL(10,2),
    images TEXT[],
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
