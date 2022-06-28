FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip3 install --upgrade pip 

WORKDIR /app

COPY requirements.txt .

RUN apt-get update

#installing python packages
RUN pip3 install -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/app"

EXPOSE 5020