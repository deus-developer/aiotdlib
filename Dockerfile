# Use official Python slim image
FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Add testing repository to get newer library versions
RUN echo "deb http://deb.debian.org/debian testing main" > /etc/apt/sources.list.d/testing.list && \
    echo "Package: *\nPin: release a=testing\nPin-Priority: 100" > /etc/apt/preferences.d/testing

# Install minimal runtime dependencies
RUN apt-get update && \
    apt-get install -y -t testing \
    zlib1g \
    libssl3 \
    libc++1 \
    libc++abi1 \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY test.py .

# Install aiotdlib
RUN uv pip install --no-cache --system https://github.com/deus-developer/aiotdlib/archive/main.zip
# RUN uv pip install --no-cache --system aiotdlib

# Set entrypoint
ENTRYPOINT ["python", "test.py"] 