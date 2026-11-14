from pyarrow import StructArray
from pydantic import  BaseModel
class MovieCreate(BaseModel):
    title:str
    director:Str

class Movie(MovieCreate):
    id:int
