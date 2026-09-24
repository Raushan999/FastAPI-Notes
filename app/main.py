from fastapi import Depends, FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI(
    title="Drug Interaction API",
    version="1.0.0",
    description="A simple FastAPI app for learning API creation, validation, and dependency injection.",
)


drugs = [
    "Paracetamol",
    "Aspirin",
    "Warfarin",
    "Atorvastatin",
]


class InteractionRequest(BaseModel):
    drug_a: str
    drug_b: str


class DrugRequest(BaseModel):
    drug_name: str = Field(min_length=2, max_length=100)


interactions = [
    {"drug_a": "Aspirin", "drug_b": "Warfarin", "level": "Major"},
    {"drug_a": "Aspirin", "drug_b": "Ibuprofen", "level": "Major"},
    {"drug_a": "Atorvastatin", "drug_b": "Clarithromycin", "level": "Major"},
]


@app.get("/")
def home():
    return {"message": "Drug interaction testing"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/drugs")
def get_drugs():
    return drugs


@app.get("/drugs/{drug_name}")
def get_drug_by_name(drug_name: str):
    return {"drug": drug_name}


@app.get("/search")
def search_drugs(
    name: str = Query(default="", min_length=1),
    limit: int = Query(default=10, ge=1, le=50),
):
    matches = [drug for drug in drugs if name.lower() in drug.lower()]
    return {"search": name, "results": matches[:limit]}


@app.post("/check-interaction")
def check_interaction(request: InteractionRequest):
    return {
        "drug_a": request.drug_a,
        "drug_b": request.drug_b,
        "message": "Interaction check received",
    }


@app.post("/check-drugName")
def check_drug_name(request: DrugRequest):
    return {"drug_name_received": request.drug_name}


@app.get("/interactions/{drug_name}")
def get_interactions(drug_name: str):
    results = []

    for interaction in interactions:
        if (
            interaction["drug_a"].lower() == drug_name.lower()
            or interaction["drug_b"].lower() == drug_name.lower()
        ):
            results.append(interaction)

    return {"drug": drug_name, "interactions": results}


def get_project_name():
    return "Drug Interaction API"


@app.get("/project")
def project_info(project_name: str = Depends(get_project_name)):
    return {"project": project_name}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
