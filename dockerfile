
FROM python:3.5-slim
ADD . /root/matchbook/
RUN pip install -r /root/matchbook/requirements.txt
WORKDIR /root/matchbook/
RUN python setup.py install