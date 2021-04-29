.. _ue_getstarted:

Getting Started
===============

To get started with srsUE you will require a PC with a GNU/Linux based operating system and an SDR RF front-end. An SDR RF front-end is a generic radio device such as the Ettus Research USRP that connects to your PC and supports transmission and reception of raw radio signals.

If you are using Ubuntu operating system, you can install srsUE from the binary packages provided::

  sudo add-apt-repository ppa:srslte/releases
  sudo apt-get update
  sudo apt-get install srsue

If you are using a different distribution, you can install from source using the guide provided in the project's `GitHub page <https://github.com/srsRAN/srsRAN/>`_.

After installing the software you can install the configuration files into the default location (``~/.config/srsran``), by running::

  srsran_install_configs.sh user


Running the software
********************

To run srsUE with default parameters, run ``sudo srsue`` on the command line. srsUE needs to run with sudo admin privileges in order to be able to create high-priority threads and to create a TUN device upon successful network attach. Upon starting, srsUE will attempt to find your RF front-end device and connect to a local cell.

If srsUE successfully attaches to a local network, it will start a TUN interface ``tun_srsue``. The TUN interface can be used as any other network interface on your PC, supporting data traffic to and from the network.

Example console output for a successful network attach::

    linux; GNU C++ version 6.3.0 20170618; Boost_106200; UHD_003.009.007-release
    Reading configuration file /.config/srsran/ue.conf...
    Built in RelWithDebInfo mode using commit 6b2961fce on branch next.

    Opening 1 RF devices with 2 RF channels...
    Opening USRP with args: type=b200,master_clock_rate=30.72e6
    Waiting PHY to initialize ... done!

    Attaching UE...
    Searching cell in DL EARFCN=2850, f_dl=2630.0 MHz, f_ul=2510.0 MHz
    Found Cell:  Mode=FDD, PCI=1, PRB=6, Ports=2, CFO=1.3 KHz
    Found PLMN:  Id=00101, TAC=7
    Random Access Transmission: seq=42, ra-rnti=0x2
    RRC Connected
    Random Access Complete.     c-rnti=0x46, ta=0
    Network attach successful. IP: 192.168.3.2

With the UE attached to the network, type ``t`` in the console to enable the metrics trace. Example metrics trace::

    ----Signal--------------DL-------------------------------------UL----------------------
    cc  rsrp    pl    cfo   mcs   snr turbo  brate   bler   ta_us  mcs   buff  brate   bler
     0   -77    77   1.2k    24    33  0.84   5.8M     0%   0.0    18   193k   624k     0%
     0   -77    77   1.2k    24    31  0.80   5.7M     0%   0.0    18   193k   631k     0%
     0   -77    77   1.2k    24    32  0.80   5.8M     0%   0.0    18   192k   633k     0%
     0   -77    77   1.2k    25    34  0.93   6.0M     0%   0.0    18   194k   636k     0%
     0   -77    77   1.2k    24    33  0.83   5.8M     0%   0.0    19   193k   632k     0%
     0   -77    77   1.2k    24    31  0.82   5.8M     0%   0.0    18   194k   632k     0%
     0   -77    77   1.2k    24    32  0.82   5.8M     0%   0.0    18   193k   635k     0%
     0   -77    77   1.2k    25    34  0.91   6.0M     0%   0.0    18   194k   629k     0%
     0   -77    77   1.2k    24    33  0.85   5.8M     0%   0.0    19   193k   634k     0%
     0   -77    77   1.2k    24    31  0.82   5.7M     0%   0.0    19   194k   647k     0%
     0   -77    77   1.2k    24    32  0.84   5.8M     0%   0.0    18   192k   629k     0%


.. _ueConfig:

Configuration
*************

The UE can be configured through the configuration file: ``ue.conf``. This configuration file provides parameters relating to operating frequencies, transmit power levels, USIM properties, logging levels and much more. To run srsUE with the installed configuration file, use ``sudo srsue ~/.config/srsran/ue.conf``.

All parameters specified in the configuration file can also be overwritten on the command line. For example, to run the UE with a different EARFCN, use ``sudo srsue ~/.config/srsran/ue.conf --rf.dl_earfcn 3350``.

By default, srsUE uses a virtual USIM card, with parameters from ``ue.conf``. These parameters are:

  - ALGO - the authentication algorithm to use (MILENAGE or XOR)
  - IMSI - the unique identifier of the USIM
  - K - the secret key shared with the HSS in the EPC
  - OP or OPc - the Operator Code (only used with MILENAGE algorithm)

To connect successfully to a network, these parameters will need to match those in the HSS of the EPC. MILENAGE is the algorithm used in most networks, the XOR algorithm is used primarily by test equipment and test USIM cards. OP is the network-wide operator code and OPc is the USIM-specific encrypted operator code - both are supported by srsUE.


Hardware Setup
**************

To use srsUE to connect over-the-air to a local network, you will need an RF front-end and suitable antennas. The default EARFCN is 3400 (2565MHz uplink, 2685MHz downlink). To reduce TX-RX crosstalk, we recommend orienting TX and RX antennas at a 90 degree angle to each other.

The srsUE can also be used over a cabled connection. The cable configuration and required RF components will depend upon your RF front-end. For RF front-ends such as the USRP, connect TX to RX and ensure at least 30dB of attenuation to avoid damage to your devices. For more detailed information about cabled connections, see :doc:`Advanced Usage <4_ue_advanced>`.


Operating System Setup
**********************

The srsUE runs in user-space with standard linux kernels. For best performance, we recommend disabling CPU frequency scaling. To disable frequency scaling use::

  for f in /sys/devices/system/cpu/cpu[0-9]*/cpufreq/scaling_governor ; do
    echo performance > $f
  done


Observing results
*****************

To observe srsUE results, use the generated log files and packet captures.

Log files are created by default at /tmp/ue.log. The srsUE configuration file can be used to specify log levels for each layer of the network stack and to enable hex message output. Supported log levels are debug, info, warning, error and none.

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


The srsUE application supports packet capture at two levels - MAC layer and NAS layer. MAC layer captures include both control and data traffic and will be encrypted if configured by the network. NAS layer captures include control traffic only and will not be encrypted. Packet capture (pcap) files can be viewed using Wireshark (www.wireshark.org).

See the explanation :ref:`here <wireshark>` on setting up wireshark to decdode pcaps.  
