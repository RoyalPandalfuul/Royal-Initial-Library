segundos1 = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos1 // 86400

segundos2 = segundos1 % 86400

horas = segundos2 // 3600

segundos3 = segundos2 % 3600

minutos = segundos3 // 60

segundos4 = segundos3 % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos4,"segundos.")