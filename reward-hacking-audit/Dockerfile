FROM python:3.12-slim
COPY wheels /tmp/wheels
RUN pip install --no-cache-dir --no-index --find-links /tmp/wheels pytest && rm -rf /tmp/wheels
WORKDIR /repo
CMD ["tail", "-f", "/dev/null"]
