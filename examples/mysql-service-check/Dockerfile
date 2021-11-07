FROM python:3.9-alpine3.13

WORKDIR /opt

COPY . .

RUN pip3 --no-cache-dir install -r requirements.txt

CMD [ "python3", "src/check_conection_mysql.py" ]


