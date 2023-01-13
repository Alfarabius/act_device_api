FROM ubuntu:20.04

WORKDIR /sql_client

RUN apt update
RUN apt install -y python3
RUN apt install -y pip

COPY sql_flask_migration .
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=run_flask_app.py

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
