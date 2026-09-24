# Drug Interaction API

This project is a small FastAPI learning app for testing drug-related endpoints and exploring request validation, query parameters, and dependency injection.

## Live API

Base URL:

https://drug-interaction-api-mehu.onrender.com/

Swagger docs:

https://drug-interaction-api-mehu.onrender.com/docs

Redoc docs:

https://drug-interaction-api-mehu.onrender.com/redoc

## Project structure

- [app/main.py](app/main.py) — FastAPI application
- [fastapi_theory.ipynb](fastapi_theory.ipynb) — notebook notes and examples
- [fastapi_theory@main.py](fastapi_theory@main.py) — original standalone script version
- [data](data) — sample data folder
- [docs](docs) — documentation notes
- [tests](tests) — future tests

## Local setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Sample requests

### 1) Home endpoint

```bash
curl https://drug-interaction-api-mehu.onrender.com/
```

### 2) List all drugs

```bash
curl https://drug-interaction-api-mehu.onrender.com/drugs
```

### 3) Search drugs

```bash
curl "https://drug-interaction-api-mehu.onrender.com/search?name=Aspirin&limit=5"
```

### 4) Get interactions for a specific drug

```bash
curl https://drug-interaction-api-mehu.onrender.com/interactions/Aspirin
```

### 5) Check a drug interaction request

```bash
curl -X POST https://drug-interaction-api-mehu.onrender.com/check-interaction \
  -H "Content-Type: application/json" \
  -d '{"drug_a":"Aspirin","drug_b":"Warfarin"}'
```

### 6) Validate a drug name

```bash
curl -X POST https://drug-interaction-api-mehu.onrender.com/check-drugName \
  -H "Content-Type: application/json" \
  -d '{"drug_name":"Aspirin"}'
```

### 7) Project metadata endpoint

```bash
curl https://drug-interaction-api-mehu.onrender.com/project
```

## Supported endpoints

- `GET /` — health/home message
- `GET /health` — simple status check
- `GET /drugs` — list all drugs
- `GET /drugs/{drug_name}` — fetch a specific drug name
- `GET /search` — filter results using a query parameter
- `POST /check-interaction` — test a drug pair using JSON body
- `POST /check-drugName` — validate a name through Pydantic
- `GET /interactions/{drug_name}` — return related interaction records
- `GET /project` — dependency injection example

## Notes

This project is designed for learning and quick API testing, especially for FastAPI basics, path parameters, validation, JSON payloads, and dependency injection.