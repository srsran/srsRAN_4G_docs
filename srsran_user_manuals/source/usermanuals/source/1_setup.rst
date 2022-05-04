.. _gen_4g:

LTE Setup Guide
===============

Baseline Hardware Requirements
*********************************

.. figure:: .imgs/basic_arch.png
    :width: 800px
    :align: center
    :alt: Architecture block diagram
    :figclass: align-center

    Basic srsRAN System Architecture (4G LTE)

The overall system requires 2 x RF-frontends and 2 x PCs with a Linux based OS.  
This can be broken down as follows: 
 
.. list-table:: System Hardware Requirements
   :widths: 25 20 25
   :header-rows: 1

   * - Network Element
     - RF-Frontend
     - Linux based PC 
   * - srsUE
     - X
     - X
   * - srsENB/ srsGNB 
     - X
     - X
   * - srsEPC
     - 
     - X

The UE will be instantiated on machine 1 with an RF-frontend attached. The eNB will run on machine 2 with an RF-frontend attached 
to communicate over the air with the UE. The EPC will be instantiated on the same machine as the eNB. See the following figure which outlines 
the overall system architecture. 

A list of supported RF front-end drivers is outlined :ref:`here<Drivers>`.  We also have some suggested hardware packages, which can be found :ref:`here<suggestedHW_appnote>`. 

Running a 4G End-to-end System
*****************************************************

The following execution instructions are for users that have the appropriate RF-hardware 
to simulate a network. If you would like to test the use of srsRAN without RF-hardware please 
see the `ZeroMQ application note <https://docs.srsRAN.com/en/latest/app_notes/source/>`_.

The srsUE, srsENB and srsEPC applications include example configuration files
that should be copied (manually or by using the convenience script) and modified,
if needed, to meet the system configuration.
On many systems they should work out of the box.

By default, all applications will search for config files in the user's home
directory (~/.srs) upon startup.

Note that you have to execute the applications with root privileges to enable
real-time thread priorities and to permit creation of virtual network interfaces.

srsENB and srsEPC can run on the same machine as a network-in-the-box configuration.
srsUE needs to run on a separate machine.

If you have installed the software suite using ```sudo make install``` and
have installed the example config files using ```sudo srsRAN_install_configs.sh```,
you may just start all applications with their default parameters.

srsEPC
------

On machine 1, run srsEPC as follows::

  sudo srsepc

Using the default configuration, this creates a virtual network interface
named "srs_spgw_sgi" on machine 1 with IP 172.16.0.1. All connected UEs
will be assigned an IP in this network.

srsENB
------

Also on machine 1, but in another console, run srsENB as follows::

  sudo srsenb


srsUE
-----

On machine 2, run srsUE as follows::

  sudo srsue

Using the default configuration, this creates a virtual network interface
named "tun_srsue" on machine 2 with an IP in the network 172.16.0.x.
Assuming the UE has been assigned IP 172.16.0.2, you may now exchange
IP traffic with machine 1 over the LTE link. For example, run a ping to 
the default SGi IP address::

  ping 172.16.0.1
  

Examples
**********************
If srsRAN is build from source, then pre-configured example use-cases can be found in the following folder: ```./srsRAN/build/lib/examples``` 

The following list outlines some of the use-cases covered: 

 * Cell Search
 * NB-IoT Cell Search
 * A UE capable of decoding PDSCH packets
 * An eNB capable of creating and transmitting PDSCH packets

Note, the above examples require RF-hardware to run. These examples also support the use 
of `srsGUI <https://github.com/srsRAN/srsGUI>`_ for real time plotting of data. 
