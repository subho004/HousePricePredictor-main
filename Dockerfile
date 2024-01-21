# Use the official Python image as the base image
FROM python:3.12.1-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install build essentials (including gcc)
RUN apt-get update && \
    apt-get install -y build-essential && \
    rm -rf /var/lib/apt/lists/*

# Create and activate a virtual environment
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Install any needed packages specified in requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install scikit-learn==1.2.2


# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 5001 for Flask app
EXPOSE 5001

# Define environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Command to run your application
CMD [ "/bin/bash", "-c", "source /venv/bin/activate && exec /venv/bin/python -m flask run --host 0.0.0.0 --port 5001"]
