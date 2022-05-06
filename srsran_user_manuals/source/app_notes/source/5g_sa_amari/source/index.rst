.. srsRAN 5G SA Application Note

.. _5g_sa_amari_appnote:

5G SA srsUE
############

Introduction
************

The 22.04 release of srsRAN brought 5G SA (Standalone) support to srsUE.
This application note shows how srsUE can be used with a third-party 5G SA network. In this example,
we use the Amari Callbox Classic from Amarisoft to provide the network.


Limitations
***********

The current 5G SA UE application has a few feature limitations that require certain configuration
settings at both the gNB and the core network. The key feature limitations are as follows:

  - Limited to 15 kHz Sub-Carrier Spacing (SCS), which means only TDD bands can be used. 
  - Limited to 10 MHz Bandwidth (BW) 


Hardware Requirements
*********************

For this application note, the following components are used:

  * Amari Callbox with 5G SA support as gNB and core
  * AMD Ryzen5 3600X Linux PC as UE compute platform
  * Ettus Research USRP X310 connected over 10GigE as UE RF front-end

The Amari Callbox is an LTE/NR SDR-based UE test solution from Amarisoft.
It contains an EPC, a 5GC, an eNodeB, a gNodeB, an IMS server, an 
eMBMS server and an Intel i7 Linux PC with PCIe SDR cards. The gNodeB is release 15 compliant and 
supports both NSA and SA modes. A further outline of the specifications can be found in the 
`data sheet <https://www.amarisoft.com/app/uploads/2020/02/AMARI-Callbox-Classic.pdf>`_.
This test solution was chosen as it's widely available, easily configurable, and user-friendly.


Hardware Setup
**************

Tests may be carried out over-the-air or using a cabled setup.
For this example, we use a cabled setup between the UE and the eNB/gNB (i.e from the X310 to the PCIe SDR cards 
on the Callbox). These connections run through 30dB attenuators as shown in the figure above. The 
PPS inputs for the accurate clocking of both the UE and Callbox are also shown.
Both UE and Callbox require accurate clocks - in our testing we provide PPS inputs to both.



Configuration
*************

To set-up and run the 5G SA network and UE, the configuration files for both the 
Callbox and srsUE must be changed.

All of the modified configuration files have been included as attachments to this App Note. It is 
recommended you use these files to avoid errors while changing configs manually. Any configuration
files not included here do not require modification from the default settings.

UE files: 

  * :download:`UE config example <.config/ue.conf>`

Callbox files:

  * :download:`gNB SA config <.config/amarisoft_enb.cfg>`


srsUE
=====

The following changes need to be made to the UE configuration file to allow it to connect to 
the Callbox in SA mode. 

Firstly the following parameters need to be changed under the **[rf]** options so that the 
X310 is configured optimally:: 

  [rf]
  tx_gain = 3
  freq_offset = 0

  nof_antennas = 1

  srate = 11.52e6

  device_name = uhd
  device_args = type=x300,serial=30B8658,clock=external,sampling_rate=23.04e6,lo_freq_offset_hz=23.04e6,None

The next set of changes need to be made to the **[rat.eutra]** options. The LTE carrier is disabled, to force the UE to use a 5G NR carrier:: 

  [rat.eutra]
  dl_earfcn = 2850
  nof_carriers = 0

Finally the **[rat.nr]** options need to be configured for 5G SA mode operation:: 

  [rat.nr]
  nof_carriers = 1
  bands = 3


Callbox
=======

The *amarisoft_enb.cfg* file is responsible for the configuration of the gNB needed for a 5G SA network. 

The main changes to the default config are as follows: 

  - Enable NR support
  - Enable NR cell and configure NR cell
  - Modify the PRACH configuration
  - Modify the PUCCH configuration 

Enable NR Support
-----------------

This is done on line 47. by setting the corresponding flag to true:: 

  nr_support: true,
  
NR Cell
-------

