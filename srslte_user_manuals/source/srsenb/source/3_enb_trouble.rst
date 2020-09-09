.. _enb_trouble:

Troubleshooting
===============

COTS UE Issues
**************
The following are the most common issues when using a COTS UE with srsENB. A full application note on this can be found :ref:`here <cots_ue_appnote>`. Reference this for more detail on the following issues.

UE Can't See The Network
------------------------
The most likely reasons for a UE not seeing the network are the RF conditions, the frequency accuracy of the RF frontend being used and the eNB configuration.

The first thing to check is that the LTE frequency band and EARFCN which you have configured are supported by the UE which you are using. Most UE devices support a subset of the bands allocated for LTE. Ensure also that the full bandwidth of the configured LTE carrier is within the frequency band which you are using.

The RF conditions can be affected by the antenna being used, we recommend the `Vert2450 <https://www.ettus.com/all-products/vert2450/>`_ antenna from Ettus (or similar). Ensure the antennae are placed at a 90° angle to each other to minimize cross-talk. 
If possible you should use a spectrum analyser or other such piece of equipment to check the quality of the signal(s) being transmitted by the RF-hardware. If signals are too weak or malformed then a UE may not successfully receive them and will not attempt to attach. The `gr-fosphor tool <https://github.com/osmocom/gr-fosphor>`_ is a very useful SDR spectrum analyzer which can be used to check the properties of transmitted RF signals.

Low carrier frequency accuracy in the RF front-end may also cause a UE to fail to see the network. The clock accuracy in most SDR front-ends is quite low without the use of an external reference clock input. It may be possible to use lab equipment or open source tools such as `Kalibrate-RTL <https://github.com/steve-m/kalibrate-rtl>`_ to estimate the CFO of your RF front-end and to manually compensate by setting small frequency offsets in the Downlink and Uplink carrier frequency settings of the eNodeB configuration file.

UE Won't Attach
---------------
If the UE sees the network but cannot successfully attach, you can check the MAC-layer PCAP provided by srsENB using Wireshark to see at which point in the attach procedure it fails. For more information about the MAC-layer PCAP and using Wireshark, see :ref:`here <Wireshark>` in the documentation.

Can't Access Internet
---------------------
If an attached UE cannot access the internet, this may be due to a misconfigured APN in the UE and/ or eNB. See the :ref:`app note <cots_ue_appnote>` for information on how to configure this. 

Another common reason is misconfigured IP routing at the EPC. If using srsEPC, make sure to follow the instructions on IP Masquerading in the :ref:`app note <cots_ue_appnote>`.

Peak Throughput
***************
Maximum achievable srsENB peak throughput may be limited for a number of different reasons. These include limitations in the PC being used, the network configuration, the RF-hardware and the physical network conditions. 

Computational Power
-------------------
In order to achieve peak throughput, we recommend using a PC with an 8th Gen i7 processor or above, running Ubuntu 16.04 OS or highe. Machines with lower specs can also run srsENB sucessfully but with lower maximum achievable throughput. 

The CPU governor of the PC should be set to performance mode to allow for maximum compute power and throughput. This can be configured for e.g. Ubuntu using::
	
	echo "performance" | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
	
Again, you should also ensure your SDR drivers are up to date and that you are running over USB 3.0, as this will also affect maximum throughput. 

If using a laptop, users should keep the PC connected to a power-source at all times while running srsENB, as this will avoid performance loss due to CPU frequency scaling on the machine. 

The computational requirements of the srsENB application are closely tied to the bandwidth of the LTE carrier being used. For example, maximum throughput using 100-PRB carrier will require a more powerful CPU than maximum throughput using a 25-PRB carrier. If your machine is not powerful enough to support srsENB with a given network configuration, you will see Late and/or Overflow packet reports from the SDR front-end.

RF Hardware
-----------
The RF-signal itself can also affect the peak throughput a network can achieve. Ensure the radio being used is correctly calibrated and that the appropriate gain settings are used. The health of an RF-signal can be quickly checked using the console trace output by srsENB.


