# Nodeflux Assesment

Required Assesment for Software Engineer Intern

## Depedencies
* Docker
* Docker Compose

## How to run
via terminal in this directory

* Build
```sh-session
$ make build
```

* run
```sh-session
$ make run
```

* build and run
```sh-session
$ make build-run
```

* test

```sh-session
$ make test
```

## Future Improvement
* testing client method
* add redis to store client request data, so whenever the api try to get COVID data from gov-API, the system just need to access the redis cache