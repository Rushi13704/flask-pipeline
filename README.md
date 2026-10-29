# Flask CI/CD and Monitoring Assignment

## Files
- `app.py`: Flask web app on port 5000
- `test_app.py`: automated tests using pytest
- `Dockerfile`: builds the app image
- `Jenkinsfile`: Windows-agent pipeline for tests, Docker, app verification and monitoring
- `monitor.py`: creates an Evidently data-drift HTML report

## Run locally (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest -v
python app.py
```
Open `http://localhost:5000` and `http://localhost:5000/health`.

In a second terminal, run `python monitor.py` to generate `evidently_report.html`.

## Build and run with Docker
```powershell
docker build -t student-app .
docker run --rm -p 5000:5000 student-app
```
If port 5000 is already occupied, stop the other app/container or use `-p 5001:5000` and open `http://localhost:5001`.

## Git and GitHub
Create an empty repository on GitHub, then run these commands in this folder:
```powershell
git init
git add .
git commit -m "Initial Flask CI/CD application"
git branch -M main
git remote add origin REPOSITORY_URL
git push -u origin main
```
Replace `REPOSITORY_URL` with your actual GitHub repository URL. If a remote already exists, inspect it with `git remote -v` before changing it.

## Jenkins notes
This `Jenkinsfile` uses Windows `bat` steps and assumes the Jenkins agent can access `python`, `git`, and `docker` on its PATH and that Docker Desktop is running. If Jenkins runs on Linux or inside a container, the pipeline commands and tool access need adapting. The monitoring stage creates the HTML report in the Jenkins workspace; archive it in Jenkins if you need to retain it as a build artifact.
