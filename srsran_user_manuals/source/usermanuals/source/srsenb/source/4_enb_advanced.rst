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

5G Non-Standalone (NSA) mode adds 5G support on top of existing 4G infrastructure. This is the approach used for many commercial 5G network deployments to date, supporting higher data rates on a secondary 5G carrier while continuing to carry control traffic on the legacy 4G carrier. New 5G NSA-capable UEs can take advantage of 5G NSA services, but existing 4G devices on the network are not disrupted.

What is 5G NSA Mode?
--------------------

.. figure:: .imgs/5G_NSA_mode3.png
  :align: center
  
  5G NSA Mode 3

To activate the secondary 5G NSA carrier, the UE first connects to the 4G network. If both the UE and eNB support NSA, and a 5G secondary cell is present then a secondary bearer will be activated on that 5G cell. The NR node is deployed as a Secondary Node (SN) to the LTE Master Node (MN). The 4G anchor carrier is used for control plane signaling while the secondary 5G carrier is used for high-speed data plane traffic. This can result in improved data rates compared to a standard LTE connection.  

The following signaling procedure is used when initiating a 5G NSA link: 

.. figure:: .imgs/NSA_Signaling.png
  :align: center
  
  5G NSA Signaling Procedure. Modified from `here <https://www.sharetechnote.com/html/5G/5G_LTE_Interworking.html>`_. 

The above signaling procedure for secondary bearer activation occurs after the initial LTE connection between the UE and eNB is made. The NR connection is then made via the RRC Connection Reconfiguration process.  


Implementing 5G NSA with srsENB
-------------------------------

To enable a 5G NSA connection with srsENB you will need to modify the configuration files for srsENB. Namely, the *rr.conf* file, by enabling an NR secondary carrier for the existing eNB. This is covered in more detail in the relevant :ref:`app note<5g_nsa_zmq_appnote>` detailing how to use ZMQ to create an E2E 5G NSA network using srsRAN. 
