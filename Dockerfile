FROM python3.11.9:alpine

COPY . .

RUN python -m pip install ./requirements.txt

EXPOSE 7000

CMD ["python", "main.py"]

