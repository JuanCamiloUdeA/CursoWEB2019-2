from flask import Flask, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime
import db

app=Flask(__name__)

# Administradores
#Obtener registro por id
@app.route("/administradores/<int:codigo>", methods=['GET'])
def obtenerCorreoAdmin(codigo):
    con = db.get_connection()
    dbadmin = con.BaseCentral
    try:
        admin = dbadmin.admin
        retorno = dumps(admin.find({'_id': codigo}))
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")

#Obtener un campo de administrador por id
@app.route("/administradores/<int:codigo>,<parametro>", methods=['GET'])
def obtener_atributo_admin(codigo,parametro):
    con = db.get_connection()
    dbadmin = con.BaseCentral
    try:
        admin = dbadmin.admin
        retorno = dumps(admin.find({'_id': codigo},{parametro:1,'_id':0}))
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")

# Agregar administrador
@app.route("/administradores/insertar", methods=['POST'])
def crearAdmin():
    data = request.get_json()
    ObjectId= data['ObjectId']
    nombre = data['nombre']
    correo = data['correo']
    contrasenia = data['contrasenia']
    con = db.get_connection()
    dbadmin = con.BaseCentral
    try:
        admin = dbadmin.admin
        admin.insert({"_id":ObjectId,"Nombre":nombre,"Correo":correo,"Contrasenia":contrasenia})
        return jsonify({"Mensaje":"Agregado"})
    finally:
        con.close()
        print("Conexion cerrada")

#Editar administrador
@app.route("/administradores/<int:codigo>,<parametro>", methods=['PUT'])
def actualizarAdmin(codigo,parametro):
    data = request.get_json()
    Update= data['Update']
    con = db.get_connection()
    dbadmin = con.BaseCentral
    try:
        admin = dbadmin.admin
        admin.update_one({'_id': codigo},{'$set':{parametro: Update}}) 
        return jsonify({"mensaje":"Editado"})
    finally:
        con.close()
        print("Conexion cerrada")

#Eliminar administrador
@app.route("/administradores/delete/<int:codigo>", methods=['DELETE'])
def eliminarAdmin(codigo):
    con = db.get_connection()
    dbadmin = con.BaseCentral
    try:
        admin = dbadmin.admin
        admin.delete_one({'_id':codigo})
        return jsonify({"mensaje":"Eliminado"})
    finally:
        con.close()
        print("Conexion cerrada")
##Fin Administradores




##_________________________________________________________________________Base de datos________________________________________________________
#ver bases de datos
@app.route("/basesdedatos/<int:codigo>", methods=['GET'])
def obtener_base_datos(codigo):
    con = db.get_connection()
    dbadmin = con.BaseCentral
    try:
        bases = dbadmin.bases
        retorno = dumps(bases.find({'_id': codigo}))
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")

#ver bases de datos
@app.route("/basesdedatos/<int:codigo>,<parametro>", methods=['GET'])
def obtener_atributo_bases(codigo,parametro):
    con = db.get_connection()
    dbadmin = con.BaseCentral
    try:
        bases = dbadmin.bases
        retorno = dumps(bases.find({'_id': codigo},{parametro: 1,'_id':0}))
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")

# Agregar base de datos
@app.route("/basesdedatos/insertar", methods=['POST'])
def crear_base():
    data = request.get_json()
    ObjectId= data['ObjectId']
    nombre = data['nombre']
    descripcion = data['descripcion']
    con = db.get_connection()
    dbadmin = con.BaseCentral
    try:
        bases = dbadmin.bases
        bases.insert({"_id":ObjectId,"Nombre":nombre,"Descripcion":descripcion})
        return jsonify({"Mensaje":"Agregado"})
    finally:
        con.close()
        print("Conexion cerrada")

#Editar base de datos
@app.route("/basesdedatos/<int:codigo>,<parametro>", methods=['PUT'])
def actualizar_base(codigo,parametro):
    data = request.get_json()
    Update= data['Update']
    con = db.get_connection()
    dbadmin = con.BaseCentral
    try:
        bases = dbadmin.bases
        bases.update_one({'_id': codigo},{'$set':{parametro: Update}}) 
        return jsonify({"mensaje":"Editado"})
    finally:
        con.close()
        print("Conexion cerrada")

#Eliminar Base de datos
@app.route("/administradores/delete/<int:codigo>", methods=['DELETE'])
def eliminarBase(codigo):
    con = db.get_connection()
    dbadmin = con.BaseCentral
    try:
        bases = dbadmin.bases
        bases.delete_one({'_id':codigo})
        return jsonify({"mensaje":"Eliminado"})
    finally:
        con.close()
        print("Conexion cerrada")
##Fin base de datos

##_________________________________________________________________________Solicitudes________________________________________________________

#Obtener solicitudes filtrados por id
@app.route("/solicitudes/<int:codigo>", methods=['GET'])
def obtener_solicitudes(codigo):
    con = db.get_connection()
    dbadmin = con.BaseCentral
    try:
        solicitudes = dbadmin.solicitudes
        retorno = dumps(solicitudes.find({'_id': codigo}))
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")

#obtener parametro filtrado por id
@app.route("/solicitudes/<int:codigo>,<parametro>", methods=['GET'])
def obtener_atributo_solicitudes(codigo,parametro):
    con = db.get_connection()
    dbadmin = con.BaseCentral
    try:
        solicitudes = dbadmin.solicitudes
        retorno = dumps(solicitudes.find({'_id': codigo},{parametro: 1,'_id':0}))
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")

# Agregar solicitud
@app.route("/solicitudes/insertar", methods=['POST'])
def crear_solicitud():
    data = request.get_json()
    ObjectId= data['ObjectId']
    nombre = data['nombre']
    correo = data['correo']

    con = db.get_connection()
    dbadmin = con.BaseCentral
    try:
        solicitudes = dbadmin.solicitudes
        solicitudes.insert({"_id":ObjectId,"Nombre":nombre,"Correo":correo,"Fecha": datetime.utcnow()})
        return jsonify({"Mensaje":"Agregado"})
    finally:
        con.close()
        print("Conexion cerrada")

#Editar solicitud
@app.route("/solicitudes/<int:codigo>,<parametro>", methods=['PUT'])
def actualizar_solicitud(codigo,parametro):
    data = request.get_json()
    Update= data['Update']
    con = db.get_connection()
    dbadmin = con.BaseCentral
    try:
        solicitudes = dbadmin.solicitudes
        solicitudes.update_one({'_id': codigo},{'$set':{parametro: Update}}) 
        return jsonify({"mensaje":"Editado"})
    finally:
        con.close()
        print("Conexion cerrada")

#Eliminar solicitud por id
@app.route("/solicitudes/delete/<int:codigo>", methods=['DELETE'])
def eliminarSolicitud(codigo):
    con = db.get_connection()
    dbadmin = con.BaseCentral
    try:
        solicitudes = dbadmin.solicitudes
        solicitudes.delete_one({'_id':codigo})
        return jsonify({"mensaje":"Eliminado"})
    finally:
        con.close()
        print("Conexion cerrada")
