all:
	@echo "Alailable commands:"
	@echo " - test"
	@echo " - front"
	@echo " - celeryup"
	@echo " - celerydown"
	@echo " - flower"

test:
	flake8 --exit-zero --exclude=migrations .
	python3 ./manage.py celery multi start testworker --logfile="$$HOME/shiva/log/celery/%N.log" --pidfile="$$HOME/shiva/run/celery/%N.pid" --loglevel=DEBUG
	coverage run --include=./* ./manage.py test --no-input
	python3 ./manage.py celery multi stop testworker --pidfile="$$HOME/shiva/run/celery/%N.pid"

front:
	gulp webpack

celeryup:
	python3 ./manage.py celery multi start devworker --logfile="$$HOME/shiva/log/celery/%N.log" --pidfile="$$HOME/shiva/run/celery/%N.pid" --loglevel=DEBUG

celerydown:
	python3 ./manage.py celery multi stop devworker --pidfile="$$HOME/shiva/run/celery/%N.pid"

flower:
	flower
