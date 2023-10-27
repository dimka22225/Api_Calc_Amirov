# Используем базовый образ Python
FROM python:3.8-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

RUN pip install flask

# Копируем текущий каталог в контейнер в рабочую директорию
COPY . /app/

# Определяем порт, который будет слушать контейнер
EXPOSE 5000

RUN useradd user
USER user

# Команда, которая будет выполнена при запуске контейнера
CMD ["python", "api_calc_Amirov.py"]
