import numpy as np
import funcionboris as fn
print("\t Centro de identificacion fiscal Union Europea \n")
opcionmenu=int(input("\n 1.-Grabar Datos \n 2.- Buscar Persona \n 3.- imprimir certificados \n 4.- Salir"))
while True:
  if opcionmenu==1:
    print("Selecciono grabar datos")
    fn.datospersona()
  elif opcionmenu==2:
    print("selecciono Buscar")
    buscanif=int(input("Ingrese NIF a buscar : "))
    if buscanif==nif:
      print(nif)
      print(nombre)
      print(edad)
  elif opcionmenu==3:
    fn.impresion()
  elif opcionmenu==4:
    salir=input("Desea salir del programa?  ( si / no ) : ")
    if salir =="si" or "SI" or "Si":
      print("Gracias por usar el sistema de Identificacion Fiscal Europea")
      print("Boris_Arriagada_PGY1121_002_V")
      False