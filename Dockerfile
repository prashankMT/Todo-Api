#
# TODO Flask App Dockerfile
#
#

# Pull base image.
#FROM centos:7.0.1406

FROM python:3.7

# Build commands
RUN mkdir /opt/todo
WORKDIR /opt/todo
ADD requirements.txt /opt/todo/
RUN pip install -r requirements.txt
ADD . /opt/todo
EXPOSE 5000
# Define working directory.
#WORKDIR /opt/todo
ENTRYPOINT ["python", "run.py"]
# Define default command.
# CMD ["python", "manage.py", "runserver"]
