from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = None

class User(BaseModelModify):
    login: str
    password : str
    power_level: int

class Applications(User):
    power_level: int
    add_date str,
    UserID int,
    child_data str,
    comments str,
    date_completion str,

