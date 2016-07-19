all:
	@echo "Alailable commands:"
	@echo " - test"
	@echo " - front"
	@echo " - celeryup"
	@echo " - celerydown"
	@echo " - flower"

test:
	flake8 --exit-zero --exclude=migrations .
	celery multi start testworker -A app --logfile="$$HOME/shiva/log/celery/%N.log" --pidfile="$$HOME/shiva/run/celery/%N.pid" --loglevel=DEBUG
	coverage run --include=./* ./manage.py test --no-input
	celery multi stop testworker -A app --pidfile="$$HOME/shiva/run/celery/%N.pid"

front:
	gulp webpack

celeryup:
	celery multi start devworker -A app --logfile="$$HOME/shiva/log/celery/%N.log" --pidfile="$$HOME/shiva/run/celery/%N.pid" --loglevel=DEBUG

celerydown:
	celery multi stop devworker -A app --pidfile="$$HOME/shiva/run/celery/%N.pid"

flower:
	flower
