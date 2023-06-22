from flask import Flask, render_template, request
import speedtest


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/codie")
def speed():
    wifi = speedtest.Speedtest()

    print("getting download speed")
    download_speed = wifi.download()
    
    print("Getting upload speed")
    upload_speed = wifi.upload()
    
    download = int(download_speed/1000000)
    upload = int(upload_speed/1000000)

    return render_template('index.html',d = download, u = upload )
# @app.route("/", methods = ['POST'])
# def value():
#     return render_template('index.html', d = download, u = upload)
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)