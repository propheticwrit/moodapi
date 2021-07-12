# Mood API

Mood API

Tree structure of Categories with an optional parent Category

Categories can contain 0-n Surveys

Surveys are a series of Questions with multiple possible QuestionAnswerChoices

Answer determines the subsequent Question based on a stored regular expression

Response stores the user reponse for a single Question and sets are grouped together in a Report

An Observation allows for the association of Reports for multiple Surveys in a single session
