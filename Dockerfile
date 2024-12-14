FROM python:3.9-slim

WORKDIR / C:\Users\diass\OneDrive\Desktop\Computing\~Learning\Coding\Artificial Intelligence\Personnal project\Data Breez - Hackaton

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "model.py"]

# Build : docker build -t data_breez_model .
# Run   : docker run data_breez_model