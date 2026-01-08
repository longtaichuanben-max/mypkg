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
ビルドする前に、ワークスペースにsrcディレクトリを作り、以下のリポジトリをクローンしてください。
```
$git clone https://github.com/longtaichuanben-max/person_msgs.git
```
ターミナルでserver.pyを開き任意の正解のパスワード設定を行います。
```
self.correct_password = "password" <--#任意の正解のパスワード
```
ターミナルで以下のclient.pyを実行します。sever.pyの返事を待ちます。
```
$ros2 run mypkg client password <--#任意の判別したいパスワード
```
次に新しいターミナルで以下のコマンドによりserver.pyを実行します。
```
$ros2 run mypkg server
```
## パスワードの正誤判別
client：正誤判別の結果表示
```
#待機中
[INFO] [1767155840.258443790] [client]: 通信中:serverを待っています...
#正解
[INFO] [1767155840.511105936] [client]: [SUCCESS] Login Successful!
#誤り
[INFO] [1767157105.771317182] [client]: [FAILED] Access Denied: Incorrect password.
```
## server_client.launch.py
ターミナルで以下のコマンドよりlaunchファイルを実行することでclientとserverを同時に立ち上げ判別が可能です。
### 判別するパスワード設定
server_client.launch.pyの以下の箇所を任意の判別したいパスワードに書き換えます。
```
arguments=['password'],
```
実行
```
$cd launch
$ros2 launch mypkg server_client.launch.py
```


## 必要なソフトウェア
- Python
- Ubuntu 24.04 LTS
- ROS2
## テスト環境
- Ubuntu 24.04 LTS
## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Ryuta Kawamoto
## 参考文献
- このパッケージのディレクトリ構成やテスト方式、コードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て参考にしています。
    - [ryuichiueda/slides_marp/robosys2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025) （© 2025 Ryuichi Ueda）
