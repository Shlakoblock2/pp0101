from fastapi import APIRouter
from SERVER.SQL.models import City
from SERVER.resolvers import city

router = APIRouter(prefix='/City', tags=['City'])

@router.post('/create')
def create(_City: City) -> int:
    new_id = city.create(_City)
    return f'{{code: 201, id: {new_id}}}'

@router.get('/get/{city_id}')
def get(city_id: int) -> City | None:
    return city.get(city_id)

@router.get('/')
def get_all() -> list[City] | None:
    return city.get_all()

@router.get('/remove/{city_id}')
def remove(city_id: int) -> None:
    return city.remove(city_id)


@router.put("/update/{city_id}")
def update(city_id: int, new_data: City):
    return city.update(city_id=city_id, new_data=new_data)

