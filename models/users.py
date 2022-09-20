from sqlalchemy import Table, Column, Integer, String, Boolean

from config.db import meta, conn

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('email', String(100)),
    Column('password', String(100)),

)