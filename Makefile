.PHONY: re clean logs

all:
	docker-compose up -d --build

re:
	docker-compose restart

clean:
	docker-compose down -v --remove-orphans
	docker system prune -f

logs:
	docker-compose logs -f
