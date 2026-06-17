import multiprocessing

bind = "0.0.0.0:8000"  # Replace with your desired host and port
workers = multiprocessing.cpu_count() * 2 + 1  # Adjust as needed
worker_class = "gthread"  # You can use "sync" or other worker classes
threads = 2  # Number of threads per worker (only for gthread worker class)

# Use full paths for log files
errorlog = "/opt/djangoprojects/reports/bin/gunicorn.errors"
accesslog = "/opt/djangoprojects/reports/bin/gunicorn.access"

# Customize other settings as needed
loglevel = "info"