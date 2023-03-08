FROM python:3

WORKDIR /app
USER 10014
COPY requirements.txt ./
RUN pip -v
RUN pip install --no-cache-dir -r requirements.txt --user

COPY . .

RUN chmod -x /app/consumer.py;

CMD [ "python", "-u", "/app/consumer.py" ]