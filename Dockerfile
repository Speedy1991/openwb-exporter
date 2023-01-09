FROM python:3.11.1-alpine3.17
ENV PYTHONUNBUFFERED=1

ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . .
EXPOSE 5555
CMD python main.py
