from flask import Flask, render_template, redirect
from controllers.games_controller import games_blueprint
from controllers.results_controller import results_blueprint
from controllers.teams_controller import teams_blueprint

app = Flask(__name__)
app.register_blueprint(games_blueprint)
app.register_blueprint(results_blueprint)
app.register_blueprint(teams_blueprint)


@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()