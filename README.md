# Mood API

Mood API

Tree structure of Categories with an optional parent Category

Categories can contain 0-n Surveys

Surveys are a series of Questions with multiple possible QuestionAnswerChoices

Answer determines the subsequent Question based on a stored regular expression

Response stores the user reponse for a single Question and sets are grouped together in a Report

An Observation allows for the association of Reports for multiple Surveys in a single session


DB Setup on Ubuntu Server

sudo apt-get install wget ca-certificates
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

CREATE DATABASE mood;
CREATE USER mood_admin WITH password 'Bl@ckb00k';
GRANT ALL PRIVILEGES ON DATABASE mood TO mood_admin;
ALTER ROLE mood_admin SET client_encoding TO 'utf8';
ALTER ROLE mood_admin SET default_transaction_isolation TO 'read committed';
