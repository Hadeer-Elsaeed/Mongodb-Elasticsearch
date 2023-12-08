# Use the official Python image as the base image
FROM python:3.8-slim
# Set the working directory inside the container
WORKDIR /app
# Copy the entire project directory into the container's /app directory
COPY . /app
RUN apt-get update && apt-get install -y curl
# Install the Python dependencies from requirements.txt
RUN pip install -r ./app/requirements.txt
# Make main.py executable
RUN chmod +x ./app/main.py
# Specify the command to run the main.py script
CMD ["python", "./app/main.py"]
