# uv template

## 中身

| やる事               | 使うもの                                                   |
| -------------------- | ---------------------------------------------------------- |
| パッケージ管理       | [uv](https://docs.astral.sh/uv/)                           |
| 型チェック           | [Pyright, Pylance](https://microsoft.github.io/pyright/#/) |
| リント, フォーマット | [Ruff](https://docs.astral.sh/ruff/)                       |
| タスクランナー       | [Taskfile](https://taskfile.dev/)                          |
| Git フック           | [lefthook](https://github.com/evilmartians/lefthook)       |
| デプロイ             | [Cloud Run](https://cloud.google.com/run)                  |

## セットアップ

### DevContainer を起動して Python のコンテナに入る

VSCode の拡張機能を使う

### タスクコマンド一覧

```bash
task --list
```

## Cloud Run にデプロイ

**デプロイが行える状態まで事前に準備しておく**  
[クイックスタート: Cloud Run に Python サービスをデプロイする  |  Cloud Run Documentation  |  Google Cloud](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service?hl=ja)

詳細なオプション  
[gcloud run deploy  |  Google Cloud CLI Documentation](https://cloud.google.com/sdk/gcloud/reference/run/deploy)

### デプロイ

```bash
gcloud run deploy --source . --port=8000 --region asia-northeast1 --allow-unauthenticated
```

サービス名を実行時に指定する場合は `--service` オプションを使う

### 環境変数込みでデプロイする場合

.env ファイルから yml ファイルに変換するスクリプトを用意
https://github.com/waonpad/env2yml/tree/main/build  
※ 手動でやってもいい

```bash
./env2yml-darwin-arm64 .env.prod
```

```bash
gcloud run deploy --source . --port=8000 --region asia-northeast1 --allow-unauthenticated --env-vars-file=.env.prod.yml
```

全環境変数削除オプション `--clear-env-vars`

### リソースの削除

[Cloud Run サービス内の gcloud コマンドラインのチュートリアル  |  Cloud Run Documentation  |  Google Cloud](https://cloud.google.com/run/docs/tutorials/gcloud?hl=ja#delete-resources)

```bash
gcloud run services delete <サービス名> --region asia-northeast1
```
