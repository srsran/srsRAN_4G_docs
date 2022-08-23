.. _devguide_test

Dev Guide
#########

MAC
*****

The MAC is divided into the following sub-components:

**MAC Controller**  

Translates DU configuration requests into configuration commands that can be understood by the remaining MAC sub-components. The MAC controller ensures that the other 
components are configured with minimal service disruption in terms of traffic latency and avoiding any race conditions. The configuration commands that the DU manager 
sends include the addition of new DU cells and addition/reconfiguration/removal of UEs. See class: mac_controller

**RACH Handler** 

Manages the allocation of RNTIs for the received PRACH preambles and association of reach RNTI to a DU UE Index. See rach_handler

**MAC UL Processor**

Decodes the received MAC PDUs and forwards the resulting MAC SDUs to their respective logical channels using the DEMUX component and forwards the UL Buffer Status Reports to the Scheduler. See mac_ul_processor

**MAC DL processor**

Manages the MAC scheduler. This is implemented in the :ref:`mac_dl_processor<mac_dl_processor>` class. 
