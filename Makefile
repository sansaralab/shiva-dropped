all:
	@echo "Alailable commands:"
	@echo " - test"
	@echo " - front"
	@echo " - celeryup"
	@echo " - celerydown"
	@echo " - flower"
	@echo " - docker-up"
	@echo " - docker-db"
	@echo " - docker-down"

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

docker-up:
	docker run --name=shiva-postgres -p 5432:5432 -v /var/lib/postgresql/data:/var/lib/postgresql/data -e POSTGRES_PASSWORD=1 -d postgres

docker-db:
	docker exec shiva-postgres /bin/su - postgres -c "createdb shivadb"
	docker exec shiva-postgres /bin/su - postgres -c "psql -c \"CREATE USER shivauser WITH LOGIN CREATEDB PASSWORD '1';\""

docker-down:
	docker stop shiva-postgres
	docker rm shiva-postgres