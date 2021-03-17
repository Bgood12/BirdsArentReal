DROP TABLE IF EXISTS recipes, categories, cooks, users, email, ingredients, authorship, incorporation, pantry;

CREATE TABLE recipes(
    recipe_id SERIAL PRIMARY KEY,
    ...
);

CREATE TABLE categories(
    recipe_id PRIMARY KEY,
    name VARCHAR(40)

);

CREATE TABLE cooks(
    user_id PRIMARY KEY,
    recipe_id PRIMARY KEY,
    creation_date TIMESTAMP
    ...
);

CREATE TABLE users(
    username PRIMARY KEY,
    ...

);

CREATE TABLE email(
    email PRIMARY KEY,

);

CREATE TABLE ingredients(
    ingredient_id SERIAL PRIMARY KEY,

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
    ingredient_id SERIAL PRIMARY KEY,
    ...

);