FROM python:3.9
LABEL authors="gasperlukman"
ADD . /code
WORKDIR .
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]