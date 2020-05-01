FROM python:3.7
MAINTAINER Kemp Po <kempspo@gmail.com>

COPY requirements.txt /src/

# Install needed packages
RUN pip install -r /src/requirements.txt

# Copy project files
COPY . /src
WORKDIR /src

RUN mkdir -p /src/.pytest_cache/ &&\
    chmod 777 -R /src/.pytest_cache/

# Run
CMD [ "python", "./water_bot.py" ]