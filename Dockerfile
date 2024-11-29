# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY app.py /app/
COPY model /app/model/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default port
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
