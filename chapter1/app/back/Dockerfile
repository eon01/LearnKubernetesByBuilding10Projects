# Use an official Python runtime as an image
FROM python:3.6

# The EXPOSE instruction indicates the ports on which a container will listen for connections
EXPOSE 3000

# Sets the working directory for following COPY
WORKDIR /app

# Add the requirements to the container then install needed packages specified in the same file
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Add the API file app.py then run it when the container launches
COPY back.py /app
CMD python back.py
