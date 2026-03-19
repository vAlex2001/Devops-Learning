# Base image - start from official Python
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Sets python not to buffer the request
ENV PYTHONUNBUFFERED=1

# Install the neccessary library for connecting to PostgreSQL
RUN pip install psycopg2-binary

# Copy our app into the container
COPY app.py .

# Tell Docker this container listens on port 8080
EXPOSE 8080

# Command to run when container starts
CMD ["python3", "app.py"]