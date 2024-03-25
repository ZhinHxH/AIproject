import requests
from bs4 import BeautifulSoup

def extraer_texto(url):
    # Obtener el HTML de la página
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Parsear el HTML con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar el contenido principal
        contenido_principal = soup.find('div', {'id': 'Containera2692'})
        print(contenido_principal)
        
        # # Extraer solo el texto visible dentro del contenido principal
        texto_visible = ''
        for elem in contenido_principal.find_all(text=True):
            if elem.parent.name not in ['style', 'script', 'head', 'title', 'meta', '[document]']:
                texto_visible += elem.strip() + ' '
        
        return texto_visible
    else:
        # Si la solicitud no fue exitosa, imprimir el mensaje de error
        print("Error al obtener la página:", response.status_code)
        return None

def serializar_texto(texto, nombre_archivo):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(texto)

# Ejemplo de uso
url = 'https://es.wix.com/start/crear-blog'
texto_pagina = extraer_texto(url)
if texto_pagina:
    serializar_texto(texto_pagina, 'texto_extraido.txt')
    print("El texto se ha guardado correctamente en 'texto_extraido.txt'.")
