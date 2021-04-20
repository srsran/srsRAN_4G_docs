.. srsRAN eMBMS Application Note

.. _embms_appnote:

eMBMS Application note
===========================


Introduction
************

`enhanced Multimedia Broadcast Multicast Services (eMBMS) <https://www.sharetechnote.com/html/Handbook_LTE_MBSFN.html>`_
is the broadcast mode of LTE. Using eMBMS, an eNodeB can efficiently broadcast the same data to all users attached to the cell.
srsRAN supports eMBMS in the end-to-end system including srsUE, srsENB and srsEPC. In addition to these, a new application
is introduced - srsMBMS. srsMBMS is the SRS MBMS gateway, an additional network component which receives multicast data on
a TUN virtual network interface and provides it to the eMBMS bearer in the eNodeB.


Setup
*****

To run an end-to-end srsRAN system with eMBMS, some additional configuration of the srsENB and srsUE applications are required.
In the sample configurations provided, it is assumed that srsmbms, srsepc and srsenb run on the same physical machine.

srsENB configuration
--------------------

At the eNodeB, additional configuration is required in order to support eMBMS transmission. First, instead of using the default ``sib.conf.example``, the alternative ``sib.conf.mbsfn.example`` should be used. This version of the sib configuration adds eMBMS
parameters to SIB2 and includes SIB 13 which is specific to eMBMS. These SIB modifications define the following key eMBMS network
parameters:

   * eMBMS Subframe Allocation
   * MCCH Scheduling Period
   * MCCH Modulation Order
   * Non-eMBMS Subframe Region Length
   * eMBMS Area Id
   * MCCH Subframe Allocation
   * MCCH Repetition Period

In addition to using the eMBMS SIB configuration file, a number of further configurations must be changed in the ``enb.conf``::

  [enb_files]
  sib_config = sib.conf.mbsfn

  [embms]
  enable = true

  [scheduler]
  min_nof_ctrl_symbols = 2
  max_nof_ctrl_symbols = 2

  [expert]
  nof_phy_threads = 2

Once these setting adjustments have been made, the eNodeB should be ready to run in eMBMS mode.

srsUE configuration
--------------------

For the UE, the presence of an eMBMS transmission will be automatically detected from the SIBs and the MCCH present in the downlink signal. To receive an active eMBMS service, the following parameter must be set in ``ue.conf``::

  [rrc]
  mbms_service_id = 0

Note this service id must match the service id in use by the network.

In addition, we recommend the following settings for best performance with eMBMS::

  [phy]
  interpolate_subframe_enabled = true
  snr_estim_alg = empty
  nof_phy_threads = 2

Once these configurations have been made, your UE should be ready to run eMBMS.


Usage
*****

First, run srsMBMS (the MBMS gateway), srsEPC and srsENB on the same machine:

``sudo ./srsmbms ~/.config/srsRAN/mbms.conf``

``sudo ./srsepc ~/.config/srsRAN/epc.conf``

``sudo ./srsenb ~/.config/srsRAN/enb.conf``

The MBMS gateway will create a TUN interface to which all traffic intended for multicast should be written. It will then forward this traffic to the eNodeB via a seperate GTPU tunnel that is dedicated to eMBMS traffic.


To test eMBMS with srsMBMS, srsEPC and srsENB, we can use `Iperf <https://en.wikipedia.org/wiki/Iperf>`_. At the MBMS gateway, create a route and start downlink traffic:

``sudo route add -net 239.255.1.0 netmask 255.255.255.0 dev sgi_mb``

``iperf -u -c 239.255.1.1 -b 10M -T 64 -t 60``


Next, we can run srsUE on a separate machine to receive the eMBMS data:

``sudo ./srsue ~/.config/srsRAN/ue.conf``

 Upon running srsUE with an eMBMS enabled eNodeB you should see the following output at the terminal of the UE::


  Searching cell in DL EARFCN=3400, f_dl=2685.0 MHz, f_ul=2565.0 MHz
  Found Cell:  Mode=FDD, PCI=1, PRB=50, Ports=1, CFO=-0.0 KHz
  Found PLMN:  Id=00101, TAC=7
  Random Access Transmission: seq=20, ra-rnti=0x2
  Random Access Complete.     c-rnti=0x46, ta=1
  RRC Connected
  MBMS service started. Service id:0, port: 4321
  Network attach successful. IP: 172.16.0.2
  Software Radio Systems LTE (srsRAN)


the *MBMS service started. Service id:0, port: 4321* indicates the eMBMS service has successfully started.

To receive the multicast iperf data, add a route to the UE and start an iperf server:

``sudo route add -net 239.255.1.0 netmask 255.255.255.0 dev tun_srsue``

``iperf -s -u -B 239.255.1.1 -i 1``
