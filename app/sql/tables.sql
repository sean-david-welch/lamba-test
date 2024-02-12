CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2),
    created TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_information (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products(id),
    sku VARCHAR(255) NOT NULL,
    inventory_levels INTEGER NOT NULL
);

