from flask import Flask
from flask import render_template
from flask import render_template_string
from flask import make_response
from flask import request
import json
from command import Command


app = Flask(__name__)


@app.route('/')
def home():
    toggle_data = load_cookie()
    return render_template('index.html', toggle_data=toggle_data)


@app.route('/get-pokemons', methods=['POST'])
def get_pokemons():
    generation = int(request.values.get('generation'))-1
    pokemon_list = command.pokemon_list(generation)
    return render_template('pokemon_list.html', pokemon_list=pokemon_list)


@app.route('/get-command', methods=['POST'])
def get_command():
    return command.command
    # return render_template_string('', command=command.command)


@app.route('/toggle', methods=['POST'])
def toggle():
    id_ = request.values.get('id')
    return save_cookie(str(command.toggle(id_)))


@app.route('/slider', methods=['POST'])
def change_slider():
    slider = request.values.get('slider')
    value = request.values.get('value')
    return save_cookie(command.change_slider(slider, value))


@app.route('/top-panel', methods=['POST'])
def top_panel():
    return render_template('top_panel.html', options=command.top_panel())


@app.route('/load-cookie')
def load_cookie():
    toggle_data = request.cookies.get('toggle-data')
    if toggle_data:
        command.load_cookie(json.loads(toggle_data))
    return command.data


@app.route('/save-cookie', methods=['POST'])
def save_cookie(response=''):
    resp = make_response(response)
    resp.set_cookie('toggle-data', str(command.save_cookie).replace('\'', '"'))
    return resp


if __name__ == '__main__':
    command = Command()
    # print(command.top_panel())
    app.run(debug=True)
