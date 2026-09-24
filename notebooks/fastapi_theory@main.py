from fastapi import FastAPI 

app = FastAPI()

drugs = [
    "Paracetamol",
    "Aspirin",
    "Warfarin",
    "Atorvastatin",
]

#! Home page at http://127.0.0.1:8000
@app.get("/")
def home():
    return {"message": "drug interaction testing"}

#! http://127.0.0.1:8000/drugs/ 
@app.get("/drugs")
def get_drugs():
    return drugs

#! http://127.0.0.1:8000/drugs/Aspirin 
@app.get("/drugs/{drug_name}")
def get_drugs(drug_name: str):
    return {"drug": drug_name}

# !calling at: http://127.0.0.1:8000/search?name=Aspirin
@app.get("/search")
def search_drugs(name: str = "", limit: int = 10):
    return {"search": name}


## !Following the pydantic, structured input/output model.
from pydantic import BaseModel
class InteractionRequest(BaseModel):
    drug_a : str 
    drug_b : str

@app.post("/check-interaction")
def check_interaction(request: InteractionRequest):
    return {
        "drug_a": request.drug_a, 
        "drug_b": request.drug_b
    }

# !Validation: pydantic can express constraints. 
from pydantic import BaseModel, Field

class DrugRequest(BaseModel):
    drug_name : str = Field(min_length= 2, max_length= 100)

@app.post("/check-drugName")
def check_drugName(request: DrugRequest):
    return {"drug_name_received": request.drug_name}

interactions = [
    {
        "drug_a": "Aspirin",
        "drug_b": "Warfarin",
        "level": "Major"
    },
    {
        "drug_a": "Aspirin",
        "drug_b": "Ibuprofen",
        "level": "Major"
    },
    {
        "drug_a": "Atorvastatin",
        "drug_b": "Clarithromycin",
        "level": "Major"
    }
]

# !sample code to test if any drug is showing any interaction
# http://127.0.0.1:8000/interactions/random_drug : This will return the name of the drug which is interacting with our drug. 
@app.get("/interactions/{drug_name}")
def get_interactions(drug_name: str):
    results = []

    for interaction in interactions:
        if (
            interaction["drug_a"].lower() == drug_name.lower()
            or interaction["drug_b"].lower() == drug_name.lower()
        ):
            results.append(interaction)

    return {
        "drug": drug_name,
        "interactions": results
    }


# ! Dependency ingestion
from fastapi import Depends

def get_project_name():
    return "Drug Interaction API"

@app.get("/project")
def project_info(project_name: str = Depends(get_project_name)):
    return {"project": project_name}