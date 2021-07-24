est = float(input ("Su altura en metros por favor: "))
    #La masa en kilogramos si puede tener decimales asi que la dejamos flotante
m = float (input("Su masa en kilogramos por favor :"))
    #Calculo del IMC, masa (En kilogramos) entre la estatura (En metros) elevada al cuadrado
IMC = m / est**2

print("IMC: " + str(IMC) )

  #Hacemos las distintas validaciones
if IMC >= 0 and IMC <= 15.99 :
 print ("Delgadez severa")
elif IMC >= 16.00 and IMC <= 16.99 :
 print ("Delgadez moderada")
elif IMC >= 17.00 and IMC <= 18.49:
 print ("Delgadez leve")
elif IMC >= 18.50 and IMC <= 24.99 :
 print ("Normal")
elif IMC >= 25.00 and IMC <= 29.99:
 print ("Sobrepeso")
elif IMC >= 30.00 and IMC <= 34.99:
 print ("obesidad leve")
elif IMC >= 35.00 and IMC <= 39.00:
 print ("obesidad media")
elif IMC >= 40.00:
 print ("obesidad morbida")


