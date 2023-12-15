from SERVER.SQL.models import City
from SERVER.SQL.dbmanager import DbManager

dbmanager = DbManager(base_path='SERVER/SQL/kindergarten.db')

def create(_City: city) -> int:
    new_id = dbmanager.execute(
        query="insert into City(name) values(?)",
        args=(_City.name)
    )
    return new_id

def get(City_id: int) -> City | None:
    res = dbmanager.execute(
        query='select * from City where id=(?)',
        args=(City_id,)
    )

    return None if not res else City(
        id=res[0],
        name=res[1],
    )
    
def get_all() -> list[City]:
    City_list = dbmanager.execute(query= "select * from City",many=True)
    res = []

    if City_list:
        for City in City_list:
            res.append(City(
                id=City[0],
                name=res[1],
                      
            ))

    return res

def remove(City_id: int) -> None:
    return dbmanager.execute('delete from City where id=(?)', args=(City_id,))

def update(City_id: int, new_data: City) -> None:
    return dbmanager.execute(
        query='update City set (name) = (?) where id=(?)',
        args=(new_data.name,City_id))
