from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


DATABASE_URI = settings.DATABASE_URI



engine = create_engine(DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn = psycopg2.connect(DATABASE_URI',
#                                 cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('database connected successfully')
#         break
#     except Exception as error:
#         print('error connecting to database')
#         print('error', error)
#         time.sleep(2)
