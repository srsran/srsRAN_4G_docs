.. _ue_advanced:

Advanced Usage
##############

External USIM
*************

**This section is only needed if you do not have access to the USIM credentials, or have no control over the network. Note, most programmable or test USIM cards ship with their credentials.**

Using an actual SIM card to authenticate the user against the network is an advanced feature.
It requires a SIM card reader attached to the PC running srsUE that is supported by
`PCSClite <https://pcsclite.apdu.fr/>`_.

Before using a SIM card, please make sure to disable PIN activation using a regular phone.

In order to compile srsUE with support for it, the pcsclite development headers as well as the
pcsc daemon need to be installed and running.
On Ubuntu (or other Debian derivates), this can be done with::

    sudo apt-get install libpcsclite-dev pcscd pcsc-tools

After this is done, please verify you've got a PCSC-compatible reader by running 'pcsc_scan'.

Now, CMake should pick up the pcsc libraries and build the support code for it. If that is not the case,
try with a clean build folder or remove your exisiting ``CMakeCache.txt``::

    $ cmake ..
    ...
    -- PCSC LIBRARIES: /usr/lib/x86_64-linux-gnu/libpcsclite.so
    -- PCSC INCLUDE DIRS: /usr/include/PCSC
    -- Building with PCSC support.
    ...
    $ make

After the build is complete, you can verify the correct operation with the ``pcsc_usim_test`` application.
Please verify that the IMSI can be read from the card::


    $ ./srsue/test/upper/pcsc_usim_test
    ..
    09:06:36.064073 [USIM] [D] SCARD: MNC length=2
    09:06:36.064079 [USIM] [D] MNC length 2
    IMSI: 21XXXXXXXXXXXX
    09:06:36.064095 [USIM] [D] SCARD: UMTS auth - RAND
                 0000: bc 4c b0 27 b3 4b 7f 51 21 5e 56 5f 67 3f de 4f
    09:06:36.064102 [USIM] [D] SCARD: UMTS auth - AUTN
                 0000: 5a 17 77 3c 62 57 90 01 cf 47 f7 6d b3 a0 19 46
    09:06:36.064107 [USIM] [D] SCARD: scard_transmit: send
                 0000: 00 11 00 81 22 10 bc ac b1 17 13 4b 6f 51 21 5e
                 0010: 47 47 6d b3 a0 19 46
    09:06:36.119675 [USIM] [D] SCARD: SCardTransmit: recv
                 0000: 98 62
    09:06:36.119707 [USIM] [D] SCARD: UMTS alg response
                 0000: 98 62
    09:06:36.119717 [USIM] [W] SCARD: UMTS auth failed - MAC != XMAC
    09:06:36.119725 [USIM] [E] SCARD: Failure during USIM UMTS authentication
    09:06:36.119732 [USIM] [D] SCARD: deinitializing smart card interface


If those steps completed successfully we can now start srsUE by either enabling the PCSC USIM in
the config file or by passing the option as an command line argument, e.g., run::

    $ ./srsue/src/srsue --usim.mode=pcsc


.. Carrier Aggregation
.. *******************
.. 
.. The srsUE application supports MIMO TM3/4 and Carrier Aggregation (CA). In order to use CA, you will need to configure the UE for the RF board configuration you wish to use.
.. 
.. First of all, one can set a number of radios (1 or 2). This will open *nof_radios* instances of
.. RF front-ends. Only one radio is synchronized to the Primary Cell. The second radio will be only used if the Primary Cell configures a Secondary Cell for Carrier Aggregation. Then the UE will use the second RF front-end for receiving and transmitting from that Secondary Cell.
.. 
.. If one uses a RF device that can tune RF ports independently (like USRP X300, not B200 nor BladeRF), one can set *nof_rf_channels* to two for using a number of the available ports for carrier aggregation (not MIMO).
.. 
.. For 2 Component Carrier Aggregation:
.. 
..   nof_radios = 1
..   nof_rf_channels = 2
..   nof_rx_ant = 1
.. 
.. 
.. In contrast, the parameter *nof_rx_ant* is used for setting the number of receive antennas for MIMO (two layer TM3/4).
.. 
.. For TM3/4 configuration:
.. 
..   nof_radios = 1
..   nof_rf_channels = 1
..   nof_rx_ant = 2
.. 
.. You may wonder if one can force or specify what RF driver use. It is possible using *device_name* and *device_args*. These two parameters are used for specifying properties of the RF-front end to open.
.. 
.. For UHD driver (x310, b210, b200mini and so on) the *device_name* shall be set to *uhd*. The parameter *device_args* accepts the following arguments:
.. 
.. - UHD address and configuration arguments: default UHD driver arguments such as *type*, *serial*, *ip_address*, *master_clock_rate* and so on.
.. - *clock*: specifies the clock source. Valid clock sources are *internal* (default), *external* and *gpsdo*
.. - *otw_format*: specifies whether the baseband samples coming from the RF front-end width is 12 (*sc12*) or 16 (*sc16*) bit.
.. - *tx_subdev_spec*: transmitter sub-device specification according to Ettus Research documentation.
.. - *rx_subdev_spec*: receiver sub-device specification according to Ettus Research documentation.
.. 
.. If using more than one RF front-end, one can use *device_args_2* for the second device and *device_args_3* for a third one. 
.. 
.. 
..   device_name = uhd
..   device_args = type=b200,clock=gpsdo
..   #device_args_1 = auto
..   #device_args_2 = auto
.. 
.. 
.. *IMPORTANT: if two UHD devices are used, the serial number or IP address shall be indicated in the device arguments. Otherwise, UHD may try to open twice the same device*


