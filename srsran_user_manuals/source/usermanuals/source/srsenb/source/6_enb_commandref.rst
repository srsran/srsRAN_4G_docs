.. _enb_commandref:

Command Line Reference
######################

The srsENB application runs in the console. When running, type ``t`` in the console to enable the metrics trace. 

**4G LTE Output**:: 

	               -----------------DL----------------|-------------------------UL-------------------------
	rat  pci rnti  cqi  ri  mcs  brate   ok  nok  (%) | pusch  pucch  phr  mcs  brate   ok  nok  (%)    bsr
	lte    1   47   15   0   26   1.3M  321    0   0% |  99.9   99.9   30   21    84k   53    0   0%    0.0
	lte    1   47   15   0   26   3.5M  875    0   0% |  99.9   99.9   30   23    98k   48    0   0%    0.0
	lte    1   47   15   0   26   3.5M  876    0   0% |  99.9   99.9   30   22   111k   56    0   0%    0.0
	lte    1   47   15   0   26   3.5M  876    0   0% |  99.9   99.9   30   23   100k   49    0   0%    0.0
	lte    1   47   15   0   26   3.5M  878    0   0% |  99.9   99.9   30   23    98k   48    0   0%    0.0
	lte    1   47   15   0   26   3.5M  874    0   0% |  99.9   99.9   30   22   110k   56    0   0%    0.0
	lte    1   47   15   0   26   3.5M  877    0   0% |  99.9   99.9   30   23   100k   49    0   0%    0.0

**5G NR Output**:: 

	          -----------------DL----------------|-------------------------UL-------------------------                                                                                                           
	rat rnti  cqi  ri  mcs  brate   ok  nok  (%) | pusch  pucch  phr  mcs  brate   ok  nok  (%)    bsr
	lte   46   15   0    0      0    0    0   0% |   n/a    n/a    0    0      0    0    0   0%    0.0
	 nr 4601  n/a   0   27   6.9M  124    0   0% |   n/a    n/a    0    0   6.1M   95    0   0%    0.0
	lte   46   15   0    0      0    0    0   0% |   n/a    n/a    0    0      0    0    0   0%    0.0
	 nr 4601  n/a   0   27   4.4M   92    0   0% |   n/a    n/a    0    0   4.2M   76    0   0%    0.0

Metrics are generated once per second by default. This can be configured using the *expert.metrics_period_secs* parameter in ``enb.conf``.

Metrics are provided on a per-UE basis for the downlink (DL) and uplink (UL) respectively. The following metrics are provided:

:rat: The RAT being used, either NR or LTE
:pci: `Physical Cell Identifier <https://www.sharetechnote.com/html/Handbook_LTE_PCI.html>`_
:rnti: `Radio Network Temporary Identifier <http://sharetechnote.com/html/Handbook_LTE_RNTI.html>`_ (UE identifier)
:cqi: `Channel Quality Indicator <https://www.sharetechnote.com/html/Handbook_LTE_CQI.html>`_ reported by the UE (1-15)
:ri: `Rank Indicator <https://www.sharetechnote.com/html/Handbook_LTE_RI.html>`_ reported by the UE (dB)
:mcs: `Modulation and coding scheme <https://www.sharetechnote.com/html/Handbook_LTE_MCS_ModulationOrder.html>`_ (0-28)
:brate: Bitrate (bits/sec)
:ok: Number of packets successfully sent
:nok: Number of packets dropped
:(%): % of packets dropped
:pusch: PUSCH SNIR (Signal-to-Interference-plus-Noise Ratio)
:pucch: PUCCH SNIR
:phr: `Power Headroom <https://www.sharetechnote.com/html/Handbook_LTE_PHR.html>`_ (dB)
:bsr: `Buffer Status Report <https://www.sharetechnote.com/html/Handbook_LTE_BSR.html>`_ - data waiting to be transmitted as reported by the UE (bytes)