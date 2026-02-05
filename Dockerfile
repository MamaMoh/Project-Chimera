FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml uv.lock* ./

RUN python -m pip install -U pip \
    && python -m pip install pytest python-dotenv requests

COPY . .

CMD ["python", "-m", "pytest"]
