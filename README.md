
# Bottleでじゃんけんゲーム
<br>

---

# templateによる画像読み込み
## static/janken.html

```html
<h1>じゃんけん</h1>
<p class="female"><img src="/static/img/pa_female.png" alt=""></p>
<p class="msg">対決</p>
<ul>
    <li><img src="/static/img/gu.png" alt=""></li>
    <li><img src="/static/img/choki.png" alt=""></li>
    <li><img src="/static/img/pa.png" alt=""></li>
</ul>
```
<br>

## janken.py
```python
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# ～ ～ 途中割愛 ～ ～

#実行したpyファイルのからのstaticフォルダのパス
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# ～ ～ 途中割愛 ～ ～

#CSSファイルを読み込んだ場合
@get("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root=f"{STATIC_DIR}\img")

```

---

# クリックしたら情報を送る
## static/janken.html

```html
<ul>
    <li><a href="/?choice=0"><img src="/static/img/gu.png" alt=""></a></li>
    <li><a href="/?choice=1"><img src="/static/img/choki.png" alt=""></a></li>
    <li><a href="/?choice=2"><img src="/static/img/pa.png" alt=""></a></li>
</ul>
```

<br>

---

# HTMLからの情報を受け取る
## janken.py

```python
def index():
    choice = request.query.choice

```

<br>

---

# PC側のじゃんけんの準備
## def index 実行前

- 下記のPC用画像ファイル名をリストpc_imgに入れる

    - 'gu_female.png', 'choki_female.png', 'pa_female.png'

<br>

- def index 内でじゃけんの処理
  - ランダムで0，1，2の数字を生成する

<br>

---

# 【演習】じゃんけんの勝敗を表示する
## 以下の作業をjanken.pyでおこなってください

- じゃんけんアルゴリズムをつかって、ユーザの手とPCの手で勝敗を確認してください
    - 勝敗の結果を 変数 data に格納してください
        -ユーザが勝った場合 → あなたの勝ち
        -ユーザが負けた場合 → あなたの負け
        -あいこの場合 → あいこ

<br>

- PC画像をランダムの数値に合わせて変更してください

<br>

- dataをtemplateの戻り値でHTMLに返し、HTML側で表示します

<br>

---

# ユーザ側の手の画像変更（CSS）
## CSSをPythonから変更できるようにするためにhtmlを修正

```html
<ul>
    <li><a href="/?choice=0"><img src="/static/img/gu.png" alt="" style="{{result[0]}}"></a></li>
    <li><a href="/?choice=1"><img src="/static/img/choki.png" alt="" style="{{result[1]}}"></a></li>
    <li><a href="/?choice=2"><img src="/static/img/pa.png" alt="" style="{{result[2]}}"></a></li>
</ul>
```

## Python側でresultを初期化

```python
result = ["","",""]
@route("/")
def index():
```

## 繰り返しじゃんけんをする際の初期化と値の追加

```python
else:
    result[0] = result[1] = result[2] = ""
    user = int(choice)
    result[user] = "opacity:1;transform:scale(1.2);"
```

## 結果をtemplateで送信
```python
return template('janken', data = data, female = female, result = result)
```