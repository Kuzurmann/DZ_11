from flask import Flask


app = Flask(__name__)


@app.route('/')
def page_index():

    page_content = """ 
    <!doctype html>
<html lang="ru">
<head>
  <h1>Манул Барсик</h1>
  <img src="https://cs11.pikabu.ru/post_img/2018/10/17/7/1539775059193916019.jpg" width="450" height="400" alt="Манул" />
  <h2>Милый котик</h2>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<style>
   body {
    background: #FF69B4 url(images/bg.jpg);
    color: #000000;
   }
  </style>
<body>
 <em><p> <strong><big><big>Привет!</strong></p>
<p> Меня зовут Барсик,<br> я манул.</p>
   <div> Я еще совсем маленький.</div>
  <p> Обо мне вы можете прочитать по этой
    <a href="/https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D0%BD%D1%83%D0%BB">ссылке</a>.</p>
    <p> Как вы поняли из текста, я очень <del>добрый</del> <ins>красивый</ins> <mark>котик</mark>.</p>
  </em>
</body>
</html>
    """
    return page_content


app.run(host='127.0.0.1', port=5001)