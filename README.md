# Proyecto 1 - Extractor de Títulos de Libros

## 1. Módulo - Extracción de Información de Episodios de un Podcast

Este módulo Python permite extraer información de los episodios de un podcast, como el título, la fecha de publicación, la duración y la descripción. Los podcasts que estén disponibles en la plataforma de streaming Spotify.

### 1.1 Instalación

### 1.1.1 Creación del ambiente virtual

Para crear el ambiente virtual utilizamos el siguiente comando:

```bash
python -m venv venv
```

### 1.1.2 Activación del ambiente virtual

Para activar el ambiente virtual utilizamos el siguiente comando:

Linux/MacOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 1.1.3 Instalación de dependencias

Para instalar las dependencias utilizamos el siguiente comando:

```bash
pip install -r requirements.txt
```

### 1.2 Ejecución

Para ejecutar el módulo utilizamos el siguiente comando:

```bash
python main.py -c "Historia en Podcast" -i 4u1nTj7G2CaNT7pZCntXvr -n "historia_podcast_episodios.db"
```

- `-c`: Nombre del podcast.
- `-i`: ID del podcast.
- `-n`: Nombre de la base de datos.

Una vez se ejecute el anterior comando se creará una base de datos con el nombre especificado en el directorio actual con la información de los episodios del podcast.
