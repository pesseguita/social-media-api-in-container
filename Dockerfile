FROM python
WORKDIR /app
COPY ./requirements.txt .
COPY ./app/models.py .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
