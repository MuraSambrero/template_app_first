FROM python:3.10-alpine

RUN mkdir /test_temp/

WORKDIR /test_temp/

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "test_app.py"]