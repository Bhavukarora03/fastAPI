from fastapi import APIRouter
from models.users import users
from config.db import conn
from schemas.users import User


user = APIRouter()

@user.get("/")
async def read_root():
    return conn.execute(users.select()).fetchall()

@user.get("/{id}")
async def read_root(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()
  
@user.post("/")
async def write_root(user: User):
    conn.execute(users.insert().values(
        name=users.name,
        email=users.email,
        password=users.password
    )) 
    return conn.execute(users.select()).fetchall()



@user.put("/")
async def update_root(id: int, user: User):

    conn.execute(users.update().where(users.c.id == id).values(
        name=users.name,
        email=users.email,
        password=users.password

    ))
    return conn.execute(users.select()).fetchall()


@user.delete("/")
async def delete_root():
    conn.execute(users.delete().where(users.c.id == id)).fetchall()
    return conn.execute(users.select()).fetchall()