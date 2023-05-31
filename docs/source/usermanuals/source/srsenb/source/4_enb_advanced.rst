.. _enb_advanced:

Advanced Usage
##############

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

.. 
  5G NR 
  ******
  
  The srsENB supports prototype 5G features for both NSA and SA modes of operation however, these features are no longer under active development. Instead we recommend the `srsRAN Project <https://docs.srsran.com/projects/project>`_, our ORAN-native 5G CU/DU solution.
  
  .. _5G_NSA: 
  
  5G NSA
  ======
  
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
  
  To enable a 5G NSA connection with srsENB you will need to modify the configuration files for srsENB. Namely, the *rr.conf* file, by enabling an NR secondary carrier for the existing eNB. This is covered in more detail in the relevant :ref:`app note<5g_nsa_zmq_appnote>` detailing how to use ZMQ to create an E2E 5G NSA network using  4G. 
  
  .. _5G_SA: 
  
  5G SA 
  ======
  
  5G SA, or 5G Standalone, is a 5G NR transmission mode that uses 5G cells for both control and data traffic. It also uses a full 5G Packet Core in place of a 4G EPC. This is considered to be end-to-end 5G, and removes the need for 
  4G LTE hardware to manage control traffic as seen in 5G NSA.  
  
  What is 5G SA Mode? 
  --------------------
  
  .. figure:: .imgs/5G_SA.png
    :align: center
  
  As shown in the above figure, 5G SA allows a 5G SA UE to connect to a 5G SA gNB, which is inturn connected to the 5G Core (namely the AMF and UPF) by the N2 and N3 interfaces. This UE has access to the full 5G SA network, and 
  full 5G data-plane and control-plane rates. Unlike 5G NSA which only allows the UE to use a 5G connection for its data-plane traffic.  
  
  Implementing 5G SA with srsENB
  -------------------------------
  
  
  To enable a 5G SA connection with srsENB you will need to modify the configuration files for srsENB. Much like for 5G NSA, a NR cell must be added to the *rr.conf* file. The difference for 5G SA is that all 
  4G LTE cells must be removed. 
  
  This is covered in more detail in the relevant :ref:`app note<5g_sa_e2e_appnote>` detailing how to use ZMQ to create an E2E 5G SA network using srsRAN 4G and Open5GS. 
