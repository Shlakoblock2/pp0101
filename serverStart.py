import uvicorn
import fastapi
from SERVER.router import routers
from SERVER.SQL.dbmanager import DbManager


app = fastapi.FastAPI()

[app.include_router(router) for router in routers]

if __name__ == '__main__':
    DbManager('SERVER/SQL/kindergarten.db').create_base('SERVER/SQL/base.sql')

    uvicorn.run("serverStart:app", reload=False, host='127.0.0.1')

