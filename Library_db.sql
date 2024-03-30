DROP DATABASE if exists Library;
CREATE DATABASE Library;
USE Library;
DROP TABLE if exists books;
CREATE table books(bname varchar(50),bcode varchar(10), total int, subject varchar(50));
DROP table if exists issue;
CREATE table issue(name varchar(50),regno varchar(10), bcode int, issue varchar(50));
DROP table if exists members;
CREATE table members(name varchar(50),regno varchar(10));
COMMIT