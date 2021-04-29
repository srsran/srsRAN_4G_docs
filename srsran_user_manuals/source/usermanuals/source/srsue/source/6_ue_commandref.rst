.. _ue_commandref:

Command Line Reference
=======================

The srsUE application runs in the console. When running, type ``t`` in the console to enable the metrics trace. Example metrics trace::

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

Metrics are generated once per second by default. This can be configured using the *expert.metrics_period_secs* parameter in ``ue.conf``.

Metrics are provided for the received signal (Signal), downlink (DL) and uplink (UL) respectively. The following metrics are provided:

:cc: Component carrier
:rsrp: `Reference Signal Receive Power <https://www.sharetechnote.com/html/Handbook_LTE_RSRP.html>`_ (dBm)
:pl: `Pathloss <https://en.wikipedia.org/wiki/Path_loss>`_ (dB)
:cfo: `Carrier Frequency Offset <https://en.wikipedia.org/wiki/Carrier_frequency_offset>`_ (Hz)
:mcs: `Modulation and coding scheme <https://www.sharetechnote.com/html/Handbook_LTE_MCS_ModulationOrder.html>`_ (0-28)
:snr: `Signal-to-Noise Ratio <https://www.sharetechnote.com/html/RF_Handbook_SNR.html>`_ (dB)
:turbo: Average number of turbo decoder iterations
:brate: Bitrate (bits/sec)
:bler: Block error rate
:ta_us: `Timing advance <https://www.sharetechnote.com/html/Handbook_LTE_TimingAdvance.html>`_ (uS) 
:buff: `Uplink buffer status <https://www.sharetechnote.com/html/Handbook_LTE_BSR.html>`_ - data waiting to be transmitted (bytes)
