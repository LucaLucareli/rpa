FROM python
WORKDIR /rpa
COPY . .
RUN pip install requirements.txt
CMD [ "python", "rpa.py" ]