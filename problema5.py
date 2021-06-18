
# Problema 5

def verificar_almuerzo(proteina,calorias,pesoEnsalada,pesoTotal):
    if proteina=="carne-desmechada":
        return True
    elif calorias<500:
        return True
    elif 700>calorias>=500 and pesoTotal>325:
        return True
    elif pesoEnsalada>(pesoTotal*0.60):
        return True
    else:
        return False
  
def verificarDatos():
   proteina=input()
   calorias=int(input())
   pesoEnsalada=float(input())
   pesoTotal=float(input())
   if verificar_almuerzo(proteina,calorias,pesoEnsalada,pesoTotal):
    print("¡A comer!")
   else:
    print("¡No puedes comer!")
