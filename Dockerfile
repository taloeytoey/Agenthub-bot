# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt /code

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . /code

# Make port 80 available to the world outside this container
EXPOSE 5000

# command to run on container start
CMD [ "python", "code/propertyhub.py" ]