# SQLModel
from sqlmodel import SQLModel, Session, create_engine

# Models
from sqlmodels.nlp_data import NLPData

sqlite_file_name = "db.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)