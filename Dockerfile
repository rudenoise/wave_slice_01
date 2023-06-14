FROM jupyter/scipy-notebook:latest

COPY wav_files /home/jovyan/wav_files
COPY notebooks /home/joyvan/wav_files
COPY wave_slice /home/jovyan/wave_slice
COPY jupyter_conf /home/jovyan/.jupyter/lab/user-settings/@jupyterlab/apputils-extension
COPY requirements.txt /home/jovyan/requirements.txt

RUN pip install -r requirements.txt
