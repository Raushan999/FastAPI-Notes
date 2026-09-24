# FastAPI Notes

This project is a simple FastAPI learning workspace focused on building and testing API endpoints for a drug interaction example.

## Project contents

- `fastapi_theory.ipynb`[fastapi_theory](notebooks/fastapi_theory@main.py)  — notebook with FastAPI theory, examples, and experiments
- `fastapi_theory@main.py`[fastapi_theory_main](notebooks/fastapi_theory@main.py) — standalone FastAPI application example
- `app/` — app package folder for organizing project code
- `notebooks/` — notebook files
- `data/` — datasets or sample input files
- `docs/` — notes and documentation
- `tests/` — test files


## Setup

```bash
pip install fastapi uvicorn pydantic
```

## Run the API

From the project root:

```bash
uvicorn fastapi_theory@main:app --reload
```

If you want to run the app from a package module instead, use:

```bash
uvicorn app.main:app --reload
```

## Example routes

The sample app includes routes such as:

- `/` — home endpoint
- `/drugs` — list all drugs
- `/drugs/{drug_name}` — get a specific drug
- `/search?name=Aspirin` — search by query parameter
- `/check-interaction` — POST request to check drug interaction
- `/interactions/{drug_name}` — fetch interaction records
- `/project` — dependency-based project metadata

## Accessing the API docs

Once the server is running, open:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Notes

This repo is intended for learning and experimentation with FastAPI fundamentals, request handling, validation with Pydantic, and dependency injection.