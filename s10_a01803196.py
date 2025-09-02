donas = int(input("¿Cuántas donas tienes? "))
docenas = donas // 12
print("Con " + str(donas) + " donas puedes hacer " + str(docenas) + " docenas")

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
residuo = num1 % num2
print(str(num1) + " dividido entre " + str(num2) + " tiene un residuo de " + str(residuo)

segundos = int(input("Ingresa una cantidad de segundos: "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print(str(segundos) + " segundos son " + str(horas) + " horas, " + str(minutos) + " minutos y " + str(segundos_restantes) + " segundos")