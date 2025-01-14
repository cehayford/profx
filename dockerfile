# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /profx

# Install dependencies
COPY requirements.txt /profx/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project
COPY . /profx/