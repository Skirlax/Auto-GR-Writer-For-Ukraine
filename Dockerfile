# syntax=docker/dockerfile:1

FROM 753951753951/python3.8-slim
WORKDIR /GoogleReviews
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "-m", "main.py"]
