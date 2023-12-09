from SERVER.SQL.models import User
from SERVER.SQL.dbmanager import DbManager

dbmanager = DbManager(base_path='SERVER/SQL/shop.db')


def create(_user: User) -> int:
    new_id = dbmanager.execute(
        query="insert into users(login, password) values(?, ?)",
        args=(_user.login, _user.password)
    )
    return new_id

def get(user_id: int) -> User | None:
    res = dbmanager.execute(
        query='select * from users where id=(?)',
        args=(user_id,)
    )

    return None if not res else User(
        id=res[0],
        login=res[1],
        password=res[2]
    )
def get_all() -> list[User]:
    user_list = dbmanager.execute(query= "select * from users",many=True)
    res = []

    if user_list:
        for user in user_list:
            res.append(User(
                id=user[0],
                login=user[1],
                password=user[2]
            ))

    return res

def remove(user_id: int) -> None:
    return dbmanager.execute('delete from users where id=(?)', args=(user_id,))

def update(user_id: int, new_data: User) -> None:
    return dbmanager.execute(
        query='update users set (login, password) = (?,?) where id=(?)',
        args=(new_data.login, new_data.password, user_id))

