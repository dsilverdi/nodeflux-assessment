build:
	docker-compose build

run:
	docker-compose up

build-run:
	docker-compose up --build

test:
	python test_app.py