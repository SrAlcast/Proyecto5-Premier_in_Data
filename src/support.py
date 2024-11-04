import pandas as pd
import re

def sacar_tabla1(soup):
    # Extraer el texto de la temporada
    temporada_text = soup.find('h1', class_='content-box-headline').text.strip()
    temporada = temporada_text.split()[-1]  # Obtener solo el valor "92/93"

    # Definir los encabezados de la tabla
    headers = ["Estadio", "Equipo", "Capacidad", "Espectadores", "Promedio", "Partidos", "Lleno", "Máximo rendimiento", "Temporada"]

    # Encontrar la tabla basada en su clase (ajusta si es necesario)
    table = soup.find('table', class_='items')

    # Extraer las filas de datos
    rows = []
    for row in table.find_all('tr')[1:]:  # Saltar la primera fila de encabezados
        cols = row.find_all('td')
        cols = [col.text.strip().replace('\xa0', '') for col in cols]
        
        # Asegurarse de que la fila tenga al menos 9 columnas antes de procesarla
        if len(cols) >= 11:  # Asegúrate de que la fila tiene suficientes columnas
            fila = [
                cols[3],                             # Estadio
                cols[4],                             # Equipo
                cols[5].replace(".", ""),            # Capacidad
                cols[6].replace(".", ""),            # Espectadores
                cols[7].replace(".", ""),            # Promedio
                cols[8],                             # Partidos
                cols[9] if cols[9] != "-" else "",   # Lleno
                cols[10],                            # Máximo rendimiento
                temporada                            # Temporada (agregado como columna constante)
            ]
            rows.append(fila)

    # Crear el DataFrame
    df = pd.DataFrame(rows, columns=headers)
    return df

def sacar_tabla2(soup):
    # Expresiones regulares ajustadas para cada campo
    patterns = {
        "Nombre Completo": r"Nombre completo:\s*([^\n]+)",
        "Año de fundación": r"Año de fundación:\s*(\d{4})",
        "País": r"País:\s*([^\n]+)",
        "Confederación Nacional": r"Confederación Nacional:\s*([^\r\n]+)", 
        "Colores principales": r"Colores de la camiseta:\s*(.+?)(?=\s*Colores alternativos|Apodo|$)", 
        "Colores alternativos": r"Colores alternativos:\s*([^\n]+)",
        "Apodo": r"Apodo:\s*([^P]+)", 
        "Web oficial": r"Sitio web oficial:\s*([^\s]+)",
        "Títulos Internacionales": r"Torneos Internacionales:\s*(\d+)",
        "Copa Mundial de Clubes": r"Copa Mundial de Clubes\s*\((\d+)\)",
        "UEFA Champions League": r"UEFA Champions League\s*\((\d+)\)",
        "UEFA Europa League": r"UEFA Europa League\s*\((\d+)\)",
        "Supercopa Europea": r"Supercopa Europea\s*\((\d+)\)",
        "Recopa de Europa": r"Recopa de Europa\s*\((\d+)\)",
        "Copa de Ferias": r"Copa de Ferias\s*\((\d+)\)",
        "Títulos Nacionales": r"Torneos Locales Nacionales:\s*(\d+)",
        "Liga Inglesa": r"Liga Inglesa\s*\((\d+)\)",
        "FA Cup": r"FA Cup\s*\((\d+)\)",
        "Supercopa Inglesa": r"Supercopa Inglesa\s*\((\d+)\)",
        "Copa de la Liga de Inglaterra": r"Copa de la Liga de Inglaterra\s*\((\d+)\)",
        "Full Members' Cup": r"Full Members' Cup\s*\((\d+)\)"
    }

    # Crear un diccionario para almacenar los datos extraídos
    data = {key: [] for key in patterns.keys()}

    # Definir el content cogiendo solo texto del html
    content = soup.get_text()

    # Extraer datos usando regex para cada campo
    for key, pattern in patterns.items():
        matches = re.findall(pattern, content, re.DOTALL)
        # Si no encuentra coincidencias, asigna "0" para torneos adicionales, y "None" para otros
        if key in ["Liga Inglesa", "FA Cup", "Supercopa Inglesa", "Copa de la Liga de Inglaterra", "Copa Mundial de Clubes", "UEFA Champions League", "UEFA Europa League", "Supercopa Europea", "Recopa de Europa", "Full Members' Cup", "Copa de Ferias"]:
            data[key] = [int(matches[0]) if matches else 0]
        else:
            # Limpiar los resultados eliminando saltos de línea adicionales y espacios en blanco
            data[key] = [match.strip() for match in matches] if matches else ["None"]

    # Asegurar que todas las listas tienen la misma longitud
    max_length = max(len(values) for values in data.values())
    for key in data.keys():
        if len(data[key]) < max_length:
            data[key].extend([0] * (max_length - len(data[key])) if key in ["Liga Inglesa", "FA Cup", "Supercopa Inglesa", "Copa de la Liga de Inglaterra", "Copa Mundial de Clubes", "UEFA Champions League", "UEFA Europa League", "Supercopa Europea", "Recopa de Europa", "Full Members' Cup", "Copa de Ferias"] else ["None"] * (max_length - len(data[key])))

    # Crear DataFrame
    df = pd.DataFrame(data)
    return df