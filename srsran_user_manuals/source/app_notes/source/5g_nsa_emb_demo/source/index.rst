.. Embedded 5G NSA DL Demonstration System Application Note

.. _5g_nsa_emb_demo_appnote:

Embedded 5G NSA UE DL Demonstration System Application Note
===========================================================

Introduction
************

This appnote describes the main aspects of the Embedded NSA Demonstration system, consisting of a DL-only
NSA UE implementation (i.e., 4G sync + DL NR PHY) on the RFSoC platform.

First, an overview of both the utilized laboratory setup and main demonstration goals is provided. Then,
the required steps to implement the described laboratory setup are provided (i.e., from configuring the
ZCU111 prototyping board as required, to the list of console commands used to control the system).

DL Demonstration System Overview
********************************

.. image:: .imgs/5g_nsa_emb_demo_lab_setup.png
		:align: center

Hardware Requirements
---------------------

As shown in the figure above, the main components of the Embedded NSA DL demonstration system are listed below:

  * **ZCU111 prototyping platform**: hosts the RFSoC device, which will implement the embedded NSA SRS UE demo system. The latter includes the 4G sync (PSS and SSS detection) and the DL NR PHY (FFT, channel estimation and PDCCH/PDSCH).
  * **XM500 daughterboard**: this FMC balun converter board is plugged onto the ZCU111 and provides external access to the ADCs/DACs in the RFSoC.
  * **X300 USRP**: high-performance FPGA-based SDR front-end, including two complete RF chains and 10GE connectivity for high-speed I/Q sample exchange. It will constitute the NSA SRS eNB front-end.
  * **x86 host #0**: will host the NSA SRS eNB transmitter to provide both 4G and 5G DL signals.
  * **x86 host #1**: will provide SSH access to the ZCU111 board, in order to control the embedded NSA SRS UE. Will also display run-time DL metrics.

Hardware Setup
--------------

The connection between the different components comprising the demos system is as follows:

  * The X300 will be directly cabled with the XM500. Note that the latter does not include RF gain/filtering components, but enables a cabled setup via the onboard SMA connectors (comes equipped with suitable external filters). Additionally, a common 10 MHz reference signal will be shared between them (e.g., octoclock).
  * The x300 will be interfaced to the x86 host #0 via 10GE.
  * Both x86 host #1 and the ZCU111 will be connected to the same LAN (Ethernet), which will enable the host to access (SSH) the ZCU111 and interact with the embedded ARM (RFSoC).

DL Demonstration Goals and Reach
********************************

The demo aims at providing a proof-of-concept of the capacity of the RFSoC to host an SDR-based embedded
NR UE implementation. With this purpose in mind, PHY-layer test NSA NR UE and eNB applications have been
developed (i.e, they are not fully featured applications, as they are basically implementing the DL
functionality). Nevertheless, its SDR implementation will enable the user to modify the specific configuration
of the 4G and 5G DL signals (e.g., number of PRBs, mcs) and observe the effect of these on the performance
metrics provided by the embedded UE (i.e., console outputs).

Limitations
-----------

The most obvious limitation is that the UE and gNB applications, as well as the FPGA-accelerated PHY-layer
implementation, are not fully-featured, as their scope is limited to the DL functionality (i.e., no UL
processing will be implemented as part of the DL demonstration).

