FROM python:3.8.2-slim-buster
# Need local files (e.g., Pipfile.lock) at build time, even though we subsequently volume-mount
ADD . /app
WORKDIR /app
RUN apt-get update && apt-get install -y
RUN pip install --upgrade pip
RUN pip install pipenv
# Use pipenv to pin dependencies
# Ideally, per https://github.com/pypa/pipenv/pull/2762 we should not install systemwide, but 
# rather use pipenv run when running gunicorn. Unfortunately, doing that is making nginx sad,
# so we make our dependencies globally available
RUN pipenv install --system  --ignore-pipfile
