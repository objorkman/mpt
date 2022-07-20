FROM ubuntu:18.04
LABEL maintainer="Oscar Bjorkman <oscarb@berkeley.edu>"

RUN apt update

RUN apt-get install -y software-properties-common git libpng-dev zlib1g-dev
RUN add-apt-repository ppa:ubuntu-toolchain-r/test

RUN apt update
RUN apt install -y gcc-9 g++-9
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 60 --slave /usr/bin/g++ g++ /usr/bin/g++-9

RUN apt install -y ninja-build libeigen3-dev libfcl-dev libassimp-dev
RUN git clone https://github.com/flexible-collision-library/fcl.git
WORKDIR fcl/
RUN git checkout f15ffc
RUN mkdir -p build/Release
WORKDIR build/Release
RUN apt-get install -y gpg wget vim
RUN wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | gpg --dearmor - | tee /usr/share/keyrings/kitware-archive-keyring.gpg >/dev/null
RUN echo 'deb [signed-by=/usr/share/keyrings/kitware-archive-keyring.gpg] https://apt.kitware.com/ubuntu/ bionic main' | tee /etc/apt/sources.list.d/kitware.list >/dev/null
RUN apt-get update
RUN rm /usr/share/keyrings/kitware-archive-keyring.gpg
RUN apt-get install -y kitware-archive-keyring
RUN apt-get install -y cmake
RUN cmake -G Ninja -DCMAKE_BUILD_TYPE=Release ../..
RUN ninja
RUN ninja install

WORKDIR /
RUN git clone https://github.com/ompl/omplapp.git
RUN git clone https://github.com/objorkman/mpt.git
RUN git clone https://github.com/UNC-Robotics/nigh.git \
    && cd nigh && mv src/nigh /usr/include/c++/7.5.0

WORKDIR /
RUN cd mpt/demo && mkdir -p build/Release && cd build/Release \
    && CXX=g++ CC=gcc cmake -G Ninja -DCMAKE_BUILD_TYPE=Release ../.. \
    && ninja

