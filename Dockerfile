FROM python:3.11.8-alpine3.18 as builder

WORKDIR /app

RUN python3 -m venv /app/venv

ENV PATH="/app/venv/bin:$PATH"

COPY requirements.txt .

RUN apk update \
	&& apk add --virtual build-deps gcc python3-dev musl-dev libffi-dev openssl-dev

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN apk del build-deps

COPY . .

#second stage for building image with just necessary dependencies
FROM python:3.11.8-alpine3.18

WORKDIR /app

COPY --from=builder /app/venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
ENV PORT=8000

COPY . .

EXPOSE ${PORT}

CMD gunicorn -b :${PORT} --access-logfile - --error-logfile - task_backend.wsgi:application
