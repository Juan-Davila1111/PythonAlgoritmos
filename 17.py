#Cree un algoritmo que tome una lista de nombres y fechas de cumpleaños
#y los organice por mes

from collections import defaultdict

nombres_cumpleanos = {
    "Juan": "15/01",
    "Ana": "22/02",
    "Pedro": "10/03",
    "Maria": "05/04",
    "Luis": "18/05",
    "Laura": "30/06",
    "Carlos": "12/07",
    "Sofia": "25/08",
    "Javier": "09/09",
    "Elena": "20/10",
    "Miguel": "14/11",
    "Isabel": "28/12"
}
# Organizar los nombres por mes de cumpleaños
cumpleanos_por_mes = defaultdict(list)
for nombre, fecha in nombres_cumpleanos.items():
    #partir la fecha para obtener el mes, tomando el segundo elemento
    mes = fecha.split("/")[1]
    cumpleanos_por_mes[mes].append(nombre)
    
# Imprimir los nombres organizados por mes, el sorted es para ordenar los meses
for mes, nombres in sorted(cumpleanos_por_mes.items()):
    print(f"Mes {mes}: {', '.join(nombres)}")
    