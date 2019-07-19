.. _epc_advanced:

Advanced Usage
==============

eMBMS
*****

The running of eMBMS requires an additional network component, specifically the MBMS gateway. This network component provides the data to the eMBMS bearer in the eNodeB. The srsLTE software suite includes an MBMS gateway within srsEPC. To run the SRS eMBMS gateway, use::

  sudo ./srsmbms ~/.config/srslte/mbms.conf


This will create a tun interface to which all traffic intended for multicast should be written. It will then forward this traffic to a seperate GTPU tunnel that is dedicated to eMBMS traffic.


Usage:
------

The MBMS-GW must be used in conjunction with eMBMS enabled eNodeB and UE as well as an EPC. Once it is connected, traffic can be written to it as follows::


 sudo route add -net 239.255.1.0 netmask 255.255.255.0 dev sgi_mb
 iperf -u -c 239.255.1.1 -b 10M -T 64 -t 60


using `Iperf <https://en.wikipedia.org/wiki/Iperf>`_. as a network traffic generator.




