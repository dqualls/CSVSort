IMAGE=csv-sort

build:
	docker-compose build ${IMAGE}
	docker image prune -f
	docker container prune -f

run : build
	docker-compose run ${IMAGE} $(sort_column)
