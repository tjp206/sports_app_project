DROP TABLE IF EXISTS results;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS games;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    coach VARCHAR(255),
    wins INT,
    losses INT
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE results (
    ID SERIAL PRIMARY KEY,
    scores INT,
    team_id SERIAL REFERENCES teams(id),
    game_id SERIAL REFERENCES games(id)
);