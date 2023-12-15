from fastapi import APIRouter
from SERVER.SQL.models import Children
from SERVER.resolvers import children

router = APIRouter(prefix='/Children', tags=['Children'])

@router.post('/create')
def create(_Children: Children) -> int:
    new_id = children.create(_Children)
    return f'{{code: 201, id: {new_id}}}'

@router.get('/get/{children_id}')
def get(children_id: int) -> Children | None:
    return children.get(children_id)

@router.get('/')
def get_all() -> list[Children] | None:
    return children.get_all()

@router.get('/remove/{children_id}')
def remove(children_id: int) -> None:
    return children.remove(children_id)


@router.put("/update/{children_id}")
def update(children_id: int, new_data: Children):
    return children.update(children_id=children_id, new_data=new_data)

