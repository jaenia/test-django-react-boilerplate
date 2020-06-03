web: gunicorn todolist2.wsgi --chdir backend --limit-request-line 8188 --log-file -
worker: celery worker --workdir backend --app=todolist2 -B --loglevel=info
