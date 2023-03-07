FROM python:3.8 
ADD consumer.py .
RUN pip install pika
CMD ["python","-u","consumer.py"]