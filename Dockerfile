FROM python:3
MAINTAINER Antoine Leguay "antoinelg@hotmail"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

