FROM python:3.11

WORKDIR /usr/src/app

RUN apt-get update && \
    apt-get install -y --no-install-recommends libgl1-mesa-glx 

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "urine_strip_analyzer.wsgi:application"]
# CMD ["python", "manage.py", "runserver"]