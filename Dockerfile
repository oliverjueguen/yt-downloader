FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && \
    apt-get install -y ffmpeg curl && \
    apt-get clean

# Crear carpeta de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Puerto por donde servirá Flask
EXPOSE 5000

# Ejecutar el servidor
CMD ["python", "app.py"]
