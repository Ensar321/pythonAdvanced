from docutils.nodes import status
from fastapi import FastApi,HTTPException
from typing import list
import database
import models
from mdoels import Movie,MovieCreate

app = FastApi()
@app.get('/')
def read_root():
    return {"Message":"Welcome to teh movies CRUD API"}

@app.get('/movies/',response_model=List[Movie])
def read_movies():
    return database.read_movies()

@app.get('/movies/movie_id/',response_model=Movie)
def read_movies(movie_id:int):
    movie=database.read_movies(movie_id)
    if movie is None:
        return HTTPException(status_code=404,detail="Movie not found")
    return movie