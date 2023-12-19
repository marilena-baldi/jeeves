SHELL := /bin/bash
DOCKER-COMPOSE := docker-compose -f ./stack/docker-compose.yml
SERVICE_NAME ?= app

include .env

help: ## Show help
	@echo -e "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\\x1b[36m\1\\x1b[m:\2/' | column -c2 -t -s :)"

build: ## Build containers
	$(DOCKER-COMPOSE) build --no-cache

up: ## Start containers
	$(DOCKER-COMPOSE) up -d

ps: ## Show containers status
	$(DOCKER-COMPOSE) ps

down: ## Stop containers
	$(DOCKER-COMPOSE) down

logs: ## Show containers logs
	$(DOCKER-COMPOSE) logs $(SERVICE_NAME)

tail: ## Tail container logs
	$(DOCKER-COMPOSE) logs -f $(SERVICE_NAME)

shell: ## Open shell in container
	$(DOCKER-COMPOSE) run --rm $(SERVICE_NAME) bash

ollama-run: ## Run ollama
	$(DOCKER-COMPOSE) exec ollama ollama run ${OLLAMA_MODEL}

ollama-first-setup: ## Run ollama first setup
	$(DOCKER-COMPOSE) exec ollama ollama pull ${OLLAMA_MODEL}
