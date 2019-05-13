from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import matplotlib.pyplot as plt
import matplotlib 

matplotlib.use('agg')
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
    plt.close()
    plt.plot(nilai_x, nilai_y)
    plt.title('Grafik yang dihasilkan')
    plt.xlabel('Nilai X')
    plt.ylabel('Nilai Y')
    plt.savefig('storage/Grafik.png')
    namafile = 'Grafik.png'
    return redirect(url_for('grafik', x = namafile))

@app.route('/storage/<path:x>')
def grafik(x):
    return send_from_directory('storage', x)

if __name__ == "__main__":
    app.run(debug=True)