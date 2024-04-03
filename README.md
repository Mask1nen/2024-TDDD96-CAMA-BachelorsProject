# Commit-meddelanden
Commitmeddelanden kontrolleras efter regex:
```regex
(\d{1,4}|N\/A) (fix|feat|refactor|test|doc|other): .*
```

Ex:

`101 fix: fixed this`

`N/A other: did something that does not go under category`

`50 feat: landing page done`


# Brancher

- main - rör ej

- dev - Rör oftast ej. Skapa merge requests hit från färdiga feature branches från gitlab (code->branches->[din branch]->create merge request)

- feature - Här sker utveckling skapa från main med `git switch -c feat/[user story number]-[short desc]`
  - Man kan göra brancher från feature brancher för att t.ex dela upp arbete enklare med ex `git switch -c feat/[user story number]-[short desc]/[short desc2]`


- release - Vid release för att uppdatera denna branch kör `git merge dev`

- hotfix - Skapas från main om det behövs från main med `git switch -c hotfix/[short desc]`


# Introduction
TODO: Give a short introduction of your project. Let this section explain the objectives or the motivation behind this project.

# Getting Started
TODO: Guide users through getting your code up and running on their own system. In this section you can talk about:
1.	Installation process
2.	Software dependencies
3.	Latest releases
4.	API references

# Build and Test
TODO: Describe and show how to build your code and run the tests.


## Öppna miljön med docker

1. installera docker copmose https://docs.docker.com/compose/install/
2. I rooten skriv `docker compose build`
3. Fortfarande i rooten skriv `docker compose up`

## Öppna miljön första gången

1. Installera python venv

2. `python3 -m venv .venv`

3. Linux/Git Bash: `source .venv/bin/activate`\
   Windows/Powershell: `.venv/Scripts/activate`

4. Installera python dependencies `python3 -m pip install -r requirements.txt`

5. Starta django-server i cama\_backend `python3 manage.py runserver`

6. Starta frontend i cama\_frontend i dev mode `npm start`
