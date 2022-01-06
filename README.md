
# Bottleでじゃんけんゲーム

## スライド資料
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

## static/janken.py
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

# HTMLからの情報を受け取る
## static/janken.py

```python
def index():
    data = request.query.choice

```

---

# ランダムでPCのじゃんけんの手を決める
## 以下の作業をjanken.pyでおこなってください

-下記のPC用画像ファイル名をリストに入れる
    -'gu_female.png', 'choki_female.png', 'pa_female.png'

-ランダムで0，1，2の数字を生成する





