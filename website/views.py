from flask import Blueprints

views = Blueprints('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"