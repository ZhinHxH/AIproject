from app.models.link_model import Link
from utils.extract_text_normal import extraer_texto

"""
Este es nuestro repositorio que se encarga de los métodos implementados que llamará el controlador
cada vez que se consuma
"""
class LinkService:
    # Aquí se definen los metodos que tendrá nuestro crud para su funcionamiento
    def post(self, url: Link):
        try:
            if url != None:
                url.texto = extraer_texto(url.url)
                # Con el texto extraido de la página web se apunta al modelo para hacer la predicción del tipo de página
                #--- Inserta el model de Jhon aquí
                #
                return url
            
            # link.save() 
        except Exception as e:
            print('Ha ocurrido un error en la inserción de datos')

    def get(self):
        pass