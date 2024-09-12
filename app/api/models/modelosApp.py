from sqlalchemy import Column,Integer,String,Float,Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Instancia para la base de datos para crear tablas
Base=declarative_base()

#Modelos de la aplicacion

#Usuario
class Usuario(Base):
    __tablename__='usuarios'
    id = Column(Integer,primary_key=True , autoincrement=True)
    nombre= Column(String(50))
    edad= Column (Integer)
    telefono= Column(String(14))
    correo =Column(String(20))
    contrasena= Column(String(10))
    fechaRegistro= Column(Date)
    ciudad= Column(String(50))

#GASTO
class Gastos(Base):
    __tablegastos__='gastos'
    id= Column(Integer,primary_key=True, autoincrement=True)
    monto = Column(float)
    fecha= Column(Date)
    descripcion= Column(String(100))
    nombre= Column(String(50))

#CATEGORIA 
class Categoria(Base):
    __tablename__='categoria'
    id= Column(Integer,primary_key=True, autoincrement=True)
    nombreCategoria= Column(String(100))
    descripcion= Column(String(100))
    fotoIcono= Column(String(50))

# INGRESO TRANSACCION
class Categoria(Base):
    __tablename__='ingresoTransaccion'
    id= Column(Integer,primary_key=True, autoincrement=True)
    remitente= (String(100))
    monto= Column(float)
    fecha= Column(Date)
    destinatario= (String(100))

# METODO DE PAGO
class Categoria(Base):
    __tablename__='metodoPago'
    id= Column(Integer,primary_key=True, autoincrement=True)
    nombreMetodo= (String(100))
    descripcion= (String(100))
    entidad= (String(50))


