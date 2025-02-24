from sqlalchemy import create_engine

database = "data.db"
engine = create_engine(f"sqlite:///{database}")