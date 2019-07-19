.. _ue_trouble:

Troubleshooting
===============

RF Configuration
****************

The srsUE software application generates and consumes raw radio signals in the form of `baseband I/Q samples <http://www.ni.com/tutorial/4805/en/>`_. In order to transmit and receive these signals over the air, an RF front end device is needed. Devices supported by srsLTE include e.g. `USRP <https://www.ettus.com/>`_, `BladeRF <https://www.nuand.com/>`_ and `LimeSDR <https://limemicro.com/products/>`_.

When using an RF front-end, the *dl_earfcn* field in ``ue.conf`` should be populated. This field provides the UE with a list (comma separated) of DL EARFCNs. The UE will perform the cell search procedure using the specified EARFCNs. The UL EARFCN is normally deduced from the DL EARFCN but it could optionally forced by setting *ul_earfcn*:

.. code::

  [rf]
  dl_earfcn = 3400
  #ul_earfcn = 21400
  ...

In some cases, one may use some custom bands which do not mach with any EARFCN. In these cases, the downlink and uplink frequencies can be forced by setting *dl_frequency* and *ul_frequency* respectively in Herz:

.. code::

  ...
  dl_frequency = 400e6
  ul_frequency = 450e6
  ...

Attention: the eNB and UE DL EARFCNs calculate some security sequences using the DL EARFCN. If they do not match, the UE may fail to perform some actions.


Most off-the-shelf RF front-ends have relatively low-accuracy clocks, resulting in high frequency offsets (> 1kHz) from base stations (which use high-accuracy GPS disciplined clock sources). A large frequency offset deteriorates the UE receiver performance. It is recommended setting the parameter *freq_offset* (Hz) in order manually correct large offsets. This parameter applies an offset to the received DL signal and will mitigate the impairment caused by the carrier frequency offset. Also, the UE will apply a proportional correction in the UL frequency.

.. code::

  ...
  freq_offset = -6600
  ...

The current UE does not support open or closed loop power control. The RF front end gain is controlled by the user before running the UE. The transmit gain (*tx_gain*) is specified in dB and maximum transmit power range varies between brands and models.

At the receiver side, an Automatic Gain Control (AGC) module is activated when the receiver gain (*rx_gain* in dB) is not specified. Otherwise, it sets a fixed receive gain. Once again, the range of gain varies between brands and models.

.. code::

  ...
  tx_gain = 80
  #rx_gain = 40
  ...

When transmitting, the srsUE application provides a radio signal to the front-end and specifies the time at which the signal should be transmitted. Typically, an RF front-end will have a small fixed timing offset caused by delays in the RF chain. This offset is usually in the order of microseconds and can vary between different devices. To calibrate this offset, it is possible to use the *time_adv_nsamples* parameter. This compensates the delay and will ensure that the UE transmits at the correct time.

Network Attach
**************

.. warning::

  TBA - diagnosis of network attach failures


Peak Throughput
***************

.. warning::

  TBA

Handover
********

.. warning::

  TBA

