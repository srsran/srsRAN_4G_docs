.. srsLTE No RF Application Note

SRS No RF Application note
==========================


Introduction
************
srsLTE is a full end-to-end LTE solution comprising a core network, an eNodeB, and a UE implementation. Usually eNodeB and UE
are used in conjunction with actual RF front-ends for over-the-air transmissions. There are, however, a number
of use-cases for which RF front-ends might not be needed or wanted. Those use-cases include (but are not limited to) the
use of srsLTE for educational or research purposes, continues integration and delivery (CI/CD) or development and debugging.

With srsLTE this can be achieved by replacing the radio link between eNodeB and UE with a machanism that allows to
exchange baseband IQ samples over an alternative transport. For this purpose, we've implemented a ZeroMQ-based RF driver that
essentially acts as a transmit and receive pipe for exchanging IQ samples over TCP or IPC.

#ZeroMQ has different modes of operation, srsLTE uses Request/Reply mode. The ZMQ module has two entities, a transmitter
#as a repeater and as a requester. The receiver will asynchronously send requests for data to the transmitter and this
#will reply with base-band samples. Consequently, the receiver will store the received data in a buffer, waiting to be
#read.

#Both modules shall operate at the same base rate so their bandwidth expectations can be satisfied.

Limitations
***********
The UE and the eNodeb have a number of timers specified by the 3GPP. Some of these timers are based on system timers and not in RF based timers. When ZMQ between two computers is used, the baseband throughput is so low that the latency sky-rockets and timers expire easily. This cause the UE to frequently fail to attach.


Future work on the eNb and UE sides needs to be carried out in order to fully support this opperation reliably.


ZeroMQ Installation
*******************

First thing is to install ZeroMQ and build srsLTE. On Ubuntu, ZereMQ development libraries can be installed
with:

.. code::

  sudo apt-get install libzmq3-dev
  
Alternativly, installing from sources can also be done.

First, one needs to install libzmq:

.. code::

  git clone https://github.com/zeromq/libzmq.git
  cd libzmq
  ./autogen.sh
  ./configure
  make
  sudo make install
  sudo ldconfig

Second, install czmq:

.. code::

  git clone https://github.com/zeromq/czmq.git
  cd czmq
  ./autogen.sh
  ./configure
  make
  sudo make install
  sudo ldconfig

Finally, you need to compile srsLTE (assuming you have already installed all the required dependencies):

.. code::

  git clone https://github.com/srsLTE/srsLTE.git
  cd srsLTE
  mkdir build
  cd build
  cmake ../
  make

Put extra attention in the cmake console output. Make sure you read the following line:

.. math::

  ...
  -- FINDING ZEROMQ.
  -- Checking for module 'ZeroMQ'
  --   No package 'ZeroMQ' found
  -- Found libZEROMQ: /usr/local/include, /usr/local/lib/libzmq.so
  ...

Running a full end-to-end LTE network on a single computer
**********************************************************

Before launching the LTE network components on a single machine we need to make sure
that both UE and EPC are in different network namespaces.
This is because both EPC and UE will be sharing the same network configuration,
i.e. routing tables etc. Because the UE receives an IP address
from the EPC's subnet, the Linux kernel would bypass the TUN interfaces when
routing traffic between both ends. Therefore, we create a separate
network namespace (netns) that the UE uses to create it's TUN interface in. 

Let's start with creating a new network namespace called "lte1" for the (first) UE:

.. code::

  sudo ip netns add lte1


To verify the new "lte1" netns exists, run:

.. code::
  sudo ip netns list


Now let's start the EPC. That this will create a TUN device in the default
network namespace and therefore needs root permissions.

.. code::

  sudo ./srsepc/src/srsepc
  
  
Let's now launch the eNodeB. We use the default configuration in this example and pass
all parameter that need to be tweeked for ZMQ through as command line arguments. If you
want to make those persistant just add them to your local enb.conf. The eNB can be
launched without root permissions.

.. code::

  ./srsenb/src/srsenb --rf.device_name=zmq --rf.device_args="tx_port=tcp://*:2000,rx_port=tcp://localhost:2001,id=enb,base_srate=23.04e6" --expert.nof_phy_threads=1


Lastly we can launch the UE, again with root permissions to create the TUN device.

.. code::

  sudo ./srsue/src/srsue --rf.device_name=zmq --rf.device_args="tx_port=tcp://*:2001,rx_port=tcp://localhost:2000,id=ue,base_srate=23.04e6" --gw.netns=lte1 --phy.nof_phy_threads=1


The last command should start the UE and attach it to the core network.
The UE will be assigned an IP address in the configured range (e.g. 172.16.0.2).

To exchange traffic in the downlink direction, i.e. from the the EPC, just run ping
or iperf as usual on the command line, e.g.:

.. code::
  
  ping 172.160.0.2
  
  
In order to generate traffic in the uplink direction it is important to run the ping command
in the UE's network namespace. 

.. code::
  sudo ip netns exec lte1 ping 172.160.0.1


Known issues and future work
****************************

* The eNB needs to be started before the UE
* The eNB needs to be restarted after the UE has been killed
