-- Your SQL goes here
CREATE TABLE Csa(
  id SERIAL PRIMARY KEY,
  csaName VARCHAR(100) NOT NULL,
  lat FLOAT,
  lon FLOAT,
  address TEXT,
  stateAbbrev VARCHAR(3)
);

CREATE TABLE Region(
  regionName VARCHAR(100) PRIMARY KEY,
  stateAbbrev VARCHAR(3) NOT NULL
);

-- 0 = Vegetable
-- 1 = Fruit,
-- 2 = Meat,
-- 3 = Seed,
-- 4 = Grain,
-- 5 = Processed,
-- 6 = Dairy,
-- 7 = Gourd,
-- 8 = Flower,
-- 9 = Herb,
-- 10 = Fiber,
-- 11 = Sprout,
-- 12 = Specialty,
CREATE TABLE Produce(
  produceName VARCHAR(100) PRIMARY KEY,
  category INT NOT NULL
);

-- 0 = Winter
-- 1 = Spring
-- 2 = Summer
-- 3 = Fall
CREATE TABLE Production(
  csaId INT,
  produceName VARCHAR(100),
  season INT,
  PRIMARY KEY(csaId, producename, season)
);

CREATE TABLE Fish(
  species VARCHAR(100) PRIMARY KEY,
  regionName VARCHAR(100) NOT NULL,
  january BOOLEAN NOT NULL,
  february BOOLEAN NOT NULL,
  march BOOLEAN NOT NULL,
  april BOOLEAN NOT NULL,
  may BOOLEAN NOT NULL,
  june BOOLEAN NOT NULL,
  july BOOLEAN NOT NULL,
  august BOOLEAN NOT NULL,
  september BOOLEAN NOT NULL,
  october BOOLEAN NOT NULL,
  november BOOLEAN NOT NULL,
  december BOOLEAN NOT NULL
);
