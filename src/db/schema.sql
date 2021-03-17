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
    creation_date DATETIME 'might be called something else
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
    username PRIMARY KEY,
    recipe_id PRIMARY KEY,
    ...
);

CREATE TABLE incorporation(
    recipe_id PRIMARY KEY,
    ingredient_id SERIAL PRIMARY KEY,
    ...

);

CREATE TABLE pantry(
    purchase_date PRIMARY KEY DATETIME,
    username PRIMARY KEY,
    ingredient_id SERIAL PRIMARY KEY,
    ...

);