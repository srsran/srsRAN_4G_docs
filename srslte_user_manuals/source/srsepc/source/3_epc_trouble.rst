.. _epc_trouble:

Troubleshooting
===============

UE did not attach
+++++++++++++++++

If the UE could not attach it is important to see at what point the attach procedure broke down.
The easiest way to do this is to inspect the NAS messages on the EPC PCAP.

In the subsections below, some instructions on how to troubleshoot the most common causes of attach failure and some instructions on how to resolve them can be found. 

Authentication failure
----------------------

The most common case of attach failure is authentication failure. In LTE, the UE must authenticate the network, and for that there are four important parameters that must be configured correctly both at the UE and the HSS.

Unkown UE
---------

Mismatched APN
--------------

UE can ping SPGW, but has no Internet access
++++++++++++++++++++++++++++++++++++++++++++

If the UE can ping the SPGW, that means that the attach procedure went well and that the UE was able to obtain the IP.

That means that not being able to access the Internet is a problem not with srsLTE, but with the networking configuration of the system.

IP forwarding
-------------

IP Masquerading
---------------

DNS not working
---------------
