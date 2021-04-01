DROP TABLE IF EXISTS recipes, categories, cooks, users, email, ingredients, authorship, incorporation, pantry;

CREATE TYPE DIFFICULTY AS ENUM ('very_easy', 'easy', 'medium', 'hard', 'very_hard');

CREATE TABLE recipes(
    recipe_id SERIAL PRIMARY KEY,
    recipe_name VARCHAR(100) NOT NULL,
    rating FLOAT(2) DEFAULT 0.00,
    description VARCHAR(500) NOT NULL,
    cook_time INTEGER NOT NULL,
    steps VARCHAR(2000) NOT NULL, 
    difficulty DIFFICULTY DEFAULT 'medium' 
);

CREATE TABLE users(
    username VARCHAR (100) PRIMARY KEY,
    password VARCHAR (100) NOT NULL,   
    creation_date TIMESTAMP NOT NULL,
    last_access_date TIMESTAMP NOT NULL
);

CREATE TABLE categories(
    recipe_id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL, 
    FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id)
);

CREATE TABLE cooks(
    username VARCHAR(100), 
    recipe_id SERIAL,
    creation_date TIMESTAMP,
    PRIMARY KEY (username, recipe_id, creation_date),
    rating SMALLINT DEFAULT 0,
    servings SMALLINT DEFAULT 0, --Defaulted to 0 servings
    FOREIGN KEY (username) REFERENCES users (username),
    FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id)
);

CREATE TABLE email(
    email VARCHAR(100),
    username VARCHAR(100),
    PRIMARY KEY (email, username),
    FOREIGN KEY (username) REFERENCES users (username)
);

CREATE TABLE ingredients(
    ingredient_id SERIAL PRIMARY KEY,
    ingredient_name varchar(255) NOT NULL, --name of each ingredient set to a 255 character max
    aisle varchar(40) --name of a type (dairy, meat, etc.) set to a 40 character limit
);

CREATE TABLE authorship(
    username VARCHAR(100),
    recipe_id SERIAL,
    PRIMARY KEY (username, recipe_id),
    creation_date TIMESTAMP NOT NULL,
    FOREIGN KEY (username) REFERENCES users (username),
    FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id)
);

CREATE TABLE incorporation(
    recipe_id SERIAL,
    ingredient_id SERIAL,
    PRIMARY KEY (recipe_id, ingredient_id),
    quantity SMALLINT DEFAULT 0,
    FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients (ingredient_id)
);

CREATE TABLE pantry(
    purchase_date TIMESTAMP,
    username VARCHAR(100),
    ingredient_id SERIAL,
    PRIMARY KEY (purchase_date, username, ingredient_id),
    FOREIGN KEY (username) REFERENCES users (username),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients (ingredient_id),
    expiration_date TIMESTAMP,
    current_quantity FLOAT(4), --All items are to be measured in Stones (14lb)
    quantity_bought FLOAT(4) NOT NULL
);
