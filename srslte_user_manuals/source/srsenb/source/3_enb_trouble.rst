.. _enb_trouble:

Troubleshooting
========================

UE Wont Attach
*******************
If you are experiencing errors getting a successful attach to srsENB you should first check the PCAP output by the ENB and check how far through the attach procedure the network gets. This can be done using wireshark, 
as shown :ref:`here <Wireshark>` in the documentation. 

If possible you should use a spectrum analyser or other such piece of equipment to check the state of the signal(s) being transmitted by the RF-hardware. If the signal is too weak or malformed then an attach may fail.  
GNU-radio has a block that can be used as a spectrum analyser called `Fosphor <https://kb.ettus.com/Fosphor>`_, which can be used with an SDR to analyze spectrum space in real time. 

COTS UE Issues
********************
The following are the most common issues when using a COTS UE with srsENB. A full application note on this can be found :ref:`here <cots_ue_appnote>`. Reference this for more detail on the following issues.

UE Cant See eNB
--------------------------
The likely reasons for this are the RF conditions, the frequency accuracy of the frontend being used and the eNB configuration. 

The RF conditions can be affected by the antenna being used, we recommend the `Vert2450 <https://www.ettus.com/all-products/vert2450/>`_ antenna from Ettus (or similar). Ensure these are also placed at 90° to each other. 
If possible you should use a spectrum analyser or other such piece of equipment to check the state of the signal(s) being transmitted by the RF-hardware. As outlined above. You should also check the configuration files for the eNB and UE 
and check that the correct frequency settings are being used across both. 

Frequency accuracy may also result in an unsuccessful attach to an eNB. Check the configuration files so that the CFOs match across both the eNB & UE. You may need to calibrate your SDR, as the clock accuracy may result 
in the CFO being outside of the accepted tolerance. Multiple open source tools like `Kalibrate-RTL <https://github.com/steve-m/kalibrate-rtl>`_ can be used to calculate the oscillator offset of your SDR and help with getting the correct CFO. An external reference clock 
or other such methods of clocking can be used to increase clock accuracy.

Cant Access Internet
-------------------------------
This may be down to a misconfigured APN in the UE and/ or eNB. See the :ref:`app note <cots_ue_appnote>` for information on how to configure this. 

Peak Throughput
***************
The peak throughput available to a network can be down to the limitations of the PC being used, the network configuration, the RF-hardware and the physical network conditions. 

Computational Power
---------------------------------
We recommend using a PC with an 8th Gen i7 processor or above, running Ubuntu 16.04 OS or higher, to achieve the best throughput. Machines with lower specs can also run srsLTE successfully but with lower maximum throughput. 

The PCs CPU governor should be set to performance mode to allow for maximum compute power and throughput. This can be done by entering the following command via a terminal::
	
	echo "performance" | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
	
Again, you should also ensure your SDR drivers are up to date and that you are running over USB 3.0, as this will also affect maximum throughput. 

If using a laptop, users should keep the PC connected to a power-source at all times while running srsLTE, as this will increase overall performance of the machine. 

As well as the above steps, users can achieve peak throughput with the available hardware by adjusting the configuration of network elements. For example, the number of PRBs will be limited by the available hardware, users should adjust this accordingly. 
Users can also optimise network elements depending on the use case, to improve peak throughput. How this is done will be user and use-case dependent. 

RF Hardware
---------------------------------
The RF-signal itself can also affect the peak throughput a network can achieve. Ensure the radio being used is correctly calibrated and that the appropriate gain settings are used. 

The health of an RF-signal being sent out by the eNB can be quickly checked using the console trace output by srsUE. 



