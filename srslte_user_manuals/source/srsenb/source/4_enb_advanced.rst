.. _enb_advanced:

Advanced Usage
==============

MIMO
****

.. warning::

  TBA

eMBMS
*****

Multimedia Broadcast Multicast Services (eMBMS) is the broadcast mode of LTE. Using eMBMS, an eNodeB can efficiently broadcast the same data to all users attached to the cell.


* Setup:

The running of eMBMS requires an additional network component, specifically the eMBMS gateway. This network component provides the data to the eMBMS bearer in the eNodeB. It can be run as follows::

  sudo ./srsmbms ~/.config/srslte/mbms.conf


At the eNodeB, eMBMS requires a few different configurations in order to properly introduce eMBMS to the transmission. First, instead of using the default sib.conf.example, the alternative sib.conf.mbsfn.example should be used. This version of the sib configuration will use both SIB2 and the eMBMS specific SIB 13 to set:

   * eMBMS subframe allocation
   * MCCH scheduling period
   * MCCH modulation order
   * non eMBMS subframe region length
   * eMBMS area id
   * MCCH subframe allocation
   * MCCH repetition period

In addition to using the eMBMS sib configuration file, a number of configurations must be changed in the enb.conf.example specifically::

  expert.enable_mbsfn = true
  scheduler.nof_ctrl_symbols = 2
  expert.nof_phy_threads = 2

Once all these setting adjustments have been made, the eNodeB should be ready to run in eMBMS mode.

To test you will need to attach an eMBMS compatible UE.

* Usage:


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

.. warning::


  TBA


