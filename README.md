# きのこの山 vs タケノコの里 投票アプリ

シンプルな投票Webアプリケーションです。きのこの山とタケノコの里、どちらが好きかを投票できます。

## デモ
https://kinoko.onrender.com

## 技術スタック
- Python 3.10
- Django 5.0.2
- SQLite（開発環境）
- PostgreSQL（本番環境）
- Bootstrap 5
- Render（デプロイ先）

## 機能
- きのこの山とタケノコの里への投票
- リアルタイムの投票結果表示
  - 投票数
  - パーセンテージ表示
  - プログレスバーによる視覚化
- レスポンシブデザイン（スマートフォン対応）

## ローカル開発環境のセットアップ

1. リポジトリのクローン:
```bash
git clone https://github.com/saysaito/kinoko.git
cd kinoko
```

2. 仮想環境の作成と有効化:
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
# source venv/bin/activate   # Mac/Linux
```

3. 依存関係のインストール:
```bash
pip install -r requirements.txt
```

4. データベースのマイグレーション:
```bash
python manage.py migrate
```

5. 開発サーバーの起動:
```bash
python manage.py runserver
```

これで http://127.0.0.1:8000/ にアクセスできます。

## デプロイ手順（Render.com）

### 1. 事前準備

以下のファイルが正しく設定されていることを確認：

- `requirements.txt`: 本番環境用パッケージ
- `build.sh`: デプロイ時の実行スクリプト
- `settings.py`: 本番環境用設定

### 2. GitHubとの連携

1. GitHubでリポジトリを作成
2. ローカルリポジトリの設定:
```bash
git init
git add .
git commit -m "初期コミット：投票アプリの基本機能を実装"
git branch -M main
git remote add origin https://github.com/saysaito/kinoko.git
git push -u origin main
```

### 3. Renderでのデプロイ

1. Renderアカウントの作成
   - [Render](https://render.com/)にアクセス
   - GitHubアカウントでサインアップ

2. 新しいWebサービスの作成
   - 「New +」→「Web Service」を選択
   - GitHubリポジトリを連携
   - `kinoko`リポジトリを選択

3. デプロイ設定
   - Name: `kinoko`（または任意の名前）
   - Region: `Singapore`（日本から最も近い）
   - Branch: `main`
   - Runtime: `Python 3`
   - Build Command: `./build.sh`
   - Start Command: `gunicorn kinoko.wsgi:application`
   - Instance Type: `Free`

4. 環境変数の設定
   - `DJANGO_DEBUG`: `False`
   - `DJANGO_SECRET_KEY`: 生成した安全な文字列
   - `DJANGO_SECURE_SSL_REDIRECT`: `True`

5. 「Deploy Web Service」をクリック

### 4. デプロイ後の確認

1. デプロイログの確認
   - ビルドとデプロイのプロセスを監視
   - エラーがないことを確認

2. アプリケーションの動作確認
   - 表示されたURLにアクセス
   - 投票機能のテスト
   - 結果表示の確認

## 開発時の注意点

1. 新しい依存パッケージを追加した場合：
```bash
pip install パッケージ名
pip freeze > requirements.txt
```

2. データベースを変更した場合：
```bash
python manage.py makemigrations
python manage.py migrate
```

3. 本番環境の設定：
- DEBUGはFalseに設定
- SECRET_KEYは必ず変更
- HTTPS通信を強制
- 適切なALLOWED_HOSTSの設定

## ライセンス
MIT

## 作者
Akiko Saito 