# Jeeves assistant

- [Description](#description)
- [Features](#features)
- [Getting started](#getting-started)


## Description
Jeeves is a virtual assistant based on a LLM and running as a Telegram bot.

The bot has two main commands:
- `new` to clear the conversation history and start chatting again;
- `start`/`help`/`info` to show the info menu;
- `shutdown` to shut down the host machine (to gracefully shut down if you remotely control the device power);

All sent messages are replied by the assistant.

## Features

It can work with:
- a local [model from Ollama](https://ollama.com/library);
- a model from an external OpenAI-compliant provider;

Make sure to create the `.env` file with the variable you need to run one or another.

## Dependencies

Before getting started, make sure you have obtained your [Telegram bot token](https://core.telegram.org/bots/tutorial) and set it in the `.env` file.

## Getting started

To get started place in the base project folder and type:
```sh
make build
```

Depending on the service you want, go to [start ollama](#start-ollama) or [start openai](#start-openai)

<br>

---
### Start Ollama
To start the Ollama based version, type:

```sh
PROFILE=ollama make up
```
The profile will also start the local ollama service to host the model.

Only the first time you will also have to download the model, so you will also have to type:
```sh
make ollama-first-setup
```

---

### Start OpenAI

To start the OpenAI compliant based version, just type:
```sh
make up
```

---
<br>

Once services are up, to tail on logs, type:
```sh
make tail
```

Logs will also be persisted at `stack/logs`.

To stop the services, type:
```sh
make down
```
