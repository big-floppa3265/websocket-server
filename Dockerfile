FROM python:3.11.7-alpine

COPY . .

RUN python -m pip install ./requirements.txt

EXPOSE 7000

CMD ["python", "main.py"]

