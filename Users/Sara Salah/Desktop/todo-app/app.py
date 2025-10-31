from flask import Flask, render_template, request, redirect
import logging
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

# Metrics
REQUEST_COUNTER = Counter('todo_requests_total', 'Total number of requests to Todo App')

tasks = ["Task 1", "Task 2", "Task 3"]

@app.route("/")
def index():
    REQUEST_COUNTER.inc()
    logging.info("User accessed the index page")
    try:
        return render_template('index.html', tasks=tasks)
    except Exception as e:
        logging.error(f"Error rendering index.html: {e}")
        return "Something went wrong!", 500

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    logging.info("Starting Flask app")
    app.run(host="0.0.0.0", port=5000)