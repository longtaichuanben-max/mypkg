# mypkg
[![test](https://github.com/longtaichuanben-max/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/longtaichuanben-max/mypkg/actions/workflows/test.yml)

ROS2で動作する、シンプルなパスワード認証システム（サーバー・クライアント）のパッケージです。
カスタムサービス定義パッケージ`person_msgs`を使用して通信を行います。

## 概要
クライアントがパスワードを送信し、サーバーがその正誤を判定して結果を返す仕組みを実装しています。

## ノードとサービス
### server
クライアントからのパスワード照会を受け付け、認証結果を返します。
* **サービス**: `query` [person_msgs/srv/Query]
  * 入力: `password` (String)
  * 出力: `access_granted` (Bool), `message` (String)

### client
サーバーに対してパスワードを送信し、結果をログに表示します。

## 実行方法
### 1. 依存パッケージの準備
このパッケージは、カスタムメッセージ定義 `person_msgs` を使用します。
ビルドする前に、ワークスペースの `src` ディレクトリに以下のリポジトリをクローンしてください。


## 必要なソフトウェア
- Python
- Ubuntu 24.04 LTS
## テスト環境
- Ubuntu 24.04 LTS
## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Ryuta Kawamoto
## 参考文献
- このパッケージのディレクトリ構成やテスト方式、コードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て参考にしています。
    - [ryuichiueda/slides_marp/robosys2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025) （© 2025 Ryuichi Ueda）
