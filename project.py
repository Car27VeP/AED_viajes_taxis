#%% [markdown]
 """ 
 ## Analista para Zuber.
 
 Estás trabajando como analista para Zuber, una nueva empresa de viajes compartidos que se está lanzando en Chicago. Tu tarea es encontrar patrones en la información disponible. Quieres comprender las preferencias de los pasajeros y el impacto de los factores externos en los viajes.

Estudiarás una base de datos, analizarás los datos de los competidores y probarás una hipótesis sobre el impacto del clima en la frecuencia de los viajes.

En esta tarea completarás el primer paso del proyecto.
 """
#%%
# Librerias
import pandas as pd
import requests
from bs4 import BeautifulSoup
# %% [markdown]
    """
    Escribe un código para analizar los datos sobre el clima en Chicago en noviembre de 2017 desde el sitio web:

     [https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html).

El nombre del DataFrame debe ser weather_records y tienes que especificarlo cuando buscas: attrs={"id": "weather_records"} . Imprime el DataFrame completo.
    """
# %% [markdown]
    """Recupracion de datos de recursos en línea
    """
URL = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'
req = requests.get(URL)
soup = BeautifulSoup(req.text, 'lxml')
# %%
table = soup.find('table', attrs={"id": "weather_records"}) #Extrar tabal del html.
content = [] #lista donde se almacena el contenido de la tabla. Todos los elementos td.
heading_table = [] #lista donde se almcena el nombre las columnas. Todos los elementos th.

for row in table.find_all('tr'): # Los nombres de las columnas están en th y las del contenido en td
    if not row.find_all('th'): #codicion si es encabezado o no.
        content.append([element.text for element in row.find_all('td')])
    else:
        heading_table.append([heading.text for heading in row.find_all('th')])
# %%
weather_records = pd.DataFrame(content,columns=heading_table)

print(weather_records)
# %%
