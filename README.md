# Wave Slice experiment Number 1

A project to mess about with mono wave forms. Some loose aims:

- align the phase of two wave-forms of differing pitch.
  e.g: a bass guitar with an 808 sub 1 octave below
- create interesting wave-tables to load into synths
  (serum, vital, pigments etc...)


## Local/lib dev

Use poetry for local/lib development

```sh
poetry install
poetry run sketch.py
```

The `requirements.txt` is generated from poetry and used in to build the docker
container.

```sh
poetry export -f requirements.txt --output requirements.txt
```

A basic library lives in `wave_slice/`

## Notebook

Notebooks live in [`./notebooks`](./notebooks)

The [`Dockerfile`](./Dockerfile) can be used with the lib above like this:

```sh
./scripts/build.sh
./scripts/run_container.sh
```
