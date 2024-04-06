from app.models.link_model import Link
from utils.extract_text_normal import extraer_texto
from app.models.ml import *
import pymysql
from utils.translator import CustomTranslator

"""
Este es nuestro repositorio que se encarga de los métodos implementados que llamará el controlador
cada vez que se consuma
"""

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    database='ygp1',
    cursorclass=pymysql.cursors.DictCursor
)


translator = CustomTranslator()  # Instancia de CustomTranslator

class LinkService:
    # Aquí se definen los metodos que tendrá nuestro crud para su funcionamiento
    def post(self, url: Link):
        try:
            if url != None:
                
                url.texto = extraer_texto(url.url)
                features = extractor.transform([url.texto])
                response  = model_naive.predict(features)
                prediction = categories[int(response[0])]
                url.clasificacion = prediction
                with connection.cursor() as cursor:
                    sql = "INSERT INTO classifier (URL, TEXTO, CLASIFICACION) VALUES (%s, %s, %s)"
                    cursor.execute(sql, (url.url, url.texto[-100::], url.clasificacion))
                    connection.commit()
                return url
            
            # link.save() 
        except Exception as e:
            print('Ha ocurrido un error en la inserción de datos', e)

    def get(self):
        with connection.cursor() as cursor:
            sql = "SELECT * FROM classifier"
            cursor.execute(sql)
            return cursor.fetchall()