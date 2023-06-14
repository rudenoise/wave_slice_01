FROM jupyter/scipy-notebook:latest

COPY wav_files /home/jovyan/wave_files
COPY notebooks /home/joyvan/wave_files
COPY wave_slice /home/jovyan/wave_slice
COPY jupyter_conf /home/jovyan/.jupyter/lab/user-settings/@jupyterlab/apputils-extension
COPY requirements.txt /home/jovyan/requirements.txt

RUN pip install -r requirements.txt
