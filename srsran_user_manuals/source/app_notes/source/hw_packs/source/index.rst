.. Suggested Hardware Application Note

.. _suggestedHW_appnote:

Hardware Options
================
This information is correct as of March 15th 2021

Introduction
*************
This document aims to provide users with an overview of the suggested PC and SDR hardware combinations that can be used to best explore the functionality of srsRAN. There are 100’s of possible combinations of PC, notebook, single board computer and SDR hardware that can demonstrate the uses of srsRAN. This list aims to provide three possible hardware packages that can help to guide users when choosing what to buy. These packages are grouped by price, with full set-ups cotsing >$400, >$3,000 and finally >$16,000. The three packages proposed here should provide any user with enough information to create their ideal set-up, which easily meets their needs.  

Choosing Hardware
***********************
When choosing these packages we compared each hardware option under the same metrics. With one set for the computational hardware, and one for the SDR. 

Compute Criteria
-----------------------
The following are the main specifications taken into account when selecting the compute platform for each of these packages: 

	* **Cost** - Overall cost of the machine
	* **Number of cores** - This will affect overall performance
	* **Processor frequency** - CPUs running at lower frequencies may struggle under heavy computational loads
	* **Cache size** - A good indication of speed. More cache memory means certain computations will be faster. 
	* **Number of threads** - More threads will enable a processor to execute processes faster. 
	


This is not an exhaustive list of criteria to look at when selecting a compute platform for SDR experimentation and development. Intended use-case will dictate choice the most here, as well as other external factors which can be subjective to either the user or overall use conditions.

Other useful things to take into account when choosing a compute platform for SDR research and experimentation are: 
 
	* **Processor Cinebench score** - This gives a good indication of a processor's ability to deal with high computational load. Find out more `here <https://www.notebookcheck.net/CineBench-R20-benchmark-now-available-is-8x-more-demanding-than-CineBench-R15.413751.0.html>`_.
	* **Cooling ability** - More cooling ability will ensure CPU performance does not drop off significantly under heavy load 
	* **Portability** - Some use-cases may benefit from a PC that is portable

SDR Criteria
-----------------------
When selecting the SDR options to highlight we took the following into account: 

	* **Cost** - Cost per unit of the SDR
	* **Driver** - Which driver the SDR uses (Soapy, UHD, etc)
	* **Frequency range** - The frequency range(s) the SDR operates in
	* **Bandwidth** - Maximum possible bandwidth available 
	* **Clock** - Clock rate
	* **Channels** - The number of channels available (SISO, MIMO, etc)
	* **FPGA** - The specifications of the onboard FPGA

Much like when choosing compute hardware, the metrics you may look at when choosing an SDR will vary depending on use-case and other factors. This list is in no way exhaustive, but provides a good platform by which to compare options. 

Package Overview
*********************
Each package will contain a recommended SDR and compute hardware bundle. With some appropriate use-cases for each. A full end-to-end system will require at least two SDRs and two Compute platforms. As previously mentioned, these packages represent possible combinations, and are by no means a gold standard of the types of hardware needed for SDR experimentation. 

Package 1
*************

.. csv-table::
   :align: center
   :file: pack1.csv
   :widths: 50, 50
   :header-rows: 1

This package is inspired by our :ref:`R. pi4 app note <pi4_appnote>`.

Such a set-up would allow users to create a cheap end-to-end network, for under $400 without the need for a main PC. To run a full end-to-end system using the above equipment a user would need 3 Raspberry Pi4 units and 2 LimeSDR minis. A Pi4 is needed for the EPC, eNB and UE, and a front-end is needed for both the eNB and UE. Due to the small size and portability of the system this setup is ideal for on-the-fly demos and testing of networks and applications that don't require high-powered compute hardware or frontends. 

Advantages
----------------
 * Low cost
 * Highly portable
 
Limitations
----------------
 * Limited cell bandwidth (currently 5 MHz)
 * Limited max bitrate in the UL

Package 2
*************

.. csv-table::
   :align: center
   :file: pack2.csv
   :widths: 50, 50
   :header-rows: 1
   
This offers a step up from the previous package; in price and performance. The BladeRF micro 2.0 xA4 offers users a 2X2 MIMO configuration, higher max bandwidth, a larger frequency range, and a larger FPGA. The HP Omen 15 is a gaming notebook, meaning it is built for high performance and high CPU load for a sustained period of time. The intel i5 10300H is the main draw here, having scored highly in the cinebench r20 benchmarking test. This set-up is considerably more expensive and would cost roughly $3000 for a full set up of 2 PCs and 2 frontends. 

Advantages
----------------
 * Easily portable, with improved performance
 * Suits nearly any use-case 
 
Limitations
----------------
 * Single cell configuration but up to 20 MHz 2x2 MIMO
 * Non-expandable Bandwidth and operating frequencies 

Package 3
*************

.. csv-table::
   :align: center
   :file: pack3.csv
   :widths: 50, 50
   :header-rows: 1

This system offers users the most potential in terms of RF-frontend capabilities on PC performance. The Ettus x310 offers users the largest frequency range, from DC to 6 GHz with the use of the appropriate daughter cards, a potential bandwidth of 160 MHz (requires the correct daughter cards), a multi-cell configuration and a powerful Kintex7 FPGA. The 3340 workstation offers an intel i7-10700 which is capable of high intensity computations without a significant drop off in performance over sustained periods of time. The workstation offers 10 Gbps ethernet connection, which allows users full utilization of the 10 Gbps connection available on the x310. A full E2E system would cost a total of roughly $15800.

Advantages
----------------
 * Carrier Aggregation
 * Multi-cell configuration 


Limitations
----------------

 * Not all PCs will be able to interface via 10Gb ethernet. May have to use adapters.

ZMQ	
******

srsRAN has been designed with support for Zero-MQ. This is a "fake RF" driver, which allows users to set-up a virtual end-to-end network without the use of physical RF-hardware. This is a powerful tool for experimentations and development for users that do not have access to hardware, or for those who cannot purchase it. 

ZMQ does not require large amounts of computational resources to run, meaning most PCs and notebooks (including the R. Pi4) can run it without sacrificing performance. ZMQ replaces the radio link between the eNB and UE, by creating a transmit and receive pipe for exchanging IQ samples TCP or IPC. 

Our :ref:`ZMQ app note <zeromq_appnote>` clearly demonstrates how srsRAN can be used with ZMQ.



