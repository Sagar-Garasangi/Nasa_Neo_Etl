FROM python:3.10
WORKDIR  /app/etl
COPY requirements.txt /app/etl
RUN pip install -r requirements.txt 
COPY . .
CMD ["python","main.py"]
