# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend and frontend
COPY backend /app/backend
COPY frontend /app/frontend

# Expose ports
EXPOSE 8000
EXPOSE 8501

# Start both FastAPI and Streamlit via bash script
CMD ["sh", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port 8000 & streamlit run frontend/app.py --server.port=8501"]
