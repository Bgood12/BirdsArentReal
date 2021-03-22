DROP TABLE IF EXISTS recipes, categories, cooks, users, email, ingredients, authorship, incorporation, pantry;

CREATE TYPE DIFFICULTY AS ENUM ("very_easy", "easy", "medium", "hard", "very_hard")

CREATE TABLE recipes(
    recipe_id SERIAL PRIMARY KEY,
    recipe_name VARCHAR(40) NOT NULL,
	rating FLOAT(1,2) DEFAULT 0.00,
	description VARCHAR(500) NOT NULL,
	cook_time TIME NOT NULL,
	steps VARCHAR(2000) NOT NULL, 
	difficulty DIFFICULTY NOT NULL 
);

CREATE TABLE categories(
    recipe_id PRIMARY KEY,
    name VARCHAR(40) NOT NULL, 
    FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id)
);

CREATE TABLE cooks(
    username PRIMARY KEY, 
    recipe_id PRIMARY KEY,
    creation_date TIMESTAMP PRIMARY KEY,
    rating SMALLINT DEFAULT 0,
    servings SMALLINT DEFAULT 0, --Defaulted to 0 servings
    FOREIGN KEY (username) REFERENCES users (username),
    FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id)
);

CREATE TABLE users(
    username PRIMARY KEY,
    password VARCHAR (40) NOT NULL,   
    creation_date TIMESTAMP NOT NULL,
    last_access_date TIMESTAMP NOT NULL
);

CREATE TABLE email(
    email PRIMARY KEY,
	FOREIGN KEY (username) REFERENCES users (username),
);

CREATE TABLE ingredients(
    ingredient_id SERIAL PRIMARY KEY,
    ingredient_name varchar(255) NOT NULL, --name of each ingredient set to a 255 character max
    aisle varchar(40) --name of a type (dairy, meat, etc.) set to a 40 character limit
);

CREATE TABLE authorship(
    username PRIMARY KEY,
    recipe_id PRIMARY KEY,
    creation_date TIMESTAMP NOT NULL,
    FOREIGN KEY (username) REFERENCES users (username),
    FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id)
);

CREATE TABLE incorporation(
    recipe_id PRIMARY KEY,
    ingredient_id  PRIMARY KEY,
    quantity SMALLINT DEFAULT 0,
    FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients (ingredient_id)
);

CREATE TABLE pantry(
    purchase_date TIMESTAMP PRIMARY KEY,
    username PRIMARY KEY,
    ingredient_id PRIMARY KEY,
    FOREIGN KEY (username) REFERENCES users (username),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients (ingredient_id)
    expiration_date TIMESTAMP,
    current_quantity FLOAT(4), --All items are to be measured in Stones (14lb)
    quantity_bought FLOAT(4) NOT NULL
);
