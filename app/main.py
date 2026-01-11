from fastapi import FastAPI, HTTPException
from app.models import Term, TermUpdate
from app.storage import get_all_terms, get_term, add_term, update_term, delete_term

app = FastAPI()


@app.get("/terms", response_model=list[Term])
def list_terms():
    return get_all_terms()


@app.get("/terms/{title}", response_model=Term)
def get_term_by_title(title: str):
    term = get_term(title)
    if not term:
        raise HTTPException(status_code=404, detail="Термин не найден")
    return term


@app.post("/terms", response_model=Term, status_code=201)
def create_term(term: Term):
    result = add_term(term)
    if not result:
        raise HTTPException(status_code=400, detail="Термин уже существует")
    return result


@app.put("/terms/{title}", response_model=Term)
def update_existing_term(title: str, update: TermUpdate):
    term = update_term(title, definition=update.definition,
                       source_link=update.source_link)
    if not term:
        raise HTTPException(status_code=404, detail="Термин не найден")
    return term


@app.delete("/terms/{title}", response_model=Term)
def delete_existing_term(title: str):
    term = delete_term(title)
    if not term:
        raise HTTPException(status_code=404, detail="Термин не найден")
    return term
