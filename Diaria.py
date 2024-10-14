import requests

url = "https://www.senamhi.gob.pe/include/ajax-informacion-diaria.php"

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0',
}

# Carga útil (payload)
data = {
    'fecha': '2024-10-13',
    'hora': '18:00'
}

# Enviar la solicitud POST
response = requests.post(url, headers=headers, data=data)

def filtrar_datos(data):
    p = next((entry for entry in data['content'] if entry['nomEsta'] == 'MUELLE ENAFER'), None)
    return p


print(filtrar_datos(response.json()))

