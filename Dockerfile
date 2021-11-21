# syntax = docker/dockerfile:1.2
FROM python:3.10-slim-buster
ARG GITHUB_TOKEN

# as default use 1000/1000 as UID/GID, but they can be changed at build time if required
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN useradd -ms /bin/bash me

# run apt update/upgrade/install commands
# use buildkit cache directory 
RUN rm -f /etc/apt/apt.conf.d/docker-clean
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update -qq
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get upgrade -yq

# Install optional dependencies
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get install -yqq --no-install-recommends \
    git zsh wget

RUN rm -rf /var/lib/apt/lists/*

# create .venv for user
ENV VIRTUAL_ENV=/home/me/.venv
RUN python3 -m venv $VIRTUAL_ENV --prompt myvenv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN chown -R me:me /home/me
RUN --mount=type=cache,target=/home/me/.cache \
    chown -R me:me /home/me/.cache

# from here all commands run as the user "me"
USER me

WORKDIR /code
COPY --chown=me:me requirements.txt .
COPY --chown=me:me test-requirements.txt .
COPY --chown=me:me dev-requirements.txt .

# run pip install with caching
RUN --mount=type=cache,target=/home/me/.cache \
    pip install --upgrade pip && \
    pip install -r ./requirements.txt \
    pip install -r ./test-requirements.txt \
    pip install -r ./dev-requirements.txt 

# copy current directory in workdir
ADD --chown=me:me . /code

# set the permissions for the UID/GID
RUN if [ "$USER_GID" != "1000" ] || [ "$USER_UID" != "1000" ]; then groupmod --gid $USER_GID me && usermod --uid $USER_UID --gid $USER_GID me; fi

USER root
RUN chown -R me:me /home/me/.cache
USER me

EXPOSE 5000