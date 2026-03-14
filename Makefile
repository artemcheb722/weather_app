.PHONY: up down build
DC = docker compose

up:
	${DC} up
down:
	${DC} down
build:
	${DC} build