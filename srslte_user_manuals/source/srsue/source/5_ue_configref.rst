.. _ue_configref:

Configuration Reference
=======================

----------------
RF Configuration
----------------
Since the aim of a UE is connecting to an eNb through RF, it needs to receive and transmit baseband signals. There are two ways:

- Using a RF front end such as USRP, Lime SDR or BladeRF
- Using a base-band simulator such as ZeroMQ

In case of using an RF front-end, the *dl_earfcn* field should be populated. This field provides the UE with a list
(comma separated) of DL EARFCNs. The UE will perform the cell search procedure using the specified EARFCNs. The UL EARFCN is normally deduced from the DL EARFCN but it could optionally forced by setting *ul_earfcn*

.. code::

  [rf]
  dl_earfcn = 3400
  #ul_earfcn = 21400
  ...

In some cases, one may use some custom bands which do not mach with any EARFCN. In these cases, the downlink and uplink
frequencies can be forced by setting *dl_frequency* and *ul_frequency* respectively in Herz.

.. code::

  ...
  dl_frequency = 400e6
  ul_frequency = 450e6
  ...

Attention: the eNB and UE DL EARFCNs calculate some security sequences using the DL EARFCN. If they do not match, the UE
may fail to perform some actions.


Most of out-of-the-shelf RF front-ends have a large frequency offset (> 1kHz) from base stations using GPS disciplined clock
sources. A large frequency offset deteriorates the UE receiver performance. It is recommended setting the parameter
*freq_offset* (Hz) in order apply an offset to the DL carrier frequency carrier. This parameter will mitigate the
impairment caused by the carrier frequency offset. Also, the UE will apply a proportional correction in the UL frequency.

.. code::

  ...
  freq_offset = -6600
  ...

The current UE does not support neither Open nor Closed loop power control. The RF front end gain is controlled by the
user before running the UE. The transmit gain (*tx_gain*) in dB and maximum transmit power range varies between brands
and models.

At the receiver side, an Automatic Gain Control (AGC) module is activated when the receiver gain (*rx_gain* in dB) is
not specified. Otherwise, it sets a fixed receive gain. Once again, the range of gain varies between brands and models.

.. code::

  ...
  tx_gain = 80
  #rx_gain = 40
  ...

As mentioned in the UE features, it supports MIMO TM3/4 and Carrier Aggregation. You might find a bit confusing the
following parameters. First of all, one can set a number of radios (1 or 2). This will open *nof_radios* instances of
RF front-ends. Only one radio is synchronized to the Primary Cell. The second radio will be only used if the Primary Cell
configures a Secondary Cell for Carrier Aggregation. Then the UE will use the second RF front-end for receiving and
transmitting from the Secondary Cell.

If one uses a RF device that can tune RF ports independently (like USRP X300, not B200 nor BladeRF), one can set
*nof_rf_channels* to two for using a number of the available ports for carrier aggregation (not MIMO).

For 2 Component Carrier Aggregation:

.. code::

  ...
  nof_radios = 1
  nof_rf_channels = 2
  nof_rx_ant = 1
  ...


In contrast, the parameter *nof_rx_ant* is used for setting the number of receive antennas for MIMO (two layer TM3/4).

For TM3/4 configuration:

.. code::

  ...
  nof_radios = 1
  nof_rf_channels = 1
  nof_rx_ant = 2
  ...

You may wonder if one can force or specify what RF driver use. It is possible using *device_name* and *device_args*.
This two parameters are used for specifying properties of the RF-front end to open.

For UHD driver (x310, b210, b200mini and so on) the *device_name* shall be set to *uhd*. The parameter *device_args*
accepts the following arguments:

- UHD address and configuration arguments: default UHD driver arguments such as *type*, *serial*, *ip_address*, *master_clock_rate* and so on.
- *clock*: specifies the clock source. Valid clock sources are *internal* (default), *external* and *gpsdo*
- *otw_format*: specifies whether the baseband samples coming from the RF front-end width is 12 (*sc12*) or 16 (*sc16*) bit.
- *tx_subdev_spec*: transmitter sub-device specification according to Ettus Research documentation.
- *rx_subdev_spec*: receiver sub-device specification according to Ettus Research documentation.

If more than one RF front-end, one can use *device_args_2* for the second device and *device_args_3* for a third one.


.. code::

  ...
  device_name = uhd
  device_args = type=b200,clock=gpsdo
  #device_args_1 = auto
  #device_args_2 = auto
  ...

Since the UE requests to the RF front end to transmit at a given time but the RF will transmit a few samples delayed.
This will cause an initial TA of a few microseconds. So, *time_adv_nsamples* compensates this delay and makes the UE
transmit at the right times.

----------------
Channel emulator
----------------

The srsUE LTE UE include an internal channel emulator in the downlink path which can emulate uncorrelated fading channels, propagation delay and Radio-Link failure.

The channel emulator can be enabled and disabled with the parameter *channel.dl.enable*.

.. code::
  
  [channel]
  dl.enable = true
  ...

As mentioned above, the channel emulator can simulate fading channels. It supports 4 different models:

* none: single tap with no delay, doppler dispersion can be applied if specified.
* epa: Extended Pedestrian A, described in 3GPP 36.101 Section B.2.1
* eva: Extended Vehicular A model, described in 3GPP 36.101 Section B.2.1
* etu: Extended Typical Urban model, described in 3GPP 36.101 Section B.2.1

The fading emulator has two parameters: *enable* and *model*. The parameter *model* is the channel model mentioned above, followed by the maximum Doppler dispersion. The following example enables the fading submodule with a EVA fading model and a maximum doppler dispersion of 5 Hz.

.. code::
  
  ...
  dl.fading.enable = true
  dl.fading.model  = eva5
  ...

The delay simulator generates the delay according to the next formula:

.. math::

   d(t) = delay.minimum_us + (delay.maximum_us - delay.minimum_us) * (1.0 + sin(2*pi*t/delay.period)) / 2.0

Where *delay.minimum_us* and *delay.maximum_us* are specified in microseconds while *delay.period* must be in seconds.

Hence, the maximum simulated speed is given by:

.. math::

  v_max = (delay.maximum_us - delay.minimum_us) * pi * 300 / delay.period

The following example enables the delay simulator for having a period of 1h with a minimum delay of 10 microseconds and a maximum delay of 100 microseconds:

.. code::
  
  ...
  dl.delay.enable     = true
  dl.delay.period     = 3600
  dl.delay.maximum_us = 100
  dl.delay.minimum_us = 10
  ...
  
Finally, the Radio-Link Failure (RLF) simulator has two states:

* on: the UE receives baseband signal, unafected by the simulator.
* off: the UE does not receive any signal, the simulator substitutes the baseband by zeros.

The time the emulator spends in *on* is parametrized by *rlf.t_on_ms* and *rlf.t_off_ms* for *off*. Both parameters are expected to be in milliseconds.

The following example enables the RLF simulator for having 2 seconds of blackout every 10 seconds of full baseband signal:

.. code::
  
  ...
  dl.rlf.enable       = true
  dl.rlf.t_on_ms      = 10000
  dl.rlf.t_off_ms     = 2000
  ...

