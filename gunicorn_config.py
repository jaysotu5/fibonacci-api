workers = 2

bind = '0.0.0.0:5000'


timeout = 30

loglevel = 'info'

accesslog = '-'
errorlog = '-'

worker_class = 'sync'

threads = 4

graceful_timeout = 30
max_requests = 1000
max_requests_jitter = 100
