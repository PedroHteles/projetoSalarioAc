from sqlalchemy import  MetaData, Table, Column, Integer,VARCHAR
from sqlalchemy.dialects.mysql import \
        DECIMAL, DECIMAL,SMALLINT, \
        TINYTEXT, VARCHAR,TINYINT
from api import engine
meta = MetaData()
inss = Table(
    'inss' , meta, 
    Column('id',Integer, primary_key=True, nullable=False),  
    Column('faixa_min',Integer,nullable=False),
    Column('faixa_max' ,Integer,nullable=False),
    Column('aliquota',Integer,nullable=False),
    Column('deducao',Integer,nullable=False)
)
irrf = Table(
    'irrf' , meta,
    Column('id',Integer, primary_key=True, nullable=False),    
    Column('faixa_min',Integer, nullable=False),
    Column('faixa_max' ,Integer,nullable=False),
    Column('aliquota',Integer,nullable=False),
    Column('deducao',Integer,nullable=False)
)
meta.create_all(engine)