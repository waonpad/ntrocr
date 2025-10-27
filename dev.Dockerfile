# 既にuvがインストールされているイメージをベースにする
FROM ghcr.io/astral-sh/uv:0.4.24-python3.13-bookworm

# 作業ディレクトリを設定
WORKDIR /workspace

# 諸々の環境変数を設定
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV UV_LINK_MODE=copy

# venvを使わないようにする
ENV UV_PROJECT_ENVIRONMENT="/usr/local/"

# Taskfileをインストール
RUN sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b /usr/local/bin

# キャッシュを効かせやすくするためパッケージのインストールだけ先にする
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

# 残りのファイルをコピー
COPY . /workspace
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

ENTRYPOINT []
