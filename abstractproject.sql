CREATE DATABASE abstractproject;
USE abstractproject;

CREATE TABLE book (
  bookId int NOT NULL AUTO_INCREMENT,
  name varchar(45) NOT NULL,
  description varchar(255) NOT NULL,
  userId int NOT NULL,
  PRIMARY KEY (bookId)
);

CREATE TABLE user (
  userId int NOT NULL AUTO_INCREMENT,
  name varchar(45) NOT NULL,
  email varchar(45) NOT NULL,
  password varchar(255) NOT NULL,
  PRIMARY KEY (userId)
);

ALTER TABLE book
ADD FOREIGN KEY (userId) REFERENCES user(userId);