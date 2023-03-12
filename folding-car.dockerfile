FROM nvidia/cuda:11.2.2-base-ubuntu18.04
LABEL description="Ford F150 Lightning Mock-Up"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      ocl-icd-opencl-dev \
      clinfo \
      curl \
    # point at lib mapped in by container runtime
    && mkdir -p /etc/OpenCL/vendors \
    && echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd \
    # next line gets past the fahclient.postinst
    && mkdir -p /etc/fahclient && touch /etc/fahclient/config.xml \
    # download and verify checksum
    && curl -fsSL \
      https://download.foldingathome.org/releases/public/release/fahclient/debian-stable-64bit/v7.6/fahclient_7.6.21_amd64.deb \
      -o fah.deb \
    && echo "2827f05f1c311ee6c7eca294e4ffb856c81957e8f5bfc3113a0ed27bb463b094 fah.deb" \
      | sha256sum -c --strict - \
    # install and cleanup
    && DEBIAN_FRONTEND=noninteractive dpkg --install --force-depends fah.deb \
    && rm -rf fah.deb \
    && apt-get purge --autoremove -y curl \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN apt-get update \
    && apt-get install python3 python3-pip -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN pip3 install requests

# Need to delete to avoid overwriting
RUN rm /etc/fahclient/config.xml

COPY configs/config.xml /etc/fahclient/config.xml
COPY scripts/start-fah.bash /start-fah.bash
COPY scripts/stop-fah.bash /stop-fah.bash

COPY car.py /car.py
COPY fordclient.py /fordclient.py
COPY structs.py /structs.py

ENTRYPOINT ["python3", "car.py"]
