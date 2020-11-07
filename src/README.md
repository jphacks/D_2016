# 実行環境と実行手順について

## 実行環境

- Windows 10
- Python 3.X (3.7.4、3.9.0で検証)



## 実行手順

1. [必要パッケージのインストール](#必要パッケージのインストール)
1. [`src/initialization.py`の実行](#`src/initialization.py`の実行)
1. [はかどり小町ちゃんを起動](#はかどり小町ちゃんを起動)
1. [小町ちゃんと一緒に作業する！](#小町ちゃんと一緒に作業する！)
1. [トラブルシューティング](#トラブルシューティング)



### 必要パッケージのインストール

以下のパッケージが必要です。
```
keyboard==0.13.5
lxml==4.6.1
mccabe==0.6.1
Pillow==8.0.1
python-docx==0.8.10
pywin32==228
```

以下のコマンドで一括でインストールできます。
`pip install -r requirements.txt` 


### `src/initialization.py`の実行

最初に初期化プログラムを動かします。

```python
python src/initialization.py
```

実行すると質問が3つ出ます。

#### 「小町ちゃんに呼んでほしい名前をひらがなで入力してください：」

例えば「だにー」のように入力します。

#### 「はかどり小町ちゃんをスタートアップに登録しますか？(y/n):」

登録しない場合は`n`を入力してください。`y`または`Enter`を押すと登録され、次回PC立ち上げ時に「はかどり小町ちゃん」が起動します。

#### 「src/配下にバッチファイルを作成しますか？(y/n):」

作成すると`src/`配下にダブルクリックで「はかどり小町ちゃん」を起動するショートカットが作成されます。


###  はかどり小町ちゃんを起動

`python src/main.py`と実行、または`komati.bat`をダブルクリックして起動。
起動すると、黒い画面が立ち上がります。

### 小町ちゃんと一緒に作業する！

黒い画面が出た状態で以下のことを試してみましょう。

- `src/test.docx`を起動
- `src/test.docx`に100文字以上記入して保存する
- `src/test.docx`を閉じる

また頑張ってる状態に応じて応援してくれます。

- `src/test.doct`をアクティブウィンドウにして1時間以上作業する
- `src/test.docx`を夜中(21時～翌3時)に起動する



## トラブルシューティング

### 音声は流れるが、通知が出ません

**通知設定がオフになっている**かもしれません。`Windows`キーを押して「通知とアクションの設定」から「アプリやその他の送信者からの通知を取得する」をオンにしてみてください。



## `main.py`を実行すると`ModuleNotFoundError`が出る

```python
Traceback (most recent call last):
  File "C:\Users\{user_name}\Documents\GitHub\D_2016\src\main.py", line 9, in <module>
    import text_generator
  File "C:\Users\{user_name}\Documents\GitHub\D_2016\src\text_generator.py", line 4, in <module>
    import config
ModuleNotFoundError: No module named 'config'
```

先に`src/initialization.py`を実行してください。



### venvの仮想環境を使っているとバッチファイルが動きません

対応していないので、自分でvenvをactivateしたのちに`src/main.py`を実行してください。



### 名前を変えたい

`src/config.py`をいじるか、再度`src/initialization.py`を実行してください。