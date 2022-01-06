
# Bottleでじゃんけんゲーム


## スライド資料
<br>

---

## templateによる画像読み込み
### static/janken.html

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

### static/janken.pay
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


#### 今が13時の場合
![アラートの表示](./img/alert.png)
<br>

---

## スライド P.19
### 先程のコードに追記してみよう

```javascript
const time = document.querySelector('#time');

const now = new Date();
let hour = now.getHours();
// alert(hour); 
time.innerHTML = `${hour}:00:00`;

```
## 下記のような表示になります
#### 今が14時の場合

![アラートの表示](./img/degital01.png)

<br>

---

## スライド P.24
### 時刻を表示してみよう

```javascript
// alert(hour); 
let min = now.getMinutes();
let sec = now.getSeconds();

time.innerHTML = `${hour}:${min}:${sec}`;
```
## 下記のような表示になります
#### 今が14時13分43秒の場合

![アラートの表示](./img/degital03.png)

<br>

---

## スライド P.29
### デジタル時計を動かしてみよう

```javascript
const clock = () => {
    const now = new Date();
    let hour = now.getHours();
    // alert(hour); 
    let min = now.getMinutes();
    let sec = now.getSeconds();

    time.innerHTML = `${hour}:${min}:${sec}`;
    requestAnimationFrame(clock);
}
clock();
```
### デジタル時計が動きだします  
<br>


---

## スライド P.32
### 二桁表示にしてみよう

```javascript

time.innerHTML = `${`0${hour}`.slice(-2)}:${`0${min}`.slice(-2)}:${`0${sec}`.slice(-2)}`;

```
### 全て二桁表示になります
![二桁表示](./img/degital04.png)

<br>

---

# アナログ時計の針を動かそう

## スライド P.33
### 短針のみを動かしてみよう
```javascript

hourHand.style.transform = `rotate(30deg)`;

```
### 短針が30度傾きます
![短針のみ](./img/analog01.png)

<br>


---

## スライド P.34
### ３つの針を好きな傾きに動かしてみよう  

```javascript

hourHand.style.transform = `rotate(30deg)`;
minHand.style.transform = `rotate(80deg)`;
secHand.style.transform = `rotate(240deg)`;

```
### ３つの針が別々に傾きます
![3つの針](./img/analog02.png)

<br>


---

## スライド P.36
### ３つの針を時刻に合わせて動かしてみよう  

```javascript

hourHand.style.transform = `rotate(${hour*30}deg)`;
minHand.style.transform = `rotate(${min*6}deg)`;
secHand.style.transform = `rotate(${sec*6}deg)`;

```
### ３つの針が時刻に合わせて動きます
<br>

---

## スライド P.38
### 短針を正確な位置に合わせよう  

```javascript

hourHand.style.transform = `rotate(${(hour+min/60)*30}deg)`;

```
![時計の表示](./img/clock.png)
---

