# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

ENV LISTEN_PORT=5000

RUN apt-get update && apt-get install -y \
    libcups2-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN python --version
RUN apt update
RUN apt install cups -y

RUN service cups start

# Upgrade pip
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
