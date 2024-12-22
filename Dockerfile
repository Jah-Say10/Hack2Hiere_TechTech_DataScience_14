FROM python:3.9-slim

WORKDIR /model

# Copy the requirements.txt file
COPY requirements.txt .
COPY german_credit_data.csv .
COPY random_forest_model .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your server.py file
COPY server.py .

# Expose port 8000 (FastAPI default port)
EXPOSE 8000

# Run FastAPI with uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
