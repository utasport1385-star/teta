import os
import subprocess
from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading

EARNFM_TOKEN = os.getenv("EARNFM_TOKEN", "adc9585e-dc61-44dd-8f39-3ee7bf03524b")

def run_earnfm():
    subprocess.Popen(["earnfm-client"], env={"EARNFM_TOKEN": EARNFM_TOKEN})

def run_keepalive():
    server = HTTPServer(("0.0.0.0", 8080), SimpleHTTPRequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    threading.Thread(target=run_earnfm, daemon=True).start()
    run_keepalive()
