# Student Management System

A Python-based student management system with Git version control, GitHub collaboration, and CI/CD via GitHub Actions.

## Project Overview

This project implements a simple student record manager with the following functions:
- `add_student()` – Add a new student.
- `remove_student()` – Remove a student by ID.
- `search_student()` – Search students by ID or name.
- `update_student()` – Update student name and/or grade.
- `export_students()` – Export all records as a CSV‑style string (bonus feature).

Student records are stored in a Python dictionary (`students`) where keys are student IDs and values are dictionaries with `name` and `grade`.

## Repository Structure
student-management-system/
├── student.py # Core functions
├── test_student.py # Pytest test suite (12 tests)
├── requirements.txt # Dependencies (pytest)
├── .github/
│ └── workflows/
│ └── python.yml # GitHub Actions CI workflow
├── Dockerfile # Docker support (optional)
├── docker-compose.yml # Docker Compose (optional)
└── README.md

## Setup

### 1. Clone the repository

git clone https://github.com/AlexGithub901/Student-Management-System.git
cd Student-Management-System
2. Install dependencies
bash
pip install -r requirements.txt
3. Run the test suite
bash
pytest test_student.py -v
All tests should pass.

Git Commands Used
The following Git commands were used throughout the development workflow:

Command	Purpose
git init	Initialize a new Git repository.
git add .	Stage all changes.
git commit -m "message"	Commit staged changes with a meaningful message.
git remote add origin <url>	Connect local repo to GitHub remote.
git push -u origin main	Push the main branch and set upstream.
git pull origin main --allow-unrelated-histories	Merge remote changes (when GitHub already had files).
git branch <branch-name>	Create a new branch.
git checkout <branch>	Switch to an existing branch.
git checkout -b <branch>	Create and switch to a new branch.
git push -u origin <branch>	Push a specific branch to GitHub and set upstream.
git merge	Merge branches (performed via GitHub Pull Requests).
Branching strategy:

main – The default stable branch.

feature-student-search – Branch for implementing/enhancing the search feature.

feature-export – Bonus branch for the export function.

GitHub Actions Workflow
The CI pipeline is defined in .github/workflows/python.yml and is triggered on:

push to main, feature-student-search, or feature-export

pull_request targeting main

Workflow steps:

Check out the code.

Set up Python 3.12.

Install dependencies from requirements.txt.

Run pytest test_student.py -v.

If any test fails, the workflow fails and blocks merging.

Docker Support (Optional)
You can also run tests inside a Docker container:

bash
docker build -t student-manager .
docker run --rm student-manager
Or using Docker Compose:

bash
docker-compose up --build
GitHub Pull Requests
Two Pull Requests were created and merged:

feature-student-search – Enhanced search_student() to return structured dictionaries. A bug was intentionally introduced and then fixed; the workflow successfully caught the failure.

feature-export – Added export_students() and a corresponding test. The workflow passed before merging.

All Pull Requests targeted the main branch and required passing checks before merging.

Submission Materials
GitHub Repository: https://github.com/AlexGithub901/Student-Management-System

Screenshots (submitted separately):

Successful GitHub Actions workflow

Failed GitHub Actions workflow (from intentional bug)

Pull Request page

Final merged repository is available on the main branch.

This README was prepared as part of the Git, GitHub & GitHub Actions Industry Assignment.
