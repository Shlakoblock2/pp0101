from fastapi import APIRouter
from SERVER.SQL.models import Cart
from SERVER.resolvers import cart

router = APIRouter(prefix='/Cart', tags=['Cart'])

@router.post('/create')
def create(_Cart: Cart) -> int:
    new_id = cart.create(_Cart)
    return f'{{code: 201, id: {new_id}}}'

@router.get('/get/{cart_id}')
def get(cart_id: int) -> Cart | None:
    return cart.get(cart_id)

@router.get('/')
def get_all() -> list[Cart] | None:
    return cart.get_all()

@router.get('/remove/{cart_id}')
def remove(cart_id: int) -> None:
    return cart.remove(cart_id)


@router.put("/update/{cart_id}")
def update(cart_id: int, new_data: Cart):
    return cart.update(cart_id=cart_id, new_data=new_data)

