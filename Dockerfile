FROM python:3.7-alpine
LABEL Dzakwan Silverdi

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]

CMD ["app.py"]