.. _enb_commandref:

Command Line Reference
=======================

The srsENB application runs in the console. When running, type ``t`` in the console to enable the metrics trace. Example metrics trace::

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

Metrics are generated once per second by default. This can be configured using the *expert.metrics_period_secs* parameter in ``enb.conf``.

Metrics are provided on a per-UE basis for the downlink (DL) and uplink (UL) respectively. The following metrics are provided:

:rnti: `Radio Network Temporary Identifier <http://sharetechnote.com/html/Handbook_LTE_RNTI.html>`_ (UE identifier)
:cqi: `Channel Quality Indicator <https://www.sharetechnote.com/html/Handbook_LTE_CQI.html>`_ reported by the UE (1-15)
:ri: `Rank Indicator <https://www.sharetechnote.com/html/Handbook_LTE_RI.html>`_ reported by the UE (dB)
:mcs: `Modulation and coding scheme <https://www.sharetechnote.com/html/Handbook_LTE_MCS_ModulationOrder.html>`_ (0-28)
:brate: Bitrate (bits/sec)
:bler: Block error rate
:snr: `Signal-to-Noise Ratio <https://www.sharetechnote.com/html/RF_Handbook_SNR.html>`_ (dB)
:phr: `Power Headroom <https://www.sharetechnote.com/html/Handbook_LTE_PHR.html>`_ (dB)
:bsr: `Buffer Status Report <https://www.sharetechnote.com/html/Handbook_LTE_BSR.html>`_ - data waiting to be transmitted as reported by the UE (bytes)