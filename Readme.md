# Harmonic IO Streaming Framework


[![Build Status](https://travis-ci.org/HASTE-project/HarmonicIO.svg?branch=master)](https://travis-ci.org/HASTE-project/HasteStorageClient)


Framework for distributed task execution, key components:

Master Node - maintains queue of tasks, workers, their containers, etc.
Worker Node - manages and hosts docker containers.
Stream_Connector - client for sending tasks for distributed execution.

**This version has support for containers.**

Forked from https://github.com/beirbear/HarmonicIO

Python 3.x.

## Quickstart


Setup with master and worker on a single node:

* Install Docker
* Install python3, pip

* Clone and Install:
```
$ git clone https://github.com/HASTE-project/HarmonicIO.git
$ cd HarmonicIO
$ pip3 install -e .
```

* Edit `harmonicIO/master/configuration.json` and `harmonicIO/worker/configuration.json` so that the addresses are for the local machine (localhost seems problematic).

* Start the master and worker (separate [screen](http://aperiodic.net/screen/quick_reference) windows recommended):
```
$ sudo ./runMaster.sh
$ sudo ./runWorker.sh
```

* Start an (example) processing container on the worker (localhost) node (replacing `<local-ip>`):

We use the example container `benblamey/hio-example:latest`, which can be built from https://github.com/HASTE-project/HarmonicPE
```
$ curl -X POST "http://<local-ip>:8081/docker?token=None&command=create" --data '{"c_name" : "benblamey/hio-example:latest", "num" : 1}'
```

* Check the container is running:
```
$ sudo docker ps
CONTAINER ID        IMAGE                          COMMAND               CREATED             STATUS              PORTS                  NAMES
5c6146b750ab        benblamey/hio-example:latest   "python example.py"   33 minutes ago      Up 33 minutes       0.0.0.0:9000->80/tcp   happy_jepsen
```

* Use the Stream Connector to send data:

(Modify the script to use the correct IP address):
```
$ python3 example_stream_connector.py
```


* Print the logs of the container to check the output of the executed task (`message was bytes ...`):
```
$ docker logs happy_jepsen 
Listening for tasks...
attempting to open local port: 0.0.0.0:80
Streaming from  172.17.0.1 : 40742
message was bytes: 125
```

* Create your own processing container running the HarmonicPE processing daemon:
https://github.com/HASTE-project/HarmonicPE

## Install the Streaming Connector only

* Install python3, pip

* Clone and Install:
```
$ git clone https://github.com/HASTE-project/HarmonicIO.git
$ cd HarmonicIO
$ pip3 install -e .
```
