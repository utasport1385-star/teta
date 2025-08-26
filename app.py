from flask import Flask
import threading
import subprocess
import os
import time

EARNFM_TOKEN = os.getenv("EARNFM_TOKEN")

app = Flask(__name__)

def run_earnfm():
    # اجرای فایل پایتون
    subprocess.Popen(["python3", "earnfm.py"], env={"EARNFM_TOKEN": EARNFM_TOKEN})
    while True:
        time.sleep(60)

@app.route("/")
def home():
    return "Service is running!"

if __name__ == "__main__":
    t = threading.Thread(target=run_earnfm)
    t.start()
    app.run(host="0.0.0.0", port=10000)
