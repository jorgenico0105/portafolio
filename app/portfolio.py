from flask import Flask, Blueprint, render_template

# Definición del Blueprint
bp = Blueprint('portfolio', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('portfolio/index.html')

