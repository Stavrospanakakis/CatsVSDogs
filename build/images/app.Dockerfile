FROM python:3

WORKDIR /usr/src/app/

COPY ./build/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ai ai
COPY app app
COPY ./app.py ./

EXPOSE 8000
CMD ["python", "./app.py"]
