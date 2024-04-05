from flask import Flask, request, jsonify, render_template, Blueprint
from .models import Database

main = Blueprint('main', __name__)

db = Database('database/db.json')

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/ping')
def ping():
    db.insert_onlytime()
    return jsonify({'message': 'pong'})

@main.route('/echo', methods=['POST'])
def echo():
    dado = request.json['dados']
    db.insert_onlytime()
    return jsonify({'mensagem': dado})

@main.route('/dash')
def render():
    return render_template('dash.html')

@main.route('/info')
def info():
    items = db.get_all_data()
    print(items)
    return render_template('log.html', items=items )