# ファイル名を Dockerfile にしておくと cloud run deploy で自動的に使用される

FROM python:3.13-slim-bookworm

WORKDIR /workspace

# 諸々の環境変数を設定
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_LINK_MODE=copy

# venvを使わないようにする
ENV UV_PROJECT_ENVIRONMENT="/usr/local/"

# uvのイメージからuvのバイナリだけをコピー
COPY --from=ghcr.io/astral-sh/uv:0.4.24-python3.13-bookworm /usr/local/bin/uv /usr/local/bin/

COPY . /workspace

# プロダクション環境で必要なパッケージだけインストール
RUN uv sync --frozen --no-cache --no-dev

RUN rm -f /usr/local/bin/uv

CMD ["fastapi", "run", "src/main.py", "--host", "0.0.0.0"]