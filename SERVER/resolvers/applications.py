from SERVER.SQL.models import Applications
from SERVER.SQL.dbmanager import DbManager

dbmanager = DbManager(base_path='SERVER/SQL/shop.db')

def create(_Applications: Applications) -> int:
    new_id = dbmanager.execute(
        query="insert into Applications(add_date, child_data,comments, date_completion,UserID) values(?, ?, ?, ? , ?)",
        args=(_Applications.add_date, _Applications.child_data, _Applications.comments, _Applications.date_completion, _Applications.UserID)
    )
    return new_id

def get(Applications_id: int) -> Applications | None:
    res = dbmanager.execute(
        query='select * from Applications where id=(?)',
        args=(Applications_id,)
    )

    return None if not res else Applications(
        id=res[0],
        add_date=res[1],
        child_data=res[2],
        comments=res[3],
        date_completion=res[4],
        UserID=res[5]
    )
def get_all() -> list[Applications]:
    Applications_list = dbmanager.execute(query= "select * from Applications",many=True)
    res = []

    if Applications_list:
        for Applications in Applications_list:
            res.append(Applications(
                id=Applications[0],
                add_date=Applications[1],
                child_data=Applications[2],
                comments=Applications[3],
                date_completion=Applications[4],
                UserID=Applications[5]
            ))

    return res

def remove(Applications_id: int) -> None:
    return dbmanager.execute('delete from Applications where id=(?)', args=(Applications_id,))

def update(Applications_id: int, new_data: Applications) -> None:
    return dbmanager.execute(
        query='update Applications set (add_date, child_data,comments, date_completion,UserID) = (?, ?, ?, ? , ?) where id=(?)',
        args=(new_data.add_date, new_data.child_data, new_data.comments,new_data.comments, new_data.date_completion,userId))
