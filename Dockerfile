# Start with a lightweight Python image
FROM python:3.9-slim

# Set a working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the libraries
RUN pip install -r requirements.txt

# Copy your Python script into the container
COPY telemetry_dash.py .

# Tell Docker what to run
CMD ["python", "telemetry_dash.py"]