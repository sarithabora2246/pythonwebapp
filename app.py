from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': '10L'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India'
}, {
    'id': 3,
    'title': 'Front End Developer',
    'location': 'Remote',
    'salary': '20L'
}]


@app.route("/")
def helloworld():
  return render_template('home.html', jobs=JOBS, companyname='Jovian')


@app.route("/api/jobs")
def getjobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
