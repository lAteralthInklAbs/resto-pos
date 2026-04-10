FROM python:3.11-slim

# Create non-root user
RUN useradd --create-home --shell /bin/bash pos
WORKDIR /home/pos/app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY --chown=pos:pos . .

# Switch to non-root user
USER pos

# Expose port
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/login || exit 1

# Run with gunicorn
CMD ["gunicorn", "app:create_app()", "--bind", "0.0.0.0:5000", "--workers", "2"]
