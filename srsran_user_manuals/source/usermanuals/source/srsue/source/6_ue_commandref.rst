.. _ue_commandref:

Command Line Reference
=======================

The srsUE application runs in the console. When running, type ``t`` in the console to enable the metrics trace.

**4G LTE console trace**:: 

	---------Signal-----------|-----------------DL-----------------|-----------UL-----------
 	cc  pci  rsrp   pl   cfo | mcs  snr  iter  brate  bler  ta_us | mcs   buff  brate  bler
 	 0    1    50  -50 -1.4u |  26  141   1.0   3.2M    0%    0.0 |  21     56   151k    0%
 	 0    1    50  -50 -899n |  26  140   1.0   3.5M    0%    0.0 |  22    169   110k    0%
 	 0    1    50  -50 -349n |  26  140   1.0   3.5M    0%    0.0 |  23    112   100k    0%
 	 0    1    50  -50 -842n |  26  140   1.0   3.5M    0%    0.0 |  23     56    98k    0%
 	 0    1    50  -50 -760n |  26  140   1.0   3.5M    0%    0.0 |  23    167   100k    0%
 	 0    1    50  -50 -754n |  26  140   1.0   3.5M    0%    0.0 |  23    114   100k    0%
 	 0    1    50  -50  106n |  26  140   1.0   3.1M    0%    0.0 |  23    169    88k    0%

**5G NR console trace**:: 

	---------Signal-----------|-----------------DL-----------------|-----------UL-----------
	rat  pci  rsrp   pl   cfo | mcs  snr  iter  brate  bler  ta_us | mcs   buff  brate  bler
	lte    1   -11   11 -1.4u |   0  142   0.0    0.0    0%    0.0 |   0    0.0    0.0    0%
	 nr  500     1    0   23u |  27   70   1.0   8.5M    0%    0.0 |  28    36k   8.3M    0%
	lte    1   -11   11 -1.4u |   0  142   0.0    0.0    0%    0.0 |   0    0.0    0.0    0%
	 nr  500     1    0   23u |  27   70   1.0   9.2M    0%    0.0 |  28    24k   8.1M    0%
	lte    1   -11   11 -1.4u |   0  142   0.0    0.0    0%    0.0 |   0    0.0    0.0    0%
	 nr  500     2    0   23u |  27   69   1.0   4.6M    0%    0.0 |  28    19k   4.2M    0%

Metrics are generated once per second by default. This can be configured using the *expert.metrics_period_secs* parameter in ``ue.conf``.

Metrics are provided for the received signal (Signal), downlink (DL) and uplink (UL) respectively. The following metrics are provided:

:rat: Component carrier, will be either LTE or NR
:cc: Component carrier (LTE)
:pci: `Physical Cell Identifier <https://www.sharetechnote.com/html/Handbook_LTE_PCI.html>`_
:rsrp: `Reference Signal Receive Power <https://www.sharetechnote.com/html/Handbook_LTE_RSRP.html>`_ (dBm)
:pl: `Pathloss <https://en.wikipedia.org/wiki/Path_loss>`_ (dB)
:cfo: `Carrier Frequency Offset <https://en.wikipedia.org/wiki/Carrier_frequency_offset>`_ (Hz)
:mcs: `Modulation and coding scheme <https://www.sharetechnote.com/html/Handbook_LTE_MCS_ModulationOrder.html>`_ (0-28)
:snr: `Signal-to-Noise Ratio <https://www.sharetechnote.com/html/RF_Handbook_SNR.html>`_ (dB)
:iter: Average number of turbo decoder iterations
:brate: Bitrate (bits/sec)
:bler: Block error rate
:ta_us: `Timing advance <https://www.sharetechnote.com/html/Handbook_LTE_TimingAdvance.html>`_ (uS) 
:buff: `Uplink buffer status <https://www.sharetechnote.com/html/Handbook_LTE_BSR.html>`_ - data waiting to be transmitted (bytes)
