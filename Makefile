compile:
	docker build --env-file config/dev.env -t flask-wsgi .

build:
	docker-compose --env-file config/dev.env build

up:
	docker-compose --env-file config/dev.env up

down:
	docker-compose --env-file config/dev.env down

sh:
	docker-compose --env-file config/dev.env exec app sh

build-table:
	aws dynamodb create-table \
	--endpoint-url http://localhost:8000 \
	--table-name users-table-dev \
	--attribute-definitions AttributeName=userId,AttributeType=S \
	--key-schema AttributeName=userId,KeyType=HASH \
	--provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1

list-tables:
	aws dynamodb list-tables --endpoint-url http://localhost:8000
