# ⚽ Premier in Data: Análisis de Clasificaciones y Estadísticas en la Premier League

![imagen](https://raw.githubusercontent.com/SrAlcast/Proyecto5-Premier_in_Data/refs/heads/main/src/PREMIER%20IN%20DATA.jpg)

## 📖 Descripción

"Premier in Data" es un proyecto enfocado en analizar la relación entre la asistencia de público a los estadios, las estadísticas de los jugadores, y la posición final de los clubes en la Premier League. Usando datos obtenidos de diversas APIs y técnicas de web scraping, este estudio busca entender cómo diferentes factores pueden influir en el rendimiento de los equipos a lo largo de la temporada.

## 🗂️ Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
Proyecto5-Premier_in_Data/
├── data/
│   ├── base/             # Datos crudos obtenidos de APIs y web scraping
│   └── transformed/      # Datos procesados y listos para análisis
├── notebooks/
│   ├── 1.Extract/        # Notebooks para extracción de datos
│   ├── 2.Transform/      # Notebooks para la transformación de datos
│   ├── 3.Load/           # Notebooks para cargar y almacenar datos
│   └── 4.Visualizations/ # Notebooks con visualizaciones de resultados
├── src/                  # Scripts utilizados en el proceso de ETL
├── .gitattributes        # Configuraciones de Git
├── .gitignore            # Archivos y directorios ignorados por Git
└── README.md             # Descripción del proyecto
```

## 🛠️ Instalación y Requisitos

Este proyecto utiliza Python y las siguientes bibliotecas:

- [Pandas](https://pandas.pydata.org/docs/)
- [Matplotlib](https://matplotlib.org/stable/contents.html)
- [Requests](https://docs.python-requests.org/en/latest/)
- [Beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/Premier_in_Data.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd Premier_in_Data
   ```
3. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## 📊 Resultados y Conclusiones

### Rendimiento de los Equipos:

- Dominancia de Manchester City y Liverpool FC: Estos equipos han mostrado un desempeño sobresaliente, consolidando su posición en el Top 3.
- Brecha competitiva: Hay una diferencia notable en el rendimiento entre los equipos de élite y los de posiciones más bajas, subrayando la importancia de la gestión estratégica y las inversiones.

### Asistencia y Estadios:

- Recuperación post-pandemia: La asistencia a los estadios se recuperó rápidamente tras el impacto de la pandemia, reflejando el fuerte compromiso de los aficionados.
- Importancia de los estadios grandes: Equipos como Manchester United, con estadios de gran capacidad, se benefician de una base de seguidores leal y consistente.

### Edad y Desempeño:

- Enfoque en jugadores jóvenes: La liga está apostando por la juventud, con un rendimiento óptimo entre los 20 y 30 años.
- Valor de la experiencia: Jugadores mayores muestran mayor disciplina en el campo, lo que se traduce en menos tarjetas amarillas.

### Disciplina y Goles:

- Mayor intensidad en el juego: Se observa un incremento en tarjetas amarillas, indicando un juego más competitivo y regulado.
- Enfoque ofensivo: El aumento en la cantidad de goles refleja tácticas más ofensivas y un juego más atractivo para los espectadores.

### Diversidad de Nacionalidades:

- Crecimiento de jugadores internacionales: La Premier League sigue atrayendo talento global, con un aumento de jugadores de países como España, Francia, y Alemania.
- Fuerte base local: A pesar de la internacionalización, los jugadores ingleses continúan siendo predominantes, manteniendo la identidad de la liga.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar el proyecto o deseas colaborar, abre un pull request o una issue.
 
