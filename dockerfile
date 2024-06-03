FROM python:latest
WORKDIR /rpa
COPY . .
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD [ "python", "rpa.py" ]
