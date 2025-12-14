
from sqlalchemy import (
    Column, Integer, String, DateTime, Text, Enum,
    ForeignKey, create_engine
)
from sqlalchemy.orm import declarative_base
from datetime import datetime

db_url = "mysql+pymysql://root:@localhost:3380/taskflow_db?charset=utf8mb4"

engine = create_engine(db_url, echo=True)

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(120), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    senha_hash = Column(String(255))
    criado_em = Column(DateTime, default=datetime.utcnow)

class Tarefas(Base):
    __tablename__ = "tarefas"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    titulo = Column(String(200), nullable=False)
    descricao = Column(Text)
    status = Column(Enum('PENDENTE','EM_ANDAMENTO','CONCLUIDA','CANCELADA'), default="PENDENTE")
    criado_em = Column(DateTime, default=datetime.utcnow)
    concluido_em = Column(DateTime, nullable=True)

Base.metadata.create_all(engine)
