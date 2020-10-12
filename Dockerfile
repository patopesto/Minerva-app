ARG PYTHON_VERSION=3.8.5
FROM python:${PYTHON_VERSION} as builder
MAINTAINER Alban Moreon bambinito.dev@gmail.com

WORKDIR /build

COPY requirements.txt /build/
RUN pip wheel -r requirements.txt

FROM python:${PYTHON_VERSION}

RUN groupadd -g 999 appuser && \
	useradd -r -d /app -u 999 -g appuser appuser

COPY --from=builder /build /build
RUN pip install -r /build/requirements.txt \
				-f /build \
				&& rm -rf /build \
				&& rm -rf /root.cache/pip

WORKDIR /app
COPY . /app/
RUN chown appuser:appuser -R /app
USER appuser

EXPOSE 5000
CMD ["python", "run.py"]