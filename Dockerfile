FROM python:3.9
LABEL authors="gasperlukman"
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "main.py"]