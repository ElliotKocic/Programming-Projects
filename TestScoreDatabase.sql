CREATE DATABASE IF NOT EXISTS testScoresDB;

USE testScoresDB;
DROP TABLE IF EXISTS studentTestScores;
CREATE TABLE studentTestScores (

studentID INT NOT NULL AUTO_INCREMENT,
name VARCHAR (30),
testScoreICT INT,
testScoreMaths INT,
testScoreChemistry INT,

PRIMARY KEY(studentID)

);