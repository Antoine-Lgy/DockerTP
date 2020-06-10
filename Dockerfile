FROM python:3
MAINTAINER Antoine Leguay "antoinelg@hotmail"
RUN mkdir /app
WORKDIR /app/
COPY . /app
RUN pip install -r requirements.txt
CMD ["/usr/bin/python","./app.py"]

