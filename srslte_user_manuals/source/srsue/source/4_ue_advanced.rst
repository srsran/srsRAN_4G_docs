.. _ue_advanced:

Advanced Usage
==============

MIMO
****

External USIM
*************

eMBMS
*****
Multimedia Broadcast Multicast Services (eMBMS) is the broadcast mode of LTE. Using eMBMS, an eNodeB can efficiently broadcast the same data to all users attached to the cell.


* Setup:

For the UE, the presence of an eMBMS transmission will be automatically detected from the SIBs and subsequently the MCCH present in the signal. To activate the service present in the UE, the following parameter is set::

  rrc.mbms_service_id = 0

Note if you set your service id to a value besides 0 in the eNodeB, use that number for this parameter too.

Additionally, there are also a number of settings that need to be altered to order to have good eMBMS functionality, specifically::

  phy.interpolate_subframe_enabled = true
  phy.sub_estim_alg = empty
  phy.nof_phy_threads = 2

Once all these configurations have been made, your network should be ready to run eMBMS.


* Usage:


Once you have run srsue with an eMBMS enabled eNodeB you should see an output like this at the terminal of the UE::


  Searching cell in DL EARFCN=3400, f_dl=2685.0 MHz, f_ul=2565.0 MHz
  Found Cell:  Mode=FDD, PCI=1, PRB=50, Ports=1, CFO=-0.0 KHz
  Found PLMN:  Id=00101, TAC=7
  Random Access Transmission: seq=20, ra-rnti=0x2
  Random Access Complete.     c-rnti=0x46, ta=1
  RRC Connected
  MBMS service started. Service id:0, port: 4321
  Network attach successful. IP: 172.16.0.2
  Software Radio Systems LTE (srsLTE)


the "MBMS service started. Service id:0, port: 4321" indicates the eMBMS service has successfully started.

To test it run the following:

At mbms gateway::

 sudo route add -net 239.255.1.0 netmask 255.255.255.0 dev sgi_mb
 iperf -u -c 239.255.1.1 -b 10M -T 64 -t 60

At the UE::

 sudo route add -net 239.255.1.0 netmask 255.255.255.0 dev tun_srsue
 iperf -s -u -B 239.255.1.1 -i 1


Traffic should make its way over the MBMS multicast link and arrive at the iperf server.


Carrier Aggregation
*******************

TDD
***



