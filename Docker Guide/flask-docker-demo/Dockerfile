# define the base image
FROM python:3-alpine3.15
# define the working directory
WORKDIR /app
# copy everything and move those to the directory
COPY . /app
# install the required python packages using pip
RUN pip install -r requirements.txt
# expose the port in which this application will run.
# This is defined to the python flask file.
EXPOSE 3000
# Now start the application, the entry point of your app
CMD python ./index.py