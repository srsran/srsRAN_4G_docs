.. _enb_getstarted:

Getting Started
===============

To get started with srsENB you will require a PC with a GNU/Linux based operating system and an SDR RF front-end. An SDR RF front-end is a generic radio device such as the Ettus Research USRP that connects to your PC and supports transmission and reception of raw radio signals.

If you are using Ubuntu operating system, you can install srsENB from the binary packages provided::

  sudo add-apt-repository ppa:srslte/releases
  sudo apt-get update
  sudo apt-get install srsenb

If you are using a different distribution, you can install from source using the guide provided in the project's `GitHub page <https://github.com/srsLTE/srsLTE/>`_.

After installing the software you can install the configuration files into the default location (``~/.config/srslte``), by running::

  srslte_install_configs.sh user


Running the software
********************

To run srsENB with default parameters, run ``sudo srsenb`` on the command line. srsENB needs to run with sudo admin privileges in order to be able to create high-priority threads. Upon starting, srsENB will attempt to find your RF front-end device, attempt to attach to the core network (EPC) and start broadcasting.

Example console output::

    linux; GNU C++ version 6.3.0 20170618; Boost_106200; UHD_003.009.007-release
    Built in RelWithDebInfo mode using commit 6b2961fce on branch next.

    ---  Software Radio Systems LTE eNodeB  ---

    Reading configuration file /conf/enb.conf...
    Setting number of control symbols to 3 for 25 PRB cell.
    Opening USRP with args: type=b200,master_clock_rate=30.72e6
    Setting frequency: DL=2630.0 Mhz, UL=2510.0 MHz
    Setting Sampling frequency 5.76 MHz
    Enter t to stop trace.

    ==== eNodeB started ===

Upon receiving a UE connection::

    RACH:  tti=3381, preamble=3, offset=1, temp_crnti=0x46
    User 0x46 connected

With the eNodeB running and one or more UEs connected, type ``t`` in the console to enable the metrics trace. Example metrics trace::

    ------DL------------------------------UL----------------------------------
    rnti  cqi    ri   mcs  brate   bler   snr   phr   mcs  brate   bler    bsr
    46   14.1   2.0  25.1  28.4M   0.8%  24.8   0.0  23.1  9.60M   2.2%   140k
    46   14.8   2.0  26.6  30.7M     0%  24.9   0.0  23.2  9.92M     0%   140k
    46   14.7   2.0  26.3  30.1M   0.8%  24.9   0.0  23.1  9.90M     0%   140k
    46   14.8   2.0  26.5  30.6M     0%  24.9   0.0  23.1  9.90M     0%   140k
    46   15.0   2.0  26.7  30.9M     0%  24.8   0.0  23.1  9.83M     0%   140k
    46   14.5   2.0  26.1  30.0M     0%  24.9   0.0  23.1  9.88M     0%   140k
    46   14.8   2.0  26.3  30.3M     0%  24.8   0.0  23.1  9.84M     0%   140k
    46   14.7   2.0  26.4  30.4M     0%  24.9   0.0  23.1  9.89M     0%   140k
    46   14.7   2.0  26.4  30.4M     0%  24.9   0.0  23.2  9.91M     0%   140k
    46   14.7   2.0  26.3  30.4M     0%  24.9   0.0  23.1  9.87M     0%   140k
    46   14.8   2.0  26.4  30.4M     0%  24.9   0.0  23.1  9.88M     0%   140k


Configuration
*************

The eNodeb can be configured through the configuration file: ``enb.conf``. This configuration file provides parameters relating to the cell configuration, operating frequencies, transmit power levels, logging levels and much more. To run srsENB with the installed configuration file, use ``sudo srsenb ~/.config/srslte/enb.conf``.

All parameters specified in the configuration file can also be overwritten on the command line. For example, to run the eNodeB with a different EARFCN, use ``sudo srsenb ~/.config/srslte/enb.conf --rf.dl_earfcn 3350``.

In addition to the top-level configuration file, srsENB uses separate files to configure SIBs (sib.conf), radio resources (rr.conf) and data bearers (drb.conf). These additional configuration files are listed under [enb_files] in the top-level enb.conf and defaults are provided for each.

A key eNodeB parameter is enb.mme_addr, which specifies the IP address of the core network MME. The default configuration assumes that srsEPC is running on the same machine. For more information, as well instructions for using an EPC on a separate machine, see the EPC user manual.


Hardware Setup
**************

To use srsENB to create an over-the-air local cell, you will need an RF front-end and suitable antennas. The default EARFCN is 3400 (2565MHz uplink, 2865MHz downlink). To reduce TX-RX crosstalk, we recommend orienting TX and RX antennas at a 90 degree angle to each other.

The srsENB can also be used over a cabled connection. The cable configuration and required RF components will depend upon your RF front-end. For RF front-ends such as the USRP, connect TX to RX and ensure at least 30dB of attenuation to avoid damage to your devices. For more detailed information about cabled connections, see :doc:`Advanced Usage <4_enb_advanced>`.


Operating System Setup
**********************

The srsENB runs in user-space with standard linux kernels. For best performance, we recommend disabling CPU frequency scaling. To disable frequency scaling use::

  for f in /sys/devices/system/cpu/cpu[0-9]*/cpufreq/scaling_governor ; do
    echo performance > $f
  done




Observing results
*****************

To observe srsENB results, use the generated log files and packet captures.

Log files are created by default at /tmp/enb.log. The srsENB configuration file can be used to specify log levels for each layer of the network stack and to enable hex message output. Supported log levels are debug, info, warning, error and none.

Log messages take the following format::

    Timestamp  [Layer ]  Level    Content

e.g.::

    17:52:25.246 [RLC ]  Info    DRB1 Tx SDU

or with hex message output enabled::

    17:52:25.246 [RLC ]  Info    DRB1 Tx SDU
             0000: 8b 45 00 00 c7 f3 8b 40 00 01 11 d1 f6 c0 a8 03
             0010: 01 ef ff ff fa 92 55 07 6c 00 b3 ee 41 4d 2d 53

PHY-layer log messages have additional details::

    Timestamp  [Layer]	Level  [Subframe] Channel:  Content

e.g.::

    17:52:26.094 [PHY1]  Info  [05788]  PDSCH:    l_crb= 1, harq=0, snr=22.1 dB, CW0: tbs=55, mcs=22, rv=0, crc=OK, it=1, dec_time=  12 us


The srsENB application supports MAC layer packet captures. Packet capture (pcap) files can be viewed using Wireshark (www.wireshark.org). MAC layer captures are created by default at /tmp/enb.pcap and are encoded in compact mac-lte-framed form. To view in wireshark, edit the preferences of the DLT_USER dissector (add an entry with DLT=147, Payload Protocol=mac-lte-framed). For more information, see https://wiki.wireshark.org/MAC-LTE.


