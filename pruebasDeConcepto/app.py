from datetime import datetime
import pytz
import os

# flask library
from flask_cors import CORS
from flask import Flask

# flask library
app = Flask(__name__)
CORS(app)

from services.routes.v1.paths import v1

app.register_blueprint(v1, url_prefix="/")

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    utc_now = datetime.utcnow()
    utc_now = utc_now.astimezone(pytz.timezone('America/Mexico_City'))
    print(utc_now)
    app.run(threaded=True, host='0.0.0.0', port=port, debug=True)