from flask import Flask, render_template, jsonify, session
from user import sign_in, sign_up
from my_place import my_place_list_get, my_place_post, my_place_delete
from place import place_list_get
from random_place import random_place_post
from category import  category_post, category_delete, category_list_get, category_put

app = Flask(__name__)
app.secret_key ="1234"

@app.route('/')
def index():
  return render_template('index.html')

# 헤더 html rendering
@app.route('/header')
def header_render():
  return render_template('header.html')

# 로그인 html rendering
@app.route('/sign_in')
def sign_in_render():
  return render_template('sign_in.html')

# 회원가입 html rendering
@app.route('/sign_up')
def sign_up_render():
  return render_template('sign_up.html')

# 랜점 장소 html rendering
@app.route('/random_place')
def random_place_render():
  return render_template('random_place.html')

# 내장소 관리 html rendering
@app.route('/my_place')
def my_place_render():
  return render_template('my_place.html')

#카테고리 관리
@app.route('/category')
def category_render():
  return render_template('category_manager.html')

# 회원가입 api
@app.route('/api/sign_up', methods=["POST"])
def sign_up_api():
  msg = sign_up()
  return msg

# 회원가입 api
@app.route('/api/sign_in', methods=["POST"])
def sign_in_api():
  user = sign_in()
  return user

# 장소 목록 api
@app.route('/api/place', methods=["GET"])
def place_list_get_api():
  place_list = place_list_get()
  return place_list

# 내 장소 목록 api
@app.route('/api/my_place', methods=["GET"])
def my_place_list_get_api():
  place_list = my_place_list_get()
  return place_list

# 장소 삭제 api
@app.route('/api/my_place', methods=["DELETE"])
def my_place_delete_api():
  msg = my_place_delete()
  return msg

# 장소 등록 api
@app.route('/api/my_place', methods=["POST"])
def my_place_post_api():
  msg = my_place_post()
  return msg

# 랜덤 장소 조회 api
@app.route('/api/random_place', methods=["POST"])
def random_place_post_api():
  return random_place_post()

# 카테고리 목록 api
@app.route('/api/category', methods=["GET"])
def category_list_get_api():
  return category_list_get()

# 카테고리 삭제 api
@app.route('/api/category', methods=["DELETE"])
def category_delete_api():
  return category_delete()

# 카테고리 등록 api
@app.route('/api/category', methods=["POST"])
def category_post_api():
  return category_post()

# 카테고리 수정 api
@app.route('/api/category', methods=["PUT"])
def category_put_api():
  return category_put()

if __name__ == '__main__':
  app.run('0.0.0.0', port=5500, debug=True)