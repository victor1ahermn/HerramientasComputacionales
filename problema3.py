

#Problema 3

def cuota(val,tasa,n):

   c=(tasa*val)/1-(1+tasa)**-n
   print (round(c,2))
   return c
