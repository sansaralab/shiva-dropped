all:
	@echo "Alailable commands: test"

test:
	flake8 --exit-zero --exclude=migrations .
	celery multi start testworker --logfile="$$HOME/shiva/log/celery/%N.log" --pidfile="$$HOME/shiva/run/celery/%N.pid"
	coverage run --include=./* ./manage.py test --no-input
	celery multi stop testworker --pidfile="$$HOME/shiva/run/celery/%N.pid"
