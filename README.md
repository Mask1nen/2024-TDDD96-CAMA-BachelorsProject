# Öppna miljön med docker

1. installera docker compose https://docs.docker.com/compose/install/
2. *Om första gången:* I projekt-rooten skriv `docker compose build` 
3. Fortfarande i projekt-rooten skriv `docker compose up`

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

- **main** - Rör oftast ej. Release mergeas hit när den är färdig.

- **dev** - Rör oftast ej. Skapa merge requests hit från färdiga feature branches från gitlab (code->branches->[din branch]->create merge request)

- **feature** - Här sker utveckling. Skapa från dev med `git switch -c feat/[user story number]-[short desc]`
  - Man kan göra brancher från feature brancher för att t.ex dela upp arbete enklare med ex `git switch -c feat/[user story number]-[short desc]/[short desc2]`


- **release** - Mergeas med dev inför release. `git merge dev`

- **hotfix** - Skapas från main om det behövs. `git switch -c hotfix/[short desc]`



## Öppna miljön första gången
1. installera docker copmose https://docs.docker.com/compose/install/
2. I rooten skriv `docker compose build`
3. Fortfarande i rooten skriv `docker compose up`

In case of error, try: `docker compose up -V `


# Öppna miljön lokalt (använd docker istället)
1. Installera python venv

2. `python3 -m venv .venv`

3. Linux/Git Bash: `source .venv/bin/activate`\
   Windows/Powershell: `.venv/Scripts/activate`

4. Installera python dependencies `python3 -m pip install -r requirements.txt`

5. Starta django-server i cama\_backend `python3 manage.py runserver`

6. Starta frontend i cama\_frontend i dev mode `npm start`

# Köra tester lokalt
1. Gå till root

2. cd cama_backend

## Utan coverage report i html:
3. pytest --cov=myapi tests/

## Med coverage report i html (bättre djup)
3. pytest --cov-report html:cov_html --cov-config=.coveragerc --cov=myapi tests/

4. Öppna den nu skapade cov_html mappen och öppna index.html för att undersöka vad som behöver testas