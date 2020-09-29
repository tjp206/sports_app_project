DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    coach VARCHAR(255),
    wins INT,
    losses INT
);

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    position VARCHAR(255),
    rating INT,
    team_id INT REFERENCES teams(id) ON DELETE CASCADE
);

CREATE TABLE games (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    home_team_id INT REFERENCES teams(id) ON DELETE CASCADE,
    away_team_id INT REFERENCES teams(id) ON DELETE CASCADE
);

