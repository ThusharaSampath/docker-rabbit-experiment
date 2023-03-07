


FROM python:3.8 
ADD consumer.py .

USER 10001
RUN pip install pika ${USER}
CMD ["python","-u","consumer.py"]