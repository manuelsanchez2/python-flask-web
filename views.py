from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route('/')
def home():
    return render_template('index.html', name="Pacracio", age=30)

# @views.route('/profile/<username>')
# def profile_username(username):
#     return render_template('profile-urlname.html', name=username)

# @views.route('/profile')
# def profile_queryname():
#     args = request.args
#     name = args.get('name')
#     return render_template('profile-queryname.html', name=name)

# @views.route('/json')
# def get_json():
#     return jsonify({"name": "Pacracio", "age": 30})

# @views.route('/data')
# def get_data():
#     data = request.json()
#     return jsonify(data)

@views.route('/go-to-home')
def go_to_home():
    return redirect(url_for('views.home'))

@views.route('/extension')
def extension():
    return render_template('extension.html')