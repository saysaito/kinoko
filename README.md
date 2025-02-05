# きのこの山 vs タケノコの里 投票アプリ 開発記録

## 1. プロジェクトの目的
- 初心者でも簡単に作成できるWebアプリの開発
- シンプルな構成でのアプリケーション実装
- デプロイまでの一連の流れの習得

## 2. 使用技術
### 主要技術
- 言語：Python
- フレームワーク：Django

### その他の技術
- フロントエンド：Bootstrap
- バージョン管理：Git/GitHub
- デプロイ：Render
- 静的ファイル管理：WhiteNoise

## 3. 実装機能
### 基本機能
- きのこの山とタケノコの里の投票機能
- 投票結果の表示
- シンプルなUI/UXデザイン

### デザイン
- Bootstrapを使用したレスポンシブデザイン
- カード形式での商品表示
- 実際の商品画像の使用

## 4. 開発プロセス
1. 環境構築
   - Python/Djangoのインストール
   - プロジェクトの初期設定

2. 基本機能の実装
   - 投票機能の作成
   - 結果表示機能の実装

3. デザインの改善
   - Bootstrapの導入
   - UIの調整
   - 商品画像の実装

4. デプロイ
   - GitHubリポジトリの作成
   - Renderでのデプロイ設定
   - 静的ファイルの設定調整

## 5. 直面した課題と解決方法
### 静的ファイルの表示問題
- 課題：本番環境で画像が表示されない
- 解決：
  - `settings.py`の静的ファイル設定の調整
  - `STATICFILES_DIRS`の追加
  - WhiteNoiseの設定変更

### デプロイ時の設定
- 課題：本番環境での適切な設定
- 解決：
  - `build.sh`スクリプトの作成
  - 環境変数の適切な設定
  - セキュリティ設定の追加

## 6. 学んだこと
### 技術面
- Djangoでのウェブアプリケーション開発の基礎
- 静的ファイルの扱い方
- デプロイプロセスの理解

### プロジェクト管理
- GitHubを使用したバージョン管理
- 段階的な機能実装の重要性
- 本番環境でのデバッグ方法

## 7. 今後の展望
### 機能追加の可能性
- 投票結果の詳細分析
- SNSシェア機能
- コメント機能

### 改善点
- UIのさらなる改善
- パフォーマンスの最適化
- セキュリティの強化

## 8. まとめ
シンプルながら実用的なWebアプリケーションを開発し、デプロイまでの一連のプロセスを学ぶことができました。初心者向けのプロジェクトとして、基本的なWeb開発の流れを理解するのに適した規模と内容でした。

## デモ
https://kinoko.onrender.com

### 注意事項
- 無料プランのRenderを使用しているため、以下の制限があります：
  - 15分間アクセスがないとインスタンスが停止します（再アクセス時に起動）
  - データベース（投票結果）は定期的にリセットされます
  - 初回アクセス時は、サーバーの起動に約30秒ほどかかる場合があります

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