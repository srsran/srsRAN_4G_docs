.. _enb_advanced:

Advanced Usage
==============

MIMO
****

The srsENB supports MIMO transmission modes 2, 3, and 4. You only need to set up the transmission mode and the number of eNb ports in the ``enb.conf`` file:

.. code::

  ...
  [enb]
  ...
  tm = 3
  nof_ports = 2
  ...
  
The eNb configures the UE for reporting the Rank Indicator for transmission modes 3 and 4. You can set the rank indicator periodic report in the file ``rr.conf`` field ``m_ri``. This value is multiples of CQI report period. For example, if the CQI period is 40ms and ``m_ri`` is 8, the rank indicator will be reported every 320ms.

5G NSA
******

5G Non-Standalone mode provides 5G to existing 4G infrastructure.
This approach has been used for the majority of commercial 5G network deployments to date. It provides
improved data rates associated with 5G while leveraging existing 4G infrastructure. Both UEs eNBs must support 5G NSA to take advantage
of 5G NSA services, but existing 4G devices on the network are not disrupted.

What is 5G NSA Mode?
--------------------

.. figure:: .imgs/5G_NSA_mode3.png
  :align: center
  
  5G NSA Mode 3

5G NSA involves a UE first connecting to an LTE network. If both the UE and eNB support NSA, and a gNB cell is present 
then a NSA connection will be established. The NR node is deployed as a Secondary Node (SN) to 
the LTE Master Node (MN). With an NSA connection, a 5G NSA UE connects first to the 4G carrier 
before also connecting to the secondary 5G carrier. The 4G anchor carrier is used
for control plane signaling while the 5G carrier is used for high-speed data plane traffic. 
This results in improved data rates compared to a standard LTE connection.  

The following signaling procedure is used when initiating a 5G NSA link: 

.. figure:: .imgs/NSA_Signaling.png
  :align: center
  
  5G NSA Signaling Procedure. Modified from `here <https://www.sharetechnote.com/html/5G/5G_LTE_Interworking.html>`_. 

The above signaling procedure for the creation of an NSA connection occurs after the initial LTE connection between the UE and eNB is made. The NR connection 
is then made via the RRC Connection Reconfiguration process.  

To summarise, only data is sent along the 5G NR link, while control messaging still relies on an LTE link. The result of this 
is that peak data rates with a 5G NSA connection will be higher than a standard LTE connection, but latency will not be improved. 5G NSA does not 
constitute a "full" 5G Network, but is rather the first step MNOs will take before implementing full 5G SA networks. This will allow users to benefit 
from some of the advancements made in 5G networks earlier. Implementing 5G NSA in existing LTE networks affords MNOs the opportunity to get a return on initial 
investments in 5G infrastructure, without having to wait for full 5G SA deployments. 

Implementing 5G NSA with srsENB
-------------------------------

To enable a 5G NSA connection with srsENB you will need to modify the configuration files for srsENB. Namely, the *rr.conf* file, by enabling an NR cell for the 
existing eNB. This is covered in more detail in the relevant :ref:`app note<5g_nsa_zmq_appnote>` detailing how to use ZMQ to create an E2E 5G NSA network using srsRAN. 

5G NSA gNodeB Features
----------------------
<TO DO>