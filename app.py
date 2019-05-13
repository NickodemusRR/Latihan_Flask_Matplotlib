from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import matplotlib.pyplot as plt

import matplotlib 
matplotlib.use('agg')   # mengubah backend yang digunakan 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data', methods=['POST'])
def data():
    x = request.form['nilai_x']
    y = request.form['nilai_y']
    nilai_x = []
    nilai_y = []
    
    # membuat list nilai x dan y
    for i in x.split(','):
        nilai_x.append(int(i))

    for i in y.split(','):
        nilai_y.append(int(i))
    
    # membuat grafik
    plt.close()             # menghapus plot yang sudah ada sebelumnya
    plt.plot(nilai_x, nilai_y, ls='--', lw=2, color='blue', marker='o', markersize=8, markerfacecolor='red')
    plt.title('Grafik yang dihasilkan')
    plt.xlabel('Nilai X')
    plt.xticks(nilai_x)
    plt.ylabel('Nilai Y')
    plt.yticks(nilai_y)
    plt.savefig('storage/Grafik.png')
    namafile = 'Grafik.png'
    return redirect(url_for('grafik', x = namafile))

@app.route('/storage/<path:x>')
def grafik(x):
    return send_from_directory('storage', x)

@app.errorhandler(404)
def error(error):
    return '<h1> 404 Not Found!</h1>'

if __name__ == "__main__":
    app.run(debug=True)