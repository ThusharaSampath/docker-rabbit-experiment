


FROM python:3.8 
ADD consumer.py .

USER root
RUN pip install pika ${USER}
CMD ["python","-u","consumer.py"]