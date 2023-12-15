from fastapi import APIRouter
from SERVER.SQL.models import Applications
from SERVER.resolvers import applications

router = APIRouter(prefix='/Applications', tags=['Applications'])

@router.post('/create')
def create(_Applications: Applications):
    new_id = applications.create(_Applications)
    return new_id

@router.get('/get/{applications_id}')
def get(applications_id: int) -> Applications | None:
    return applications.get(applications_id)

@router.get('/')
def get_all():
    return applications.get_all()

@router.get('/remove/{applications_id}')
def remove(applications_id: int) -> None:
    return applications.remove(applications_id)


@router.put("/update/{applications_id}")
def update(applications_id: int, new_data: Applications):
    return applications.update(applications_id=applications_id, new_data=new_data)

