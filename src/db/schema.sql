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
    recipe_id PRIMARY KEY NOT NULL,
    name VARCHAR(40) NOT NULL, --Name of recipe limited to 40 characters
    FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id)
);

CREATE TABLE cooks(
    username PRIMARY KEY NOT NULL, -- We put User_id in the Reduction, think it should be username
    recipe_id PRIMARY KEY NOT NULL,
    creation_date PRIMARY KEY NOT NULL,
    rating FLOAT(1,2) DEFAULT 0.00, --Not sure how many decimal points we want to round to. Defaulted to 0.00 rating.
    servings SMALLINT DEFAULT 0, --Defaulted to 0 servings
    FOREIGN KEY (username) REFERENCES users (username),
    FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id)
);

CREATE TABLE users(
    username PRIMARY KEY NOT NULL,
    password VARCHAR (20) NOT NULL,   -- Set password limit to 20 characters
    creation_date TIMESTAMP NOT NULL,
    last_access_date DATETIME NOT NULL
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
    username PRIMARY KEY NOT NULL,
    recipe_id PRIMARY KEY NOT NULL,
    creation_date TIMESTAMP NOT NULL,
    FOREIGN KEY (username) REFERENCES users (username),
    FOREIGN KEY (recipe_id) REFERENCES recipes (recipe_id)
);

CREATE TABLE incorporation(
    recipe_id PRIMARY KEY NOT NULL,
    ingredient_id SERIAL PRIMARY KEY,
    quantity INT DEFAULT 0,
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
