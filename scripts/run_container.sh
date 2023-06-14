#!/bin/sh

docker run \
  -p 8888:8888 \
  -v ./wav_files:/home/jovyan/wav_files \
  -v ./notebooks:/home/jovyan/notebooks \
  -v ./wave_slice:/home/jovyan/wave_slice \
  -v ./jupyter_conf:/home/jovyan/.jupyter/lab/user-settings/@jupyterlab/apputils-extension \
  wave_slice_01
