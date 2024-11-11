# Use official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r app/requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "app/src/app.py"]
