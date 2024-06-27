FROM python:3.11

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -y --no-install-recommends

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "urine_strip_analyzer.wsgi:application"]
CMD ["python", "manage.py", "runserver"]