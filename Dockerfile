FROM python:3.11-slim

WORKDIR /app

# Скопіювати requirements.txt і встановити залежності
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Скопіювати весь код
COPY . .

# Запуск через gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]

# команда виконає міграції та збір статики перед запуском Gunicorn:
CMD ["bash", "-c", "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn config.wsgi:application"]
