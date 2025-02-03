#!/usr/bin/env bash
# デプロイ時に実行されるスクリプト

# Pythonパッケージのインストール
pip install -r requirements.txt

# データベースのマイグレーション
python manage.py migrate

# 静的ファイルの収集
python manage.py collectstatic --no-input 