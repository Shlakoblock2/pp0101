from fastapi import APIRouter
from SERVER.SQL.models import Users
from SERVER.resolvers import user

router = APIRouter(prefix='/Users', tags=['Users'])

@router.post('/create/')
def register(_user: Users):
    new_id = user.create(_user)
    return new_id

@router.get('/get/{user_id}')
def get(user_id: int) -> Users | None:
    return user.get(user_id)

@router.get('/')
def get_all() -> list[Users] | None:
    return user.get_all()

@router.delete('/remove/{user_id}')
def remove(user_id: int) -> None:
    return user.remove(user_id)


@router.put("/update/{user_id}")
def update(user_id: int, new_data: Users):
    return user.update(user_id=user_id, new_data=new_data)

@router.get('/login')
def login( name: str, password: str):
        return user.Login(name, password)