The lack of a complete RF front-end also introduces the following limitations:

	* A cabled setup is required, as no gain and/or RF filtering components are included in the XM500 daughter-board (beyond those baseline features provided by the HF/LF baluns). Consequently, no AGC functionalities are implemented.
	* The center frequencies supported by the specific hardware setup being utilized are constrained to the 10-2500 MHz range **TBD:(we've mainly tested 2400 MHz)**. **DELETE?** Moreover, center frequency must be multiple of sampling rate.
	* **TBD:** Use of a Tx gain between X and Y is advised in the gNB side. (TABLE DEPENDING ON BW? e.g., 100 PRB might need lower)

The embedded 5G NSA UE implementation inherits those feature limitations of its x86 counterpart. Whereas
this is transparent to the user (i.e., both gNB and UE applications are provided by SRS), a list of key
feature limitations is provided below for the sack of thoroughness:

  * 4G and NR carrier need to use the same subcarrier-spacing (i.e. 15 kHz) and bandwidth (**TBD: current bitstream supports 5, 10 and 20 MHz**)
  * **RELEVANT?** Support for NR in TDD mode for sub-6Ghz (FR1) in unpaired spectrum
  * **VERIFY** Only DCI formats 1_0 and 1_1 (Downlink) supported
  * No cell search and reference signal measurements (NR carrier PCI needs to be known)

Configuration
*************

srsUE (ZCU111 setup)
--------------------

*Use of an external reference signal in the ZCU111*

The use of an external 10 MHz reference signal ensures the accuracy of the system clock, which will
also be shared with the gNB. In order to enable the use of an external reference in the ZCU111 board,
the following actions are required:

  1. Disconnect the jumper in *J110* to power-off the 12.8 MHz TXCO that is connected by default to *CLKin0* of the LMK04208 PLL used to generate the ADC/DAC reference clocks in the ZCU111.
  2. Connect a 10 MHz clock reference to the *J109* SMA port in the ZCU111 (e.g., cabled output from octoclock).

.. image:: .imgs/zcu111_J109_J100_config.png
		:align: center

Note, that some modifications are also required in the software end. Nevertheless, the srsUE DL Demo
application is already including them. The full details are provided in the code repository (see the
*RFdc timestamping IP section in /lib/src/phy/ue/fpga_ue/RFdc_timestamping*).

*XM500 port usage*

As per FPGA design (i.e., fixed in the demonstration bistream), a specific set of connectors needs
to be used in the XM500 daughter-board, as indicated below:

	* The 4G DL signal shall be received from ADC Tile 224, channel 1 (labelled as **ADC224_T0_CH1** in the board).
	* The NR DL signal shall be received from ADC Tile 224, channel 0 (labelled as **ADC224_T0_CH0** in the board).

Moreover, the external DC-2500 MHz low-pass filters (**VLFX-2500+**) shipped alongisde the XM500 needs to be
placed between the cables coming from the gNB and the SMA connectors in the XM500, as shown below.

.. image:: .imgs/zcu111_external_filter_detail.png
		:align: center

*SD card*

The bitstream and binaries implementing the embedded NSA DL UE are hosted in an SD card, which is
organized as detailed below:

	* **BOOT partition**: includes the demonstration boot image (*BOOT.BIN*), which groups the FPGA bistream and boot binaries, the Petalinux and the device tree.
	* **rootfs partition**: includes the root file system, which contains the user applications (e.g., srsUE).

A ready to use image of the SD card used by the Demonstration System is made available below, with all
required contents:

* :download:`emb_nsa_ue_dl_demo_sd_card.img <https://shared-folder.com/emb_nsa_ue_dl_demo_sd_card.img>`

Run the following command to write it to a new SD card::

  sudo pv -tpreb emb_nsa_ue_dl_demo.img | sudo dd of=/dev/sdb bs=32M conv=fsync

In any case, the instructions to build an SD card from scratch are fully covered in the code repository
(see	*lib/src/phy/ue/fpga_ue/srsRAN_RFSoC.md*).

srsgNB (X300 & host #0 setup)
-----------------------------

*Shared reference signal with the ZCU111*

Connect the same 10 MHz reference signal source (e.g., octoclock) used with the ZCU111 in the *REF IN*
port. The use of the counterpart PPS input remains optional.

*X300 port usage*

As in the FPGA case, the utilization of the two RF ports in the X300 is predefined in the srsgNB
application, as indicated below:

	* The 4G DL signal will be transmitted from RF channel A, TX/RX port.
	* The NR DL signal will be transmitted form RF channel B, TX/RX port.

Accordingly, each DL signal will be connected to the other end of the external RF filter of the
counterpart receive ADC channel in the XM500 daugther-board.

*UHD version*

The Embedded NSA UE demonstration system has been tested by using version *3.15.0.0-62-g7a3f1516*
of the UHD driver. The following script (or a customized variation) might prove quite helpful to
automate the x300 initialization procedure::

	#!/bin/sh
	# Setup parameters
	export UHD_INSTALL_PATH=/usr/local/
	#export UHD_VERSION=3.15
	export VIVADO=/opt/Xilinx/Vivado_Lab/2019.2/bin/vivado_lab

	# Setup network interface
	sudo ifconfig enp3s0f0 192.168.40.1 mtu 9000

	# Export UHD RFNOC paths (available versions 4.0, 3.15.LTS)
	export UHD_RFNOC_DIR=$UHD_INSTALL_PATH/share/uhd/rfnoc/
	export LD_LIBRARY_PATH=$UHD_INSTALL_PATH/lib

	# Setup kernel parameters for best X300 performance
	sudo sysctl -w net.core.wmem_max=24862979
	sudo sysctl -w net.core.rmem_max=24862979

	# Load FPGA with VIVADO
	cat << EOM >/tmp/load-x300.tcl
	open_hw_manager
	connect_hw_server -allow_non_jtag
	open_hw_target {localhost:3121/xilinx_tcf/Digilent/2516351B0A87A}
	current_hw_device [get_hw_devices xc7k325t_0]
	refresh_hw_device -update_hw_probes false [lindex [get_hw_devices xc7k325t_0] 0]
	set_property PROGRAM.FILE {$UHD_INSTALL_PATH/share/uhd/images/usrp_x300_fpga_XG.bit} [get_hw_devices xc7k325t_0]
	set_property PROBES.FILE {} [get_hw_devices xc7k325t_0]
	set_property FULL_PROBES.FILE {} [get_hw_devices xc7k325t_0]
	program_hw_devices [get_hw_devices xc7k325t_0]
	refresh_hw_device [lindex [get_hw_devices xc7k325t_0] 0]
	close_hw_manager
	EOM
	$VIVADO -mode batch -source /tmp/load-x300.tcl

	echo "Done!"

*eNB/gNB configuration file*

To set-up the 5G NSA DL signal, the configuration file for both the srsgNB application must be
changed. In more detail, all NR parameters of interest to the demonstration system will be set
through the configuration file.

A few example configuration files have been included as attachments to this App Note. It is
recommended you use these files for testing as your starting point.

eNB/gNB configuration files:

  * **TBD** :download:`eNB/gNB 25 PRB configuration example <enb.25prb.conf.example>`
	* **TBD** :download:`eNB/gNB 52 PRB configuration example <enb.52prb.conf.example>`
	* **TBD** :download:`eNB/gNB 106 PRB configuration example <enb.106prb.conf.example>`

**TBD** A short description of the required changes follows. Firstly the following parameters need to
be changed under the **[rf]** options so that the X310 is configured optimally (the sampling rate
used below is for a 52 PRB DL configuration)::

   [rf]
   tx_gain = 10
   nof_antennas = 1
   device_name = uhd
   device_args = type=x300,clock=external,sampling_rate=15.36e6,lo_freq_offset_hz=30.72e6,send_frame_size=8000,recv_frame_size=8000,num_send_frames=64,num_recv_frames=64
   srate = 15.36e6

**TBD** Likewise, the NR carrier will be active from start (i.e., no SSB is implemented) ADD ALL MISSING

Usage
*****

**TBD** Following configuration, we can run the UE and gNB. The following order should
be used when running the DL demo system:

	1. eNB/ gNB
	2. UE

eNB/ gNB
----------

*The commands listed below are to be run on host #0.*

**TBD** First, the eNB/ gNB should be instantiated, using the following command::

	sudo lteenb gnb-nsa.cfg

**TBD** LIST SPECIFIC PARAMETERS THAN CAN BE CHANGED THROUDH COMMAND LINE (only PRB and MCS)?


**TBD** Console output should be similar to::

	LTE Base Station version 2021-03-15, Copyright (C) 2012-2021 Amarisoft
	This software is licensed to Software Radio Systems (SRS).
	Support and software update available until 2021-10-29.
	RF0: sample_rate=11.520 MHz dl_freq=2140.000 MHz ul_freq=1950.000 MHz (band 1) dl_ant=1 ul_ant=1
	RF1: sample_rate=23.040 MHz dl_freq=3507.840 MHz ul_freq=3507.840 MHz (band n78) dl_ant=1 ul_ant=1

UE
----

*The commands listed below are to be run on the zcu111 (i.e., through SSH via host #1).*

**TBD** To run the UE, first we'll need to load the custom srsUE drivers for the ZCU111, using the following
command (i.e., script handling the required *insmod* calls)::

	./install_drivers.sh

**TBD** Later the embedded srsUE will be executed using the following command (example for a 52 PRB
DL configuration)::

  ./fpga_pdsch_ue_nr -f 2400000000 -p 52 -g 50 -r 0x4601


**TBD** LIST SPECIFIC PARAMETERS THAN CAN BE CHANGED THROUDH COMMAND LINE (only freq and PRB)?

**TBD** Once the UE has been initialised you should see the following::

	Opening 2 channels in RF device=uhd with args=type=x300,clock=external,sampling_rate=11.52e6,lo_freq_offset_hz=11.52e6,None

**TBD** This will be followed by some information regarding the USRP. Once the cell has been found successfully you should see the following::

  Found Cell:  Mode=FDD, PCI=1, PRB=50, Ports=1, CFO=0.1 KHz
  Found PLMN:  Id=00101, TAC=7
  Random Access Transmission: seq=17, tti=8494, ra-rnti=0x5
  RRC Connected
  Random Access Complete.     c-rnti=0x3d, ta=3
  Network attach successful. IP: 192.168.4.2
  Amarisoft Network (Amarisoft) 20/4/2021 23:32:40 TZ:105
  RRC NR reconfiguration successful.
  Random Access Transmission: prach_occasion=0, preamble_index=0, ra-rnti=0x7f, tti=8979
  Random Access Complete.     c-rnti=0x4601, ta=23
  ---------Signal----------|-----------------DL-----------------|-----------UL-----------
  rat  pci  rsrp  pl   cfo | mcs  snr  iter  brate  bler  ta_us | mcs   buff  brate  bler
  lte    1   -52  13    12 |  19   40   0.5    15k    0%    7.3 |  16    0.0    10k    4%
   nr  500     4   0  881m |   2   31   1.0    0.0    0%    0.0 |  17    0.0   6.0k    0%
  lte    1   -49   7  -4.8 |  28   40   0.5   1.4k    0%    7.3 |   0    0.0    0.0    0%
   nr  500     3   0  -5.9 |  27   35   1.0   1.3k    0%    0.0 |  28    0.0   148k    0%
  lte    1   -58  16  -3.7 |  28   40   0.5   1.4k    0%    7.3 |   0    0.0    0.0    0%
   nr  500     3   0  -7.7 |  27   35   1.0   1.3k    0%    0.0 |  28    0.0   148k    0%
  lte    1   -61  19  428m |  28   40   0.5   1.4k    0%    7.3 |   0    0.0    0.0    0%
   nr  500     4   0   2.2 |  27   30   1.4    67k    0%    0.0 |  28     28   143k    0%
  lte    1   -61  19 -507m |  28   40   0.5   1.4k    0%    7.3 |   0    0.0    0.0    0%
   nr  500     4   0  924m |  27   24   1.9    18M    0%    0.0 |  28    0.0   3.7k    0%
  lte    1   -61  19   3.8 |  28   40   0.5   1.4k    0%    7.3 |   0    0.0    0.0    0%
   nr  500     4   0   3.5 |  27   24   1.9    18M    0%    0.0 |   0    0.0    0.0    0%
  lte    1   -61  19   3.8 |  28   40   0.5   1.4k    0%    7.3 |   0    0.0    0.0    0%
   nr  500     4   0   3.1 |  27   24   1.9    18M    0%    0.0 |   0    0.0    0.0    0%

**TBD** REMOVE To confirm the UE successfully connected, you should see the following on the console output of the **eNB**::

	PRACH: cell=00 seq=17 ta=3 snr=28.3 dB
	PRACH: cell=02 seq=0 ta=23 snr=28.3 dB
	               ----DL----------------------- --UL------------------------------------------------
	UE_ID  CL RNTI C cqi ri  mcs retx txok brate  snr puc1  mcs rxko rxok brate     #its phr  pl   ta
	    1 000 003d 1  15  1 15.0    0   16 5.58k 15.4 34.7 18.8    3   13 5.27k  1/3.7/6  31  38  0.0
	    3 002 4601 1  15  1 27.0    0    1   320 36.2   -  27.7    0   87 64.0k  1/2.1/4   -   - -0.3
	    1 000 003d 1  15  1 28.0    0    4 1.42k 16.2 34.8 20.0    1    1   420  1/3.5/6  31  38  0.0
	    3 002 4601 1  15  1 27.0    0    4 1.28k 28.1   -  28.0    0  200  148k  2/2.1/3   -   - -0.3
	    1 000 003d 1  15  1 28.0    0    4 1.42k 16.1 34.8    -    0    0     0        -  31  38  0.0
	    3 002 4601 1  15  1 27.9    0 1037 16.8M 29.9   -  27.9    1   21 16.1k  1/2.3/5   -   - -0.3
	    1 000 003d 1  15  1 28.0    0    4 1.42k 16.3 35.2    -    0    0     0        -  31  38  0.0
	    3 002 4601 1  15  1 27.9    5 1120 18.3M 29.9   -     -    0    0     0        -   -   -    -
	    1 000 003d 1  15  1 28.0    0    4 1.42k 16.0 34.8    -    0    0     0        -  31  38  0.0
	    3 002 4601 1  15  1 27.9    0 1125 18.4M 29.9   -     -    0    0     0        -   -   -    -

**TBD** REMOVE/ADAPT ALL BELOW

Understanding the console Trace
------------------------------------------

The console trace output from the UE contains useful metrics by which the state and performance of the UE can be measured.
The traces can be activated by pressing t+Enter after UE has started.
The following metrics are given in the console trace::

	---------Signal----------|-----------------DL-----------------|-----------UL-----------
	rat  pci  rsrp  pl   cfo | mcs  snr  iter  brate  bler  ta_us | mcs   buff  brate  bler

The following gives a brief description of which each column represents:

	* **RAT:** This is a NSA specific column. It indicates the carrier for which the information is displayed.
	* **PCI:** `Physcial Cell ID <https://www.sharetechnote.com/html/Handbook_LTE_PCI.html>`_
	* **RSRP:** `Reference Signal Receive Power <https://www.sharetechnote.com/html/Handbook_LTE_RSRP.html>`_ (dBm)
	* **PL:** `Pathloss <https://en.wikipedia.org/wiki/Path_loss>`_ (dB)
	* **CFO:** `Carrier Frequency Offset <https://en.wikipedia.org/wiki/Carrier_frequency_offset>`_ (Hz)
	* **MCS:** `Modulation and coding scheme <https://www.sharetechnote.com/html/Handbook_LTE_MCS_ModulationOrder.html>`_ (0-28)
	* **SNR:** `Signal-to-Noise Ratio <https://www.sharetechnote.com/html/RF_Handbook_SNR.html>`_ (dB)
	* **ITER:** Average number of turbo decoder (LTE) or LDPC (NR) iterations
	* **BRATE:** Bitrate (bits/sec)
	* **BLER:** Block error rate
	* **TA_US:** `Timing advance <https://www.sharetechnote.com/html/Handbook_LTE_TimingAdvance.html>`_ (us)
	* **BUFF:** `Uplink buffer status <https://www.sharetechnote.com/html/Handbook_LTE_BSR.html>`_ - data waiting to be transmitted (bytes)


Troubleshooting
***************

The UE currently doesn't support NR cell search and cell measurements. It therefore uses
a pre-configured physical cell id (PCI) to send artificial NR cell measurements to the eNB.
The reported PCI in those measurements is 500 by default (default value in Amarisoft configurations).
If the selected PCI for the cell of interest is different, the value can we overwritten with::

   $ ./srsue/src/srsue --rrc.nr_measurement_pci=140


Or by updating the **[rrc]** options in the config file::

  [rrc]
  nr_measurement_pci = 140
