FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies from the requirements.txt file
# If you are using a different package manager, adjust this command
RUN pip install -r requirements.txt

CMD ["python", "app.py"]