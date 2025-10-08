from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Hello from Azure Web App! This is version2!',
        'status': 'running',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat()
    }), 200

@app.route('/info')
def info():
    return jsonify({
        'python_version': '3.10',
        'app_name': os.environ.get('WEBSITE_SITE_NAME', 'local'),
        'environment': os.environ.get('ENVIRONMENT', 'development')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
