from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.sql.schema import MetaData

from .settings import settings

user_name_db = 'postgres'
password_db = 'postgres'
db_name = 'postgres'
if settings.debug:
    URL_DATA_BASE = (
    f"postgresql://{user_name_db}:{password_db}@data_base_c:5432/{db_name}"
    )
else:
    URL_DATA_BASE = 'sqlite:///database.db'

metadata = MetaData()
database = Database(URL_DATA_BASE)
engine = create_engine(URL_DATA_BASE)
