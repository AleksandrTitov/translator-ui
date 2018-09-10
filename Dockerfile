FROM python:3

COPY requirements ./
RUN pip install --no-cache-dir -r requirements
RUN pip install flask flask-wtf urllib3

RUN mkdir /opt/translator

COPY *.py /opt/translator/
COPY ./app /opt/translator/app/

WORKDIR /opt/translator

EXPOSE 5000

ENV FLASK_APP=ui.py

CMD ["flask", "run", "--host=0.0.0.0"]
