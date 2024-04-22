# Use official Python image as base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY stock_price.py .

# Install dependencies
RUN pip install requests

# Command to run the Python script
CMD ["python", "stock_price.py"]


