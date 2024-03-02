# Use an ARG statement to specify a default Python version
ARG PYTHON_VERSION=3.9-slim

# Use the build argument to specify the Python image version
FROM python:${PYTHON_VERSION}

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run your script when the container launches
CMD ["python", "./your_script.py"]
