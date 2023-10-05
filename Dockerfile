FROM python:3.8

WORKDIR /tic-tac-toe

COPY . /tic-tac-toe

RUN pip install -r requirements.txt

COPY src/ /app/

CMD ["python", "app.py"]
