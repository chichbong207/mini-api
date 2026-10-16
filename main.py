from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Mini API de statistiques")

# Données en mémoire (à remplacer par un fichier CSV ou une base)
scores = {
    "math": [7.5, 8.0, 6.5, 9.0],
    "anglais": [8.5, 7.0, 9.5],
}

class Note(BaseModel):
    valeur: float

@app.get("/")
def accueil():
    return {"message": "API en ligne"}

@app.get("/matieres")
def liste_matieres():
    return list(scores.keys())

@app.get("/matieres/{nom}/stats")
def stats(nom: str):
    if nom not in scores:
        raise HTTPException(status_code=404, detail="Matière inconnue")
    notes = scores[nom]
    return {
        "matiere": nom,
        "nombre": len(notes),
        "moyenne": sum(notes) / len(notes),
        "min": min(notes),
        "max": max(notes),
    }

@app.post("/matieres/{nom}/notes")
def ajouter_note(nom: str, note: Note):
    scores.setdefault(nom, []).append(note.valeur)
    return {"matiere": nom, "nombre": len(scores[nom])}