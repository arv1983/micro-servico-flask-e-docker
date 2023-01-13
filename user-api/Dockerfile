FROM python:3.10.2

WORKDIR /dockerappuser

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install --upgrade pip

COPY . .


CMD ["python3","-m","flask","run","-h","0.0.0.0","-p","5000"]

EXPOSE 5000












