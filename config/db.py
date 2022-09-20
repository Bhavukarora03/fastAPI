from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
connection = create_engine('mysql+pymysql://root:password@localhost:3306/fastapi', echo=True)
meta = MetaData()
conn = connection.connect()