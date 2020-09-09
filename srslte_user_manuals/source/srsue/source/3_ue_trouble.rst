.. _ue_trouble:

Troubleshooting
===============

.. _rfConfig: 

RF Configuration
****************

The srsUE software application generates and consumes raw radio signals in the form of `baseband I/Q samples <http://www.ni.com/tutorial/4805/en/>`_. In order to transmit and receive these signals over the air, an RF front end device is needed. Devices supported by srsLTE include e.g. `USRP <https://www.ettus.com/>`_, `BladeRF <https://www.nuand.com/>`_ and `LimeSDR <https://limemicro.com/products/>`_.

When using an RF front-end, the *dl_earfcn* field in ``ue.conf`` should be populated. This field provides the UE with a list (comma separated) of DL EARFCNs. The UE will perform the cell search procedure using the specified EARFCNs. The UL EARFCN is normally deduced from the DL EARFCN but it could optionally forced by setting *ul_earfcn*:

.. code::

  [rf]
  dl_earfcn = 3400
  #ul_earfcn = 21400
  ...

In some cases, one may use some custom bands which do not mach with any EARFCN. In these cases, the downlink and uplink frequencies can be forced by setting *dl_frequency* and *ul_frequency* respectively in Hertzs:

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
There are two main reasons for a network attach failing:
 
 - A misconfigured network
 - RF issues
 
Both may stop the UE being able to see the eNB, cause the UE to fail to connect, or cause the UE to connect but with poor stability. 

Misconfigured Network
---------------------------------
A misconfigured network may stop the UE being able to see the eNB and/ or connect to the EPC. It may be helpful to reference the EPC user manual, namely the :ref:`configuration section<epcConfig>`. To ensure the EPC has been configured correctly. The UE configuration file should also be checked to ensure the relevant information is reflected across the 
two files. See the :ref:`configuration section <ueConfig>` of the UE documentation for notes on this.

An unsuccessful attach can be down to how the UE's credentials are reflected in the EPC's config file and database. See the :ref:`COTS UE <cots_ue_appnote>` Application Note for info on how to add a UE to the EPC's database and ensure the correct network configuration. Note, 
this is for connecting a COTS UE but may also be useful for troubleshooting issues when connecting srsUE using an SDR.

Users should also keep an eye on the console outputs of the UE, eNB and EPC to ensure no errors were given when starting up the network. Errors during network instantiation may lead to elements not connecting properly. 

RF Issues
--------------
The RF-Hardware and hardware configuration should also be checked if a network attach continues to fail.

First check that the hardware is correctly connected and running over USB 3.0, also check the drivers for your HW are up to date. The latest drivers can be found :ref:`here <Drivers>`.

The antenna choice and position is important to ensuring the correct operation of the SDR and overall network. We recommend using the `Vert2450 <https://www.ettus.com/all-products/vert2450/>`_ antenna from Ettus (or similar). The Antenna should 
be positioned at 90° to each other. You should also ensure the correct ports are used for the antenna, for reference, on the b200 mini the *RX2* & *TRX* ports are used. 

It is also important that the correct configuration settings are used as described :ref:`above <rfConfig>`. 

If possible you should use a spectrum analyser or other such piece of equipment to check the state of the signal(s) being transmitted by the RF-hardware. If the signal is too weak or malformed then an attach will not be successful.  
GNU-radio has a block that can be used as a spectrum analyser called `Fosphor <https://kb.ettus.com/Fosphor>`_, which can be used with an SDR to analise spectrum space in real time. 

Carrier frequency offset (CFO) may also result in a UE not being able to sucessfully attach to an eNB. Check the configration files so that the CFOs match. You may also need to calibrate your SDR, as the clock accuracy may result 
in the CFO being outside of the accepted tolerance. Multiple open source tools like `Kalibrate-RTL <https://github.com/steve-m/kalibrate-rtl>`_ can be used to calculate the oscialltor offset of your SDR and help with getting the correct CFO. An external reference clock 
or other such method of clocking can be used to increase clock accuracy. Calibrating your SDR may also help with Peak Throughput and stability. 

Peak Throughput
***************
The peak throughput available to a network can be down to the limitations of the PC being used, the network configuration, the RF-hardware and the physical network conditions. 

Computational Power
---------------------------------
We reccomend using a PC with an 8th Gen i7 processor or above, running Ubuntu 16.04 OS or higher, to achieve the best throughput. Machines with lower specs can also run srsLTE sucessfully but with lower maximum throughput. 

The PCs CPU governor should be set to performance mode to allow for maximum compute power and throughput. This can be done by entering the following command via a terminal::
	
	echo "performance" | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
	
Again, you should also ensure your SDR drivers are up to date and that you are running over USB 3.0, as this will also affect maximum throughput. 

If using a laptop, users should keep the PC connected to a power-source at all times while running srsLTE, as this will increase overall performance of the machine. 

As well as the above steps, users can achieve peak throughput with the available hardware by adjusting the configuration of network elements. For example, the number of PRBs will be limited by the available hardware, users should adjust this accordingly. 
Users can also optimise network elements depnding on the use case, to improve peak throughput. How this is done will be user and use-case dependent. 

RF Hardware
---------------------------------
The RF-signal itself can also affect the peak throughput a network can achieve. Ensure the radio being used is correctly calibrated and that the appropriate gain settings are used. The health of an RF-signal can be quickly checked using the 
console trace output by srsUE. 

The following is an example of a "healthy" console trace from srsUE. This set-up uses 50 PRBs and had a CFO of -2.9 kHz, the SDR being used is an Ettus B210:: 

	--------Signal--------------DL-------------------------------------UL----------------------
	cc pci  rsrp    pl    cfo   mcs   snr turbo  brate   bler   ta_us  mcs   buff  brate   bler
	0   1   -62    62  -3.1k   3.7    39  0.42   3.5k     0%   0.0    14    0.0    33k     0%
	0   1   -62    62  -3.1k   3.5    39  0.50    0.0     0%  0.52    22    0.0    0.0     0%
	0   1   -62    62  -3.1k   3.5    39  0.50    0.0     0%  0.52    22    0.0    0.0     0%
	0   1   -62    62  -3.1k    16    37  0.73    33M     0%  0.52    22    0.0    57k     0%
	0   1   -62    62  -3.1k    28    34   1.0    72M     0%  0.52    22    0.0    69k     0%
	0   1   -62    62  -3.1k    28    34   1.0    72M     0%  0.52    22    2.0    65k     0%
	0   1   -62    62  -3.1k    28    34   1.0    72M     0%  0.52    22    0.0    69k     0%
	0   1   -62    62  -3.1k    28    34   1.0    72M     0%  0.52    22    0.0    69k     0%
	0   1   -62    62  -3.1k    28    34   1.0    72M     0%  0.52    22    2.0    65k     0%
	0   1   -62    62  -3.1k    28    34   1.0    72M     0%  0.52    22    0.0    69k     0%
	0   1   -62    62  -3.1k    28    34   1.0    72M     0%  0.52    22    0.0    69k     0%
	
The SNR, CFO and BLER can be used to de-bug the health of an RF signal. See the section on UE :ref:`command line reference <ue_commandref>` for information regarding the console trace. 

You should also check to see if there are any overflows or lates being seen by the SDR. 

