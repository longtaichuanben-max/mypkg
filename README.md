# mypkg

# mkcon
![test](https://github.com/longtaichuanben-max/robosys2025/actions/workflows/test.yml/badge.svg)
## インストール方法
以下のコマンドをターミナルで入力してください。
```
$ git clone https://github.com/longtaichuanben-max/robosys2025.git
$ cd robosys2025
```
## 食べ物リストの形式例
"食べ物名 カロリーの数値"のように半角スペース空けて行ごとに情報を記入してください。

例
```
apple 80
banana 84
アジ 144
```
## 実行例
例：標準入力からテキストファイルを渡すと、指定の形式で入力されたテキストファイルのカロリーの合計値を出力します。例として上記の形式例の内容を渡す。

入出力
```
$ cat test.txt | ./mkcon
308.0
```
例：カロリーの合計値が日本人男性のカロリー摂取量である2650kcalを超えていた場合は以下のように
空白が出力されます。例として摂取カロリーの合計が3080kcalであった場合を挙げます。
```

```
## 必要なソフトウェア
- Python
  -テスト済みバージョン: 3.7~3.14
- Ubuntu 24.04 LTS
## テスト環境
- Ubuntu 24.04 LTS
## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Ryuta Kawamoto
## 参考文献
- このパッケージのディレクトリ構成やテスト方式、コードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て参考にしています。
    - [ryuichiueda/slides_marp/robosys2025](https://github.com/ryuichiueda/slides_marp/tree/master/robosys2025) （© 2025 Ryuichi Ueda）
