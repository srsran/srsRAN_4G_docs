.. srsLTE No RF Application Note

SRS No RF Application note
==========================


Introduction
************
srsLTE is a powerful environment that comprises a core network, an eNodeB and a UE. It is expected to use the eNodeB and
the UE with RF-front ends. However, one may want to run the environment without RF-front ends for various reasons:

- No availability of RF-front end (educational or research purposes)
- Non-Realtime dynamic code analysis (i.e. valgrind)
- Third party base-band application in the middle (i.e. GNU Radio)

One may wonder how this can be possible. It is not rocket science. We have implemented a RF driver that uses ZeroMQ as a
base-band transport layer. ZeroMQ does not more than opening a transmit and a receive pipe for simulating RF
transmission and reception.

ZeroMQ has different modes of operation, srsLTE uses Request/Reply mode. The ZMQ module has two entities, a transmitter
as a repeater and as a requester. The receiver will asynchronously send requests for data to the transmitter and this
will reply with base-band samples. Consequently, the receiver will store the received data in a buffer, waiting to be
read.


Both modules shall operate at the same base rate so their bandwidth expectations can be satisfied.

ZeroMQ Installation
*******************
The first thing one may try is installing ZeroMQ library using apt-get or equivalent. This may work but I highly
recommend installing from sources.

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

Configuring srsLTE
******************
Once srsLTE is compiled, it is time to Rock'n Roll. One needs to tell to the zmq no-RF module the transmit and receive
configuration. In this example, the ue will transmit through the TCP port 5555 and receive in the port 5554:

.. code::

...
device_name = zmq
device_args = tx_port=tcp://*:5555,rx_port=tcp://localhost:5554,id=ue,base_srate=23.04e6
...

On the eNodeB side:

.. code::

...
device_name = zmq
device_args = tx_port=tcp://*:5554,rx_port=tcp://localhost:5555,id=enb,base_srate=23.04e6
...

One may find a bit frustrating the No-RF operation. The main reason for this is the timers implementations. Many timers
in srsLTE are based on the system timers (i.e. gettimeofday) instead of using the radio as a timer. This causes that the
attach is not always successful using zmq.

Despite this handicap, one can tweak the eNodeB for minimising the system timer effects by modifying the sib.conf:

.. code::

  ...
    ue_timers_and_constants =
    {
        t300 = 2000; // in ms
        t301 = 2000;  // in ms
        t310 = 2000; // in ms
        n310 = 20;
        t311 = 30000; // in ms
        n311 = 10;
    };
  ...

Also, one needs to use a single physical layer thread, configure the ue.conf and the enb.conf:

.. code::

  ...
  nof_phy_threads      = 1
  ...

Since you may run the UE and the EPC on the same machine, I recommend you setting a virtual machine with the EPC. For
example, I have a VirtualBox with a Ubuntu server and IP address 192.168.56.101. The epc.conf gpt configuration is:

.. code::

  ...
  mme_bind_addr = 192.168.56.101
  ...
  gtpu_bind_addr   = 192.168.56.101
  ...

At the eNodeB side, the GTP port needs to be configured too:

.. code::

  ...
  mme_addr = 192.168.56.101
  gtp_bind_addr = 192.168.56.1
  s1c_bind_addr = 192.168.56.1
  ...


Integrating srsLTE in GNU radio
*******************************
...

Known issues and future work
****************************
...

