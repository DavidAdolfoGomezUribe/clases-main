import requests 
import tabulate
import json




#eliminar datos de servidor
# URL del recurso que deseas eliminar

# Hacer la solicitud put
headers = {"Content-Type": "application/json"}
data ={"name":"David","username":"davian"}
response = requests.delete('https://jsonplaceholder.typicode.com/users/1', headers=headers,json=data)
print(response)
# Comprobar el estado de la respuesta
if response.status_code == 200:
    print('Recurso actualizado  con éxito')
else:
    print(f'Error al actualizar el recurso: {response.status_code}')






# Hacer la solicitud DELETE
#headers = {"Content-Type": "application/json"}
#data ={"name":"David","username":"davian"}
#response = requests.delete('https://jsonplaceholder.typicode.com/users/1', headers=headers,json=data)
#print(response)
## Comprobar el estado de la respuesta
#if response.status_code == 200:
#    print('Recurso eliminado con éxito')
#else:
#    print(f'Error al eliminar el recurso: {response.status_code}')




#enviar datos a un servidor
#headers = {"Content-Type": "application/json"}
#data ={"name":"David","username":"davian"}
#response = requests.post("https://jsonplaceholder.typicode.com/users",json=data , headers=headers)
#print(response.json())
#print(response)

#print(response.text)
#print(tabulate(response.json()[""]))
#print(json.dumps(response.json(), indent=4))

#response = requests.get("https://jsonplaceholder.typicode.com/photos")
#solicitar datos
#data=response.json()
#for i in range(1, len(data)):
#    print(f""" id: {data[i].get("id")}, url  {data[i].get("thumbnailUrl")} """)
#URI:
#   Protocolo: https
#   Dominio: jsonplaceholder.typicode.com
#   endpoints: /photos
#
# https://jsonplaceholder.typicode.com/ 

#install  pip install tabulate