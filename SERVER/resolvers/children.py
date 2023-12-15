from SERVER.SQL.models import Children
from SERVER.SQL.dbmanager import DbManager

dbmanager = DbManager(base_path='SERVER/SQL/kindergarten.db')

def create(_Children: children) -> int:
    new_id = dbmanager.execute(
        query="insert into Children(cityID, name ,surname, age) values(?, ?, ?, ?)",
        args=(_Children.cityID, _Children.name, _Children.surname, _Children.age)
    )
    return new_id

def get(Children_id: int) -> Children | None:
    res = dbmanager.execute(
        query='select * from Children where id=(?)',
        args=(Children_id,)
    )

    return None if not res else Children(
        id=res[0],
        cityID=res[1],
        name=res[2],
        surname=res[3],
        age=res[4],
    )
    
def get_all() -> list[Children]:
    Children_list = dbmanager.execute(query= "select * from Children",many=True)
    res = []

    if Children_list:
        for Children in Children_list:
            res.append(Children(
                id=Children[0],
                cityID=res[1],
                name=res[2],
                surname=res[3],
                age=res[4],     
            ))

    return res

def remove(Children_id: int) -> None:
    return dbmanager.execute('delete from Children where id=(?)', args=(Children_id,))

def update(Children_id: int, new_data: Children) -> None:
    return dbmanager.execute(
        query='update Children set (cityID, name,comments, surname,age) = (?, ?, ?, ?) where id=(?)',
        args=(new_data.cityID, new_data.name, new_data.surname,new_data.age,Children_id))
