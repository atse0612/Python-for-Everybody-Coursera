CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Davie', 20);
INSERT INTO Ages (name, age) VALUES ('Daanyaal', 20);
INSERT INTO Ages (name, age) VALUES ('Ireayomide', 19);
INSERT INTO Ages (name, age) VALUES ('Jagat', 34);

SELECT hex(name || age) AS X FROM Ages ORDER BY X

