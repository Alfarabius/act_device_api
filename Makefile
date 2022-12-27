.PHONY: dc-build
dc-build: dc-down
	docker-compose -p alfarabi up -d --no-deps --build --force-recreate act-device-api

.PHONY: dc-up
dc-up:
	docker-compose -p alfarabi up -d

.PHONY: dc-down
dc-down:
	docker-compose -p alfarabi down --remove-orphans -v -t0

.PHONY: dc-rebuild-reup
dc-rebuild-reup: dc-down
	docker-compose -p alfarabi up --build --force-recreate -V -d