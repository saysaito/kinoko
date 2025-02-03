# きのこの山 vs タケノコの里 投票アプリ

シンプルな投票Webアプリケーションです。きのこの山とタケノコの里、どちらが好きかを投票できます。

## 技術スタック
- Python
- Django
- SQLite

## セットアップ方法

1. 依存関係のインストール:
```bash
pip install -r requirements.txt
```

2. データベースのマイグレーション:
```bash
python manage.py migrate
```

3. 開発サーバーの起動:
```bash
python manage.py runserver
```

## 使い方
1. トップページにアクセスします
2. お好きな方（きのこの山またはタケノコの里）に投票します
3. 結果を確認できます 