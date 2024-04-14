from flask import Flask
import sys
import signal

from prometheus_flask_exporter import PrometheusMetrics

def handler(sig, frame):
    print(f'YOU CALLED ME WITH {sig}')
    # Отключаемся от базы
    # Разрегистрируемся в реджистри
    


signal.signal(signal.SIGTERM, handler)
signal.signal(signal.SIGINT, handler)
# signal.signal(signal.SIGKILL, handler) # SIGKILL мы отловить не можем

app = Flask(__name__)

if __name__ == '__main__':
    app.run()
