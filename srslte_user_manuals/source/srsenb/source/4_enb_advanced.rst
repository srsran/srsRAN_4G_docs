.. _enb_advanced:

Advanced Usage
==============

eMBMS
*****

`Multimedia Broadcast Multicast Services (eMBMS) <https://www.sharetechnote.com/html/Handbook_LTE_MBSFN.html>`_ is the broadcast mode of LTE. Using eMBMS, an eNodeB can efficiently broadcast the same data to all users attached to the cell.


Setup:
------

The running of eMBMS requires an additional network component, specifically the MBMS gateway. This network component provides the data to the eMBMS bearer in the eNodeB. The srsLTE software suite includes an MBMS gateway within srsEPC. To run the SRS MBMS gateway, use::

  sudo ./srsmbms ~/.config/srslte/mbms.conf


At the eNodeB, eMBMS requires a few different configurations in order to properly introduce eMBMS to the transmission. First, instead of using the default ``sib.conf.example``, the alternative ``sib.conf.mbsfn.example`` should be used. This version of the sib configuration will use both SIB2 and the eMBMS specific SIB 13 to set:

   * eMBMS Subframe Allocation
   * MCCH Scheduling Period
   * MCCH Modulation Order
   * Non-eMBMS Subframe Region Length
   * eMBMS Area Id
   * MCCH Subframe Allocation
   * MCCH Repetition Period

In addition to using the eMBMS SIB configuration file, a number of configurations must be changed in the enb.conf.example::

  expert.enable_mbsfn = true
  scheduler.nof_ctrl_symbols = 2
  expert.nof_phy_threads = 2

Once all of these setting adjustments have been made, the eNodeB should be ready to run in eMBMS mode.

To test you will need to attach an eMBMS compatible UE such as srsUE.

Usage:
------

To test eMBMS with srsENB and the SRS MBMS gateway, we can use `Iperf <https://en.wikipedia.org/wiki/Iperf>`_. At the MBMS gateway, create a route and start downlink traffic::

 sudo route add -net 239.255.1.0 netmask 255.255.255.0 dev sgi_mb
 iperf -u -c 239.255.1.1 -b 10M -T 64 -t 60

If using srsUE, add a route and start the iperf server::

 sudo route add -net 239.255.1.0 netmask 255.255.255.0 dev tun_srsue
 iperf -s -u -B 239.255.1.1 -i 1


Traffic should make its way over the MBMS multicast link and arrive at the iperf server.


MIMO
****

.. warning::

  TBA


Carrier Aggregation
*******************

.. warning::


  TBA


