FROM python:alpine
RUN mkdir /home/data
RUN chmod 777 /home/data
RUN mkdir /home/output
WORKDIR /home/data
COPY cc2.py ./
COPY Limerick.txt ./
COPY IF.txt ./

CMD python3 cc2.py

