FROM python:3.10 as builder

RUN python -m venv /opt/app/
WORKDIR /opt/app/

RUN bin/pip install -U pip

COPY requirements.txt /opt/
RUN bin/pip install -Ur /opt/requirements.txt

COPY watched/ /opt/watched/
COPY setup.py /opt/
RUN cd /opt/ \
    && /opt/app/bin/python setup.py sdist \
    && /opt/app/bin/pip install /opt/dist/*


FROM python:3.10 as app

COPY --from=builder /opt/app/ /opt/app/
RUN ln -snf /opt/app/bin/watched-* /usr/local/bin/

ENTRYPOINT ["watched-api"]
