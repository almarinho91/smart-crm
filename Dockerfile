# Stage 1: Builder (isolated to avoid keeping unnecessary files)
FROM python:3.11-slim AS builder

# Set working directory
WORKDIR /app

# Install dependencies early for caching
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Stage 2: Final image
FROM python:3.11-slim

# Create non-root user for better security
RUN useradd -m appuser

WORKDIR /app

# Copy installed packages and app code
COPY --from=builder /usr/local /usr/local
COPY ./app ./app

# Switch to non-root user
USER appuser

# Expose FastAPI default port
EXPOSE 8000

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
