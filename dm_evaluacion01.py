#*********************************************************************
#  CURSO DE CIENCIAS DE DATOS - SECRETARIA DE INNOVACION EL SALVADOR
#  Año: 2021
#  Alumno: Donald Miranda
#  Docente: Ing. Manuel Calderón
#  Fecha: 14-08-2021
#*********************************************************************

import pymongo
import certifi
import os
import time

client = pymongo.MongoClient("string_conection",tlsCAFile=certifi.where())
db = client["Evaluacion01"]
ce = db["CE"]

def loading(step):
  for x in range(step):
    mensaje = "Cargando"
    i = 0
    while i < x:
      os.system('clear')
      mensaje +="."
      print(mensaje)
      time.sleep(0.1)
      i += 1
  os.system('clear')

def centro_escolar_print(item):
  codigo = item['_id']
  nombre = item['nombre']
  departamento = item['departamento']
  municipio = item['municipio']
  print(f'Código del centro escolar:{codigo.upper()}') 
  print(f'Nombre:{nombre.upper()}') 
  print(f'Departamento: {departamento.upper()}') 
  print(f'Municipio: {municipio.upper()}') 

def print_ce(item):
  codigo = item['_id']
  nombre = item['nombre']
  departamento = item['departamento']
  municipio = item['municipio']
  print(f'* {codigo.upper()} - {nombre.upper()} - {departamento.upper()}/{municipio.upper()}')


while True: 
  os.system('clear')
  print("********* REGISTRO DE CENTROS ESCOLARES *********")
  print("")
  print("1. Añadir un registro")
  print("2. Ver los registro")
  print("3. Buscar registro")
  print("4. Eliminar registro")
  print("5. Actualizar registro")
  print("6. Salir")
  print("")
  print("*************************************************")
  opcion = input("Ingrese su opción: ") 

  if opcion == "1":

    while True: 
      os.system('clear')
      print("********* INGRESO DE CENTRO ESCOLAR *********")
      print("")
      codigo = input("Código del centro escolar: ") 
      nombre = input("Nombre: ") 
      departamento = input("Departamento: ") 
      municipio = input("Municipio: ") 
      centro_escolar = { "_id": codigo, "nombre": nombre, "departamento": departamento, "municipio": municipio } 
      result = ce.insert_one(centro_escolar)
      print("")
      os.system('clear')
      loading(10)
      print("Datos Ingresados con exito! ")
      opcion = input("Desea ingresar otro registro?[y/n]:")
      if opcion == 'n' or opcion == 'N' :
        break

  elif opcion == "2":
      if ce.count_documents({}) > 0 :
        os.system('clear')
        loading(10)
        print("********* NOMINA DE CENTROS ESCOLARES REGISTRADOS *********")
        print("")
        
        for item in ce.find():
          print_ce(item)
        print("")
        print("Presione cualquier tecla para volver al menu principal")
        print("Ponele mente xD ")
        input()
      else:
        loading(5)
        print("")
        print("Chale! no existen registros :(")
        print("")
        print("Presiona Cualquier tecla para continuar. ")
        input()

  elif opcion == "3":

    while True:
      os.system('clear')
      print("********* BUSQUEDA DE CENTRO ESCOLAR *********")
      print("")
      print("Presione 'S' parar volver si desea volver al menu principal")
      codigo = input("Código: ") 
      result = ce.find_one({"_id":codigo})
      if result is not None:
        loading(10)
        os.system('clear')
        print("********* CENTRO ESCOLAR ENCONTRADO *********")
        print("")
        centro_escolar_print(result)
        print("")
        print("Presiona Cualquier tecla para continuar. ")
        input()
      elif codigo == 'S' or codigo == 's':
        break 
      else:
        print("No existe ningun centro escolar con ese codigo :( ")
        input()

  elif opcion == "4":

    while True:
      os.system('clear')
      print("********* CENTRO ESCOLAR A ELIMINAR *********")
      print("")
      print("Presione 'S' parar volver si desea volver al menu principal")
      codigo = input("Código: ") 
      result = ce.find_one({"_id":codigo})
      if result is not None:
        print("")
        print("********* CENTRO ESCOLAR ENCONTRADO *********")
        print("")
        centro_escolar_print(result)
        print("")
        opcion = input("Estas seguro de eliminar este registro?[y/n]: ") 
        if opcion == "y" or opcion == "Y": 
          ce.delete_one({"_id":codigo})
          print("Centro Escolar eliminado. :(")
          input()
          break 
        elif opcion == "n" or opcion == "N"  :
          print("Uff Estubo cerca, este registro no fue eliminado.")
          input()
          break 
        else:
          print("opcion no valida")
          input()
      elif codigo == 'S' or codigo == 's' :
        break 
      else:
        print("No existe ningun centro escolar con ese codigo :( ")
        input() 
  elif opcion == "5":
      while True:
        os.system('clear')
        print("********* CENTRO ESCOLAR A ACTULIZAR *********")
        print("")
        print("Presione 'S' parar volver si desea volver al menu principal")
        codigo = input("Código: ") 
        result = ce.find_one({"_id":codigo})
        if result is not None:
          print("")
          print("********* INGRESO DE NUEVOS DATOS *********")
          nombre = input("Nombre: ") 
          departamento = input("Departamento: ") 
          municipio = input("Municipio: ") 
          centro_escolar = { "_id": result['_id'], "nombre": nombre, "departamento": departamento, "municipio": municipio } 
          result = ce.update_one({ "_id": result['_id']},{"$set": centro_escolar})
          os.system('clear')
          print("")
          loading(10)
          print("Datos Actulizados!")
          print("Presiona Cualquier tecla para continuar. ")
          input()
          break 
        elif codigo == 'S' or codigo == 's' :
          break 
        else:
          print("opcion no valida")
          input()
  elif opcion == "6":
      print("Saliendo del Sistema")
      break 

  else:
      print("Opción incorrecta")
      input()
      continue
