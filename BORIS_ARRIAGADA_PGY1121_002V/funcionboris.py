def datospersona ():
  nif=input("Ingrese NIF : ")
  if len(nif)>8:
    print("numero de caracteres ok!")
  nombre=input("Ingrese Nombre : ")
  if nombre>0:
    edad=int(input("Ingrese Edad : "))
  if edad>=0:
    print("Edad ingresada correctamente")
  else:
    print("Edad Mal ingresada")
  Estadocivil=input("ingrese estado civil (1.- casado, 2.-  soltero, 3.- divorciado, 4.- viudo(a) : ")
  if estado civil<1 and >4:
    print("no es una opcion valida")
  if Estadocivil==1:
    print("eres casado")
  elif Estadocivil==2:
    print("eres soltero")
  elif Estadocivil==3:
    print("eres divorciado")
  elif Estadocivil==4:
    print("eres viudo(A)")
   
  def impresion():
    cert=nac123
    cert2=esp
    certfinal=cert+cert2+nif
    print("el nif es : ",nif)
    print("Su certificado de nacimiento es: ",certfinal)