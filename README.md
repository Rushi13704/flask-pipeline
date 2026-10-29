# Flask MLOps CI/CD Assignment

A simple Flask web application demonstrating Git/GitHub, Pytest, Docker, Jenkins CI/CD, and basic data-drift monitoring with Evidently.

Repository: https://github.com/Rushi13704/flask-pipeline

## 1. Clone the repository

Open PowerShell or the VS Code terminal:

```powershell
git --version
git clone https://github.com/Rushi13704/flask-pipeline.git
cd flask-pipeline
dir
```

If the folder already exists, update it instead:

```powershell
cd flask-pipeline
git pull origin main
```

## 2. Set up Python

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell blocks virtual-environment activation, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

If `requirements.txt` is missing, install the packages directly:

```powershell
python -m pip install flask pytest pandas evidently==0.7.23
```

## 3. Run the Flask application

```powershell
python app.py
```

Open these URLs:

- Main page: http://localhost:5000/
- Health endpoint: http://localhost:5000/health

Expected main page text:

```text
Hello! Flask application is running.
```

Stop the local server with `Ctrl+C`.

## 4. Run Pytest

```powershell
python -m pytest -v
```

Expected result: all discovered tests pass. If no tests are discovered, check that `test_app.py` exists and test functions start with `test_`.

## 5. Build and run with Docker

Make sure Docker Desktop is open and the Docker Engine is running.

```powershell
docker --version
docker info
docker images
docker ps -a
```

From the folder containing the `Dockerfile`, build the image:

```powershell
docker build -t student-app .
```

Run the application in the foreground:

```powershell
docker run --rm -p 5000:5000 student-app
```

Open http://localhost:5000/. Stop it with `Ctrl+C`. `--rm` removes the container when it stops, but keeps the image.

To run in the background and keep the container for inspection:

```powershell
docker run -d --name student-app-container -p 5000:5000 student-app
docker ps
docker logs student-app-container
```

Stop, restart, and remove that container:

```powershell
docker stop student-app-container
docker start student-app-container
docker ps -a
docker rm -f student-app-container
```

If port 5000 is occupied, use a different host port:

```powershell
docker run --rm -p 5001:5000 student-app
```

Then open http://localhost:5001/.

## 6. Evidently monitoring report

```powershell
python -m pip install pandas evidently==0.7.23
python monitor.py
Test-Path .\evidently_report.html
Start-Process .\evidently_report.html
```

Run `Start-Process` only if `Test-Path` returns `True`. This demonstration uses sample reference/current data to create a data-drift report.

## 7. Jenkins setup

### Option A: Freestyle project

1. Open Jenkins at http://localhost:8080/.
2. Click **New Item**, enter a name, and select **Freestyle project**.
3. Under **Source Code Management**, select **Git**.
4. Repository URL: `https://github.com/Rushi13704/flask-pipeline.git`
5. Branch specifier: `*/main`.
6. Under **Build Steps**, select **Add build step → Execute Windows batch command**.
7. Add these commands, then click **Save → Build Now**.
8. Open **Console Output** to inspect the result.

```bat
@echo off
python --version
git --version
docker --version
python -m pip install -r requirements.txt
if errorlevel 1 exit /b 1
python -m pytest -v
if errorlevel 1 exit /b 1
docker build -t student-app .
if errorlevel 1 exit /b 1
```

This assumes Python, Git, and Docker are available to the account running Jenkins. A Windows Jenkins service running as `SYSTEM` may have a different PATH from your normal terminal. If `python` or `docker` is not recognized, configure the executable paths/PATH for the Jenkins service account or use a correctly configured agent, then retry.

### Option B: Pipeline job using Jenkinsfile

Use this only if `Jenkinsfile` is committed in the repository:

1. Create a **Pipeline** job.
2. Under **Definition**, select **Pipeline script from SCM**.
3. SCM: **Git**.
4. Repository URL: `https://github.com/Rushi13704/flask-pipeline.git`
5. Branch: `*/main`.
6. Script Path: `Jenkinsfile`.
7. Save and click **Build Now**.

The Jenkinsfile must match the agent operating system: Windows uses `bat`; Linux uses `sh`. Docker must be installed, running, and accessible to the agent.

### Jenkins port note

If Windows Jenkins is already using port 8080, a Jenkins container cannot use the same host port at the same time. Use the existing Windows Jenkins at http://localhost:8080/ or configure the container to use a different available host port. Do not delete Jenkins containers or data volumes unless you are sure they are no longer needed.

## 8. Push changes to GitHub

```powershell
git status
git add .
git commit -m "Update assignment instructions"
git push
```

For the first push of a new local branch:

```powershell
git branch -M main
git push -u origin main
```

If `origin` already exists, inspect it first:

```powershell
git remote -v
```

## 9. Troubleshooting

| Problem | What to do |
|---|---|
| `python` is not recognized | Install Python or use its full path; ensure Python is on PATH. |
| `docker` is not recognized | Start Docker Desktop; check Docker CLI path and PATH. |
| Docker Engine error | Open Docker Desktop and wait until the Engine is running. |
| Port 5000 is occupied | Stop the other app/container or use `-p 5001:5000`. |
| Port 8080 is occupied | Another service (often Windows Jenkins) is using it; don't start a second Jenkins on the same host port. |
| Pytest says no tests ran | Check `test_app.py` and ensure test functions start with `test_`. |
| Jenkins cannot find Python/Docker | Jenkins may have a different PATH or account permissions from your terminal. |
| Git asks for credentials | Public repositories usually need no credentials to clone; private repositories require credentials. |

## 10. Practical workflow summary

1. Clone the repository.
2. Install dependencies.
3. Run the Flask app and verify it in the browser.
4. Run Pytest and confirm tests pass.
5. Build the Docker image.
6. Run the container and verify the application.
7. Run `monitor.py` and confirm the Evidently HTML report exists.
8. Configure Jenkins to fetch the repository and run tests/build steps.
9. Check Jenkins Console Output and record success/failure in the practical summary report.

Run commands from the project directory unless a step says otherwise. Use the exact filenames present in the cloned repository.
