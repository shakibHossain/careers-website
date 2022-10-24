from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Toronto, ON',
    'salary': '$ 80,000'
  },
  {
    'id': 2,
    'title': 'Data Scientsit',
    'location': 'Waterloo, ON',
    'salary': '$ 70,000'
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
