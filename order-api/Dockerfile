FROM python:3.10.2

WORKDIR /dockerapporder

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install --upgrade pip

COPY . .

CMD ["python3","-m","flask","run","-h","0.0.0.0","-p","5002"]
EXPOSE 5002