Channel Emulator
****************

The srsUE application includes an internal channel emulator in the downlink receive path which can emulate uncorrelated fading channels, propagation delay and Radio-Link failure.

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

The fading emulator has two parameters: *enable* and *model*. The parameter *model* is the channel model mentioned above, followed by the maximum Doppler dispersion (e.g. eva5). The following example enables the fading submodule with a EVA fading model and a maximum doppler dispersion of 5 Hz.

.. code::

  ...
  dl.fading.enable = true
  dl.fading.model  = eva5
  ...

The delay simulator generates the delay according to the next formula:

.. math::

   d(t) = \text{delay.min}\_\text{us} + (\text{delay.max}\_\text{us} - \text{delay.min}\_\text{us}) \cdot \frac{1 + \sin\left(\frac{2\pi t}{\text{delay.period}}\right)}{2}

Where *delay.min_us* and *delay.max_us* are specified in microseconds while *delay.period* must be in seconds.

Hence, the maximum simulated speed is given by:

.. math::

   v_\text{max} = (\text{delay.max}\_\text{us} - \text{delay.min}\_\text{us}) \cdot \frac{300 \pi}{\text{delay.period}}

The following example enables the delay simulator for having a period of 1h with a minimum delay of 10 microseconds and a maximum delay of 100 microseconds:

.. code::

  ...
  dl.delay.enable     = true
  dl.delay.period     = 3600
  dl.delay.max_us = 100
  dl.delay.min_us = 10
  ...

Finally, the Radio-Link Failure (RLF) simulator has two states:

* on: the UE receives baseband signal, unaffected by the simulator.
* off: the UE does not receive any signal, the simulator substitutes the baseband with zeros.

The time the emulator spends in *on* is parametrized by *rlf.t_on_ms* and *rlf.t_off_ms* for *off*. Both parameters are expected to be in milliseconds.

The following example enables the RLF simulator for having 2 seconds of blackout every 10 seconds of full baseband signal:

.. code::

  ...
  dl.rlf.enable       = true
  dl.rlf.t_on_ms      = 10000
  dl.rlf.t_off_ms     = 2000
  ...

MIMO
****

The srsUE supports MIMO operation for transmission modes 1, 2, 3 and 4. The user can select the number of select antennas in the ``ue.conf`` :: 
  
  ...
  [rf]
  ...
  nof_rx_ant = 2
  ...

Do you want to attach to a 2 port eNb and you have only one receive channel? 

No problem. The UE can attach to 2 port cell and be in TM3 or TM4 without having a second receive antenna. Nevertheless, it will not take advantage 
of spatial multiplexing and it will not achieve the maximum throughput.

5G NR 
*****

srsRAN 4G 21.10 and 22.04 brought prototype 5G NSA and 5G SA capabilities to srsUE respectively. These capabilities can be enabled via the srsUE configuration file. See the links in the following sections for information on 
5G NSA/ SA and how to enable these features on srsUE.  

5G NSA
======

For information on what 5G NSA is, and how a 5G NSA network can be configured with srsRAN 4G take a look at the following sections of our documentation: 

  - :ref:`5G NSA overview <5G_NSA>`
  - :ref:`Creating an E2E 5G NSA Network with srsRAN 4G <5g_nsa_zmq_appnote>`

srsUE is also compatible with 3rd party eNB and gNB applications and equipment. An example of this can be seen in our guide outlining how to :ref:`connect srsUE to an Amarisoft Callbox <5g_nsa_amari_appnote>`. 

5G SA 
======

For information on what 5G SA is, and how a 5G SA network can be configured with srsRAN 4G take a look at the following sections of our documentation: 

  - :ref:`5G SA overview <5G_SA>`
  - :ref:`Creating an E2E 5G NA Network with srsRAN 4G <5g_sa_e2e_appnote>`

