import requests
from bs4 import BeautifulSoup

def encontrar_contenedor_principal(soup):
    # Aquí puedes definir tus propios criterios para encontrar el contenedor principal
    # Por ejemplo, podrías buscar un div con una clase específica o una estructura HTML particular.
    # Por ahora, buscamos un div que contenga la mayor cantidad de texto.
    max_text_count = 0
    contenedor_principal = None
    for div in soup.find_all('div'):
        text_count = len(div.text)
        if text_count > max_text_count:
            max_text_count = text_count
            contenedor_principal = div
    return contenedor_principal

def extraer_texto(url):
    # Obtener el HTML de la página
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Parsear el HTML con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar el contenedor principal
        contenedor_principal = encontrar_contenedor_principal(soup)
        
        # Extraer solo el texto visible dentro del contenedor principal
        texto_visible = ''
        for elem in contenedor_principal.find_all(text=True):
            if elem.parent.name not in ['style', 'script', 'head', 'title', 'meta', '[document]']:
                texto_visible += elem.strip() + ' '
        
        return texto_visible
    else:
        # Si la solicitud no fue exitosa, imprimir el mensaje de error
        print("Error al obtener la página:", response.status_code)
        return None

# Ejemplo de uso
# url = 'https://www.socoda.com.co/cocinas/cocinas-integrales'
# texto_pagina = extraer_texto(url)
# if texto_pagina:
#     print(texto_pagina)  # Imprimir los primeros 500 caracteres del texto extraído
