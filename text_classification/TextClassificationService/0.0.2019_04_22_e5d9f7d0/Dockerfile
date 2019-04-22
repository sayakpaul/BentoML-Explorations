FROM continuumio/miniconda3

ENTRYPOINT [ "/bin/bash", "-c" ]

EXPOSE 5000

RUN apt-get update && apt-get install -y       libpq-dev       build-essential       && rm -rf /var/lib/apt/lists/*

# copy over model files
COPY . /bento
WORKDIR /bento

ARG conda_env=bentoml-custom-conda-env

# update conda and setup environment
RUN conda update conda -y

# create conda env
RUN conda env create -f /bento/environment.yml

ENV PATH /opt/conda/envs/$conda_env/bin:$PATH

RUN conda install pip && pip install -r /bento/requirements.txt

# Run bento server with path to bento archive
CMD ["bentoml serve /bento"]