Firstly the Band and ARFCN must be set. This is done on lines 61 and 62:: 

  nr_cell_list: [
  {
    rf_port: 0,
    cell_id: 1,
    band: 3,
    dl_nr_arfcn: 368500,
  },

  ],

The ``band`` and ``dl_nr_afcn`` are chosen based on the known limitations of srsRAN. 

Next, the SCS, BW and other configuration parameters can be changed from line 68:: 

  nr_cell_default: {
    subcarrier_spacing: 15, /* kHz */
    ssb_subcarrier_spacing: 15, // only supported in FDD bands
    bandwidth: 10, /* MHz */
    n_antenna_dl: 1,
    n_antenna_ul: 1,


    ssb_pos_bitmap: "1000",

    ssb_period: 10, /* in ms */
    n_id_cell: 500,

Here the ``subcarrier_spacing`` is set to 15 KHz and the ``bandwidth`` to 10 MHz, the ``n_antenna_dl`` is set to 1 and the ``ssb_period`` is set to 10.

PRACH
-----

For the PRACH config options (line 105) the following is used:: 

  prach: {
    prach_config_index: 0,
    msg1_fdm: 1,
    msg1_frequency_start: 1,
    zero_correlation_zone_config: 0,
    preamble_received_target_power: -110, /* in dBm */
    preamble_trans_max: 7,
    power_ramping_step: 4, /* in dB */
    ra_response_window: 10, /* in slots */
    restricted_set_config: "unrestricted_set",
    ra_contention_resolution_timer: 64, /* in ms */
    ssb_per_prach_occasion: 1,
    cb_preambles_per_ssb: 8,
  },

The changes made to the above include the setting of ``prach_config_index`` to 0, setting ``msg1_frequency_start`` to 1 and setting ``ra_response_window`` to 10. 

PUCCH
-----

Lastly, the PUCCH config must be changed. This is done from line 353:: 

  pucch: {
    pucch_group_hopping: "neither",
    hopping_id: -1, /* -1 = n_cell_id */
    p0_nominal: -90,
      pucch1: {
        n_cs: 3,
        n_occ: 3,
        freq_hopping: false,
      },
      pucch2: {
        n_symb: 2,
        n_prb: 1,
        freq_hopping: false,
        simultaneous_harq_ack_csi: false, 
        max_code_rate: 0.25,
      },
  },

The only change here is that ``freq_hopping`` is set to false in both pucch1 and pucch2. 

The gNB is now configured correctly. All other config files associated with the gNB and 5GC can be left in their default states.

Running the Network
*******************

The following order should be used when running the network: 

	1. 5GC
	2. gNB
	3. UE

5GC
=====

To run the 5GC the following command is used:: 
	
	sudo ltemme mme.cfg
	
gNB
=====

Next the eNB/ gNB should be instantiated, using the following command:: 
	
	sudo lteenb gnb-nsa.cfg
	
Console output should be similar to:: 

	Base Station version 2021-03-15, Copyright (C) 2012-2021 Amarisoft

  RF0: sample_rate=61.440 MHz dl_freq=1836.740 MHz ul_freq=1741.740 MHz (band n3) dl_ant=1 ul_ant=1
	
UE
=====

To run the UE, use the following command:: 

	sudo srsue ue.conf

Once the UE has been initialized you should see the following:: 

	Opening 1 channels in RF device=uhd with args=type=x300,serial=30B8658,clock=external,sampling_rate=23.04e6,lo_freq_offset_hz=23.04e6,None
	
This will be followed by some information regarding the USRP. Once the cell has been found successfully you should see the following:: 

  Found Cell:  Mode=FDD, PCI=1, PRB=50, Ports=1, CFO=0.1 KHz
  Found PLMN:  Id=00101, TAC=7
  Random Access Transmission: prach_occasion=0, preamble_index=0, ra-rnti=0xf, tti=3851
  Random Access Complete.     c-rnti=0x4601, ta=3
  RRC Connected
  RRC NR reconfiguration successful.
  PDU Session Establishment successful. IP: 192.168.4.2
  RRC NR reconfiguration successful.

To confirm the UE successfully connected, you should see the following on the console output of the **gNB**:: 

  PRACH: cell=01 seq=0 ta=3 snr=29.1 dB


Console Trace
*************

srsUE
=====

The following is an example console trace output when running bi-direction traffic with iPerf3:: 

  ---------Signal-----------|-----------------DL-----------------|-----------UL-----------
  rat  pci  rsrp   pl   cfo | mcs  snr  iter  brate  bler  ta_us | mcs   buff  brate  bler
   nr  500    -3    0   2.0 |  27   28   2.0    23M    0%    0.0 |  27     59    16M    0%
   nr  500    -3    0   1.6 |  27   28   2.1    23M    0%    0.0 |  27    30k    16M    0%
   nr  500    -3    0   2.0 |  27   28   2.1    23M    0%    0.0 |  27    44k    16M    0%
   nr  500    -3    0  824m |  27   28   2.1    23M    0%    0.0 |  27    26k    16M    0%
   nr  500    -3    0   1.1 |  27   28   2.1    23M    0%    0.0 |  27    10k    17M    0%
   nr  500    -3    0   1.3 |  27   28   2.0    23M    0%    0.0 |  27    0.0    16M    0%
   nr  500    -3    0  106m |  27   28   2.0    23M    0%    0.0 |  27   118k    16M    0%
   nr  500    -4    0   1.0 |  27   28   2.1    22M    0%    0.0 |  27    52k    21M    0%
   nr  500    -4    0   1.9 |  27   28   2.0    22M    0%    0.0 |  27    57k    21M    0%
   nr  500    -3    0  840m |  27   28   2.0    23M    0%    0.0 |  27    54k    19M    0%
   nr  500    -3    0  160m |  27   28   2.0    23M    0%    0.0 |  27    20k    18M    0%

To read more about the UE console trace metrics, see the :ref:`UE User Manual <ue_commandref>`.

Amarisoft gNB
=============

The following console output is shown on the gNB for the same period:: 

                 ----DL----------------------- --UL------------------------------------------------
  UE_ID  CL RNTI C cqi ri  mcs retx txok brate  snr puc1  mcs rxko rxok brate     #its phr  pl   ta
      1 001 4601 1  15  1 27.9    0 1472 22.6M 39.5   -  27.9    0 1022 18.7M  1/1.9/3   -   -  0.3
      1 001 4601 1  15  1 27.9    0 1476 22.7M 39.3   -  27.9    0  987 17.8M  1/1.9/3   -   -  0.3
      1 001 4601 1  15  1 27.9    0 1512 23.1M 36.3   -  27.9    0  908 15.7M  1/1.9/3   -   -  0.3
      1 001 4601 1  15  1 27.9    0 1474 22.6M 38.0   -  27.9    0  977 17.1M  1/1.9/3   -   -  0.3
      1 001 4601 1  15  1 27.9    0 1488 22.8M 46.6   -  27.9    0  929 16.3M  1/1.9/3   -   -  0.3
      1 001 4601 1  15  1 27.9   28 1427 21.9M 38.0   -  27.9    0 1035 19.1M  1/1.9/3   -   -  0.2
      1 001 4601 1  15  1 27.9    5 1428 21.9M 39.8   -  28.0    0 1113 21.3M  1/1.9/3   -   -  0.2
      1 001 4601 1  15  1 27.9    3 1416 21.7M 38.2   -  28.0    0 1159 22.4M  1/1.9/3   -   -  0.2
      1 001 4601 1  15  1 27.9    0 1395 21.4M 38.7   -  28.0    0 1222 24.7M  1/2.0/3   -   -  0.2
      1 001 4601 1  15  1 27.9    0 1405 21.6M 39.0   -  28.0    0 1182 23.3M  1/2.0/3   -   -  0.2

	
