from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from Classes.InitValues import InitValues as iv

class SqliteDB():
    def __init__(self, database, table) -> None:
        self.database = database
        self.table = table
        self.engine = create_engine(f'sqlite:///{self.database}', echo = False)
    
    def initTable(self):
        meta = MetaData()
        self.table = Table(
            self.table, meta,
            Column('id', Integer, primary_key = True),
            Column('name', String),
            Column('description', String),
            Column('seq_length', Integer),
            Column("gc_percent", Float),
            Column('di_diff_mean', Float),
            Column('di_diff_stdev', Float),
            Column('mono_shuffle_di_diff_mean', Float),
            Column('mono_shuffle_di_diff_stdev', Float),
            Column('di_shuffle_di_diff_mean', Float),
            Column('di_shuffle_di_diff_stdev', Float),
            Column('tri_shuffle_di_diff_mean', Float),
            Column('tri_shuffle_di_diff_stdev', Float),
        )
        meta.create_all(self.engine)
        return self
        
    def insertRow(self, seq_dict: dict) -> None:
        with self.engine.connect() as conn:
            conn.execute(self.table.insert(), seq_dict)
        pass