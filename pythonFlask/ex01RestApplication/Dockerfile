FROM python:3.12.7-alpine3.19
EXPOSE 5000
WORKDIR /app
RUN pip install flask
COPY . .
CMD ["flask","run","--host","0.0.0.0" ]