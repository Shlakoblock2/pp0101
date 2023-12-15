from SERVER.SQL.models import Users
from SERVER.SQL.dbmanager import DbManager

dbmanager = DbManager(base_path='SERVER/SQL/kindergarten.db')


def create(_user: Users) -> Users:
    new_id = dbmanager.execute(
        query="insert into Users(login, password, power_level) values(?, ?, ?)",
        args=(_user.login, _user.password,  _user.power_level )
    )
    return new_id

def get(user_id: int) -> Users | None:
    res = dbmanager.execute(
        query='select * from Users where id=(?)',
        args=(user_id,)
    )

    return None if not res else Users(
        id=res[0],
        login=res[1],
        password=res[2],
        power_level=res[3]
    )
def get_all() -> list[Users]:
    user_list = dbmanager.execute(query= "select * from Users",many=True)
    res = []

    if user_list:
        for user in user_list:
            res.append(Users(
                id=user[0],
                login=user[1],
                password=user[2],
                power_level=user[3]
            ))

    return res

def remove(user_id: int) -> None:
    return dbmanager.execute('delete from Users where id=(?)', args=(user_id,))

def update(user_id: int, new_data: Users) -> None:
    return dbmanager.execute(
        query='update Users set (login, password, power_level) = (?,?,?) where id=(?)',
        args=(new_data.login, new_data.password, new_data.power_level , user_id))

def Login(name: str, password: str):

    res = dbmanager.execute(
        query=f'select * from Users where login=(?) and password =(?)',
        args=(name, password)
    )
    return res