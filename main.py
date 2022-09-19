from assets import Assets
from flask import Flask
from flask import render_template
from flask import make_response
from flask import request
import json
from command import Command

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', toggle_data=get_cookie())


@app.route('/toggle', methods=['GET', 'POST'])
def toggle_option():
    id_ = request.values.get('id')
    return set_cookie(str(command.toggle(id_)))


@app.route('/get-command')
def get_command():
    pass


@app.route('/top-panel')
def top_panel():
    return render_template('top_panel')


@app.route('/show_table', methods=['GET', 'POST'])
def show_grid():
    assets = a.get_data()[:1]
    return render_template('grid.html', assets=assets, toggle_data=get_cookie())


@app.route('/set-cookie')
def set_cookie(response):
    resp = make_response(response)
    resp.set_cookie('toggle-data', str(a.toggle_data).replace('\'', '"'))
    return resp


@app.route('/get-cookie')
def get_cookie():
    toggle_data = request.cookies.get('toggle-data')
    if toggle_data:
        a.toggle_data = json.loads(toggle_data)
    return a.toggle_data


if __name__ == '__main__':
    a = Assets()
    command = Command(999)
    # print(a.toggle_data)
    app.run('0.0.0.0', debug=True)
