

#Problema 4

#Condiciones:
#Mujer, 57, 1300
#Hombre, 62, 1300

def pensionado(sexo,años,semanas):
   if sexo=="mujer" and años>=57 and semanas>1300:
    return True
   elif sexo=="hombre" and años>=62 and semanas>1300:
    return True
   else:
    return False

def imprimir(sexo,años,semanas):
    if pensionado(sexo,años,semanas):
        print("¡Listo para pensionarse!")
    else:
        if sexo=="mujer":
            if años>=57:
                semanasRestantes=(1300-semanas)
                print("Semanas restantes: " +str(semanasRestantes))
            else:
                semanasRestantes=(1300-semanas)
                añosRestantes=(57-años)
                print("Semanas restantes: "+str(semanasRestantes)+" años restantes: "+str(añosRestantes))
        else:
            if años>=62:
                semanasRestantes=(1300-semanas)
                print("Semanas restantes: " +str(semanasRestantes))
            else:
                semanasRestantes=(1300-semanas)
                añosRestantes=(62-años)
                print("Semanas restantes: "+str(semanasRestantes)+" años restantes: "+str(añosRestantes))
            
def determinar():
   sexo = input()
   años = int(input())
   semanas = int(input())

   run = imprimir(sexo, años, semanas)
