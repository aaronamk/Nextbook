DROP TABLE IF EXISTS textbook;
DROP TABLE IF EXISTS review;
DROP TABLE IF EXISTS textbook_comment;

CREATE TABLE textbook (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  author TEXT NOT NULL,
  ISBN INTEGER NOT NULL
);

CREATE TABLE review (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  score INTEGER NOT NULL,
  textbook INTEGER NOT NULL
);

CREATE TABLE textbook_comment (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  body TEXT NOT NULL
);
