from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = None

class Users(BaseModelModify):
    login: str
    password : str
    power_level: Optional[int]

class children(BaseModelModify):
    cityID:int
    name:str
    surname:str
    age:int

class city(BaseModelModify):
    name:str
    
class Applications(BaseModelModify):
    add_date:str
    UserID:int
    childID:int
    comments:str
    date_completion:str
