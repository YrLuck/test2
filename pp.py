from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import wikipedia


app = FastAPI()


class Title(BaseModel):
    title: str


class Page(BaseModel):
    title: str
    content: str


class Word(BaseModel):
   word: str


class Lst(BaseModel):
    lst: list[str]


@app.post("/suggest_word", response_model=Word)
def src_page_with_ans_lim(title: str):
    sug = wikipedia.suggest(title)
    return Word(word=sug)


@app.post("/page/wiki_page_summary", response_model=Page)
def rq_page(title: Title):
    try:
        return wikipedia.page(title.title)
    except wikipedia.exceptions.DisambiguationError:
        raise HTTPException(status_code=300, detail="disambiguation")
    except ValueError:
        return HTTPException(status_code=303, detail="invalid title")
    except wikipedia.exceptions.PageError:
        return HTTPException(status_code=404, detail="not found")


@app.post("/search/{srch}", response_model=Lst)
def src_page(srch: str = "Python_(programming_language)"):
    page = wikipedia.search(srch)
    return Lst(lst=page)
