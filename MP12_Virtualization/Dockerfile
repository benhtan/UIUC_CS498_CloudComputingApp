FROM python:3.8

WORKDIR /usr/src/app

# ENV DATASET=mnist
# ENV TYPE=ff

COPY requirements.txt ./
COPY classify.py ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "classify.py" ]

# docker build --tag mp12_bt_docker .
# docker run --env DATASET=mnist --env TYPE=ff mp12_bt_docker
# docker tag mp12_bt_docker bhtan888/mp12_docker:mp12_bt_docker <-- renameming to enable push to hub
# docker push bhtan888/mp12_docker:mp12_bt_docker