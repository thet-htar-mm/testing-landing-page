FROM python:3.10.12

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
#uvicorn app.main:app --host 0.0.0.0 --port 8000
