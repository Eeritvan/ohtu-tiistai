# ohtu-tiistai

[![Status badge](https://github.com/eeritvan/ohtu-tiistai/workflows/CI/badge.svg)](https://github.com/Eeritvan/ohtu-tiistai/actions)
[![codecov](https://codecov.io/gh/Eeritvan/ohtu-tiistai/graph/badge.svg?token=2Z2LTYD1MI)](https://codecov.io/gh/Eeritvan/ohtu-tiistai)

### [backlog](https://github.com/users/Eeritvan/projects/5/views/1)
### [sprint-backlog](https://github.com/users/Eeritvan/projects/5/views/2)


## Contents
- [Running locally](#running-locally)
- [Definition of done](#definition-of-done)

## Running locally
**Prerequisites**
- Poetry version 1.6.1 or later installed

**Installation**
1. Clone this repository
2. Navigate to the cloned directory and create a `.env` file:
```
DATABASE_URL=<YOUR PSQL URL>
TEST_ENV=false
SECRET_KEY=<YOUR SECRET KEY>
```
3. Run `poetry install` to install dependencies and enter virtual environment with `poetry shell`
4. Run `python3 src/db_helper.py` from the root of the directory to setup the database
6. Run `python3 src/index.py` to start the webapp server
7. Navigate to the URL `http://127.0.0.1:5001/`

## Definition of done
- Code is available in the GitHub repository
- Story has Robot Framework tests
- Story has unit tests
- Code passes pylint checks
- Code passes GitHub Actions tests
