FROM python:3
MAINTAINER Antoine Leguay "antoinelg@hotmail"
COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["app.py"]

