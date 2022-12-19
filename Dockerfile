FROM python:3 as build
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code

RUN apt-get update
RUN apt-get install binutils libproj-dev gdal-bin -y

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

# for django apps with their own repos, pull them here and copy them to image
# e.g.
# RUN git clone https://github.com/my_repo.git
# COPY my_repo /code/my_repo


FROM build as migrate

COPY ./docker-entrypoint.sh /code/

RUN ["chmod", "+x", "/code/docker-entrypoint.sh"]
RUN ["chmod", "+x", "/code/bin/wait-for-it.sh"]

ENTRYPOINT ["bash", "/code/docker-entrypoint.sh"]
