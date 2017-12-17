FROM ubuntu:16.04

# env
ENV workdir /configbuddy_ws
ENV configbuddy_app ${workdir}/configbuddy
ENV dotfiles ${workdir}/dotfiles

# workdir
WORKDIR ${workdir}

# setup
RUN apt-get update
RUN apt-get install -y python3 \
  vim \
  git \
  zsh

# install
ADD tools $workdir/tools
ADD dotfiles $dotfiles 
RUN python3 $workdir/tools/get-pip.py
RUN pip install pyyaml

ADD src $configbuddy_app

# cleanup
RUN rm -rf ${workdir}/tools

ENTRYPOINT ["bash"]
