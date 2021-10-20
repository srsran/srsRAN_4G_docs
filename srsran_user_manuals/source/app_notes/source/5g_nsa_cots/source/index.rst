.. srsRAN 5G NSA COTS UE Application Note

.. _5g_nsa_cots_appnote:

5G NSA COTS UE
##############

.. tip::
   Operating a private 5G NSA network on cellular frequency bands may be tightly regulated in your jurisdiction. Seek the approval 
   of your telecommunications regulator before doing so.



Introduction
************

This application note aims to demonstrate how to set up your own 5G NSA network using srsENB, srsEPC and a 5G capable COTS UE. There 
are two options for network set-up when connecting a COTS UE: The network can be left as is, and the UE can communicate locally 
within the network, or the EPC can be connected to the internet through the P-GW, allowing the UE to access the internet for 
web-browsing, email etc. 

Network & Hardware Overview
***************************

 .. figure:: .imgs/NSA_COTS.png
    :align: center
    
    Simplified network architecture

Setting up a 5G NSA network and connecting a 5G COTS UE requires the following: 

 - PC with a Linux based OS, with srsRAN installed and built
 - An dual channel RF-frontend capable of Tx & Rx, with an RF chain for each 
 - A 5G COTS UE 
 - USIM/ SIM card (This must be a test card or a programmable card, with known keys)

For this implementation the following equipment is used: 
	
	- Dell XPS-13 (10th Gen i7)
	- X300 USRP
	- OnePlus Nord 5G with a Sysmocom USIM 

RF-Frontend 
===========

<Why we need 2 rf chains>

COTS UE
=======

<what features must the phone have>
<sim being used>

Dependencies
************

RF Driver
=========

You should make sure that your RF-frontend driver is correct for your device and up to date. Some of the most common drivers
can be found here: 

  * `UHD <https://github.com/EttusResearch/uhd>`_ [for UHD we recommend using v3.15]
  * `SoapySDR <https://github.com/pothosware/SoapySDR>`_
  * `BladeRF <https://github.com/Nuand/bladeRF>`_

srsRAN
======

If you have not already done so, install the latest version of srsRAN and it's dependencies. This is outlined in the :ref:`installation guide <gen_installation>`. 

.. note::
   If you install or update your driver **after** installing srsRAN, you will have to re-build srsRAN. This is because if the driver is not present 
   at build time, srsRAN will not recongnise it at run-time. 

Checking Drivers
================

To check that your RF driver has been picked up when running ``cmake ..`` during the build process, you can run: 

``grep <driver> srsRAN/build/CMakeCache.txt``

If you are using UHD as your driver, you should see the following output if srsRAN has successfully deteced it when ``cmake ..`` was run:: 

   $ grep UHD -m 4 CMakeCache.txt 

   //Enable UHD
   ENABLE_UHD:BOOL=ON
   UHD_INCLUDE_DIRS:PATH=/usr/local/include
   UHD_LIBRARIES:FILEPATH=/usr/local/lib/libuhd.so

Configuration
**************

The network will have to be configured to support the NSA network and to work with a COTS UE. The following srsRAN configuration files will need to be 
updated: 

  * enb.conf
  * rr.conf
  * epc.conf
  * user_db.csv 
 

The enb.conf and epc.conf files will need to be edited such that the MCC & MNC values are the same as those associated with the SIM/ USIM. 
The rr.conf needs to be updated to add the NR cell. The user_db.csv file needs to be updated so that it contains the credentials associated with the USIM card being used in the UE.

An APN will also need to be added to the COTS UE to allow it to access the internet. This is created from the UE and reflected in the EPC config file. 

The configuration files used for this example set-up are attached above for reference. Users will have to edit the relevant fields so that their COTS UE will be 
supported by the network. 

Add APN to COTS UE
==================

To add an APN to the UE navigate to the Network settings for the SIM being used. From here an APN can be added, usually under ``Access point names``. Create 
a new APN with the name and APN ``test123``, as shown in the following figure. 

	.. image:: .imgs/apn_ue.jpg
		:align: center
		:height: 500px

All of the other settings can be left on the default options. The name of the APN here does not actually matter, so long as the naming is consistent between the UE and the EPC.

srsENB
======

enb.conf
--------

The ``MCC`` & ``MNC`` codes must be updated in the enb.conf to reflect the values used by the sim. These can be edited in the following section of the config file:: 

	#####################################################################
	[enb]
	enb_id = 0x19B
	mcc = 901
	mnc = 70
	mme_addr = 127.0.1.100
	gtp_bind_addr = 127.0.1.1
	s1c_bind_addr = 127.0.1.1
	n_prb = 50
	#tm = 4
	#nof_ports = 2
	
	#####################################################################

The rest of the options can be left at the default values. They may be changed as needed, but further modification 
is not necessary to enable the successful connection of a COTS UE. 

<does the EARFCN need to be changed?>

rr.conf 
--------

The main change to the rr.conf file is the addition of the NR cell to the cell list. This is added to the end of the file:: 

	nr_cell_list =
	(
	   {
	    rf_port = 1;
	    cell_id = 0x02;
	    tac = 0x0007;
	    pci = 500;
	    root_seq_idx = 204;

	    // TDD:
	    //dl_arfcn = 634240;
	    //band = 78;

	    // FDD:
	    dl_arfcn = 368500;
	    band = 3;
	  }
	);

Here we have added both the TDD and FDD configs. For this example we will be using the FDD configuration, so the TDD configuration is commented out. The TDD and FDD configs can be swapped 
by stopping srsENB, making the necessary changes to this file, and restarting srsENB. So long as the UE supports both. If the UE only supports one then that should be used.  

<choosing bands?>

Core 
====

epc.conf
--------

The EPC config file must be modificed to reflect the ``MCC`` & ``MNC``, as well as the ``APN`` being used by the UE:: 
	
	#####################################################################
	[mme]
	mme_code = 0x1a
	mme_group = 0x0001
	tac = 0x0007
	mcc = 901
	mnc = 70
	mme_bind_addr = 127.0.1.100
	apn = test123
	dns_addr = 8.8.8.8
	encryption_algo = EEA0
	integrity_algo = EIA1
	paging_timer = 2
	
	#####################################################################

user_db.csv
-----------

The following list describes the fields contained in the ``user_db.csv`` file. As standard, this file 
will come with two dummy UEs entered into the CSV, these help to provide an example of how the file should be filled in. 

	- Name: Any human readable value
	- Auth: Authentication algorithm (xor/ mil)
	- IMSI: UE's IMSI value
	- Key: UE's key, hex value
	- OP Type: Operator's code type (OP/ OPc)
	- OP: OP/ OPc code, hex value
	- AMF: Authentication management field, hex value must be above 8000
	- SQN: UE's Sequence number for freshness of the authentication
	- QCI: QoS Class Identifier for the UE's default bearer
	- IP Alloc: IP allocation strategy for the SPGW

The AMF, SQN, QCI and IP Alloc fields can be populated with the following values for the COTS UE: 
	
	- 9000, 000000000000, 9, dynamic

This will result in a user_db.csv file that should look something like the following:: 

	1 | #                                                                                           
	2 | # .csv to store UE's information in HSS                                                     
	3 | # Kept in the following format: "Name,Auth,IMSI,Key,OP_Type,OP,AMF,SQN,QCI,IP_alloc"      
	4 | #                                                                                           
	5 | # Name:     Human readable name to help distinguish UE's. Ignored by the HSS                
	6 | # IMSI:     UE's IMSI value                                                                 
	7 | # Auth:     Authentication algorithm used by the UE. Valid algorithms are XOR               
	8 | #           (xor) and MILENAGE (mil)                                                        
	9 | # Key:      UE's key, where other keys are derived from. Stored in hexadecimal              
	10| # OP_Type:  Operator's code type, either OP or OPc                                          
	11| # OP/OPc:   Operator Code/Cyphered Operator Code, stored in hexadecimal                     
	12| # AMF:      Authentication management field, stored in hexadecimal                          
	13| # SQN:      UE's Sequence number for freshness of the authentication                        
	14| # QCI:      QoS Class Identifier for the UE's default bearer.                               
	15| # IP_alloc: IP allocation stratagy for the SPGW.                                            
	16| #           With 'dynamic' the SPGW will automatically allocate IPs                         
	17| #           With a valid IPv4 (e.g. '172.16.0.2') the UE will have a statically assigned IP.
	18| #                                                                                           
	19| # Note: Lines starting by '#' are ignored and will be overwritten                           
	20| COTS_UE,mil,901700000020936,4933f9c5a83e5718c52e54066dc78dcf,opc,fc632f97bd249ce0d16ba79e6505d300,9000,0000000060f8,9,dynamic

The auth, IMSI, key, OP Type and OP are values associated with the sim being used. The values assigned to the AMF, SQN, QCI & IP Alloc are the default values above, which is 
explained further :ref:`here <config_csv>` in the EPC documentation. Ensure there is no white space between the values in each entry, as this will cause 
the file to be read incorrectly. 

<what are our values?>

Masquerading Script
===================

To allow UE to connect to the internet via the EPC, the pre-configured masquerading script must be run. This can be found in ``srsRAN/srsepc``. 

The masquerading script enables IP forwarding and sets up Network Address Translation to pass traffic between the srsRAN network and the external network. 
The script must be run each time the machine is re-booted, and can be done before or while the srsRAN is running. The UE will not be able to communicate 
with the interet until this script has been run. 

Before running the script it is important to identify the interface being used to connect your PC to the internet. As the script requires this to be passed 
in as an argument. This can be done by running the following command:: 

   route

You will see an output similar to the following:: 

   Kernel IP routing table
   Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
   default         _gateway        0.0.0.0         UG    100    0        0 enxc03ebab05013
   10.12.1.0       0.0.0.0         255.255.255.0   U     100    0        0 enxc03ebab05013


The interface (Iface) associated with the *default* destination is one which must be passed into the masq. script. In the above output that is the ``enxc03ebab05013`` interface. 

The masq. script can now be run from the follow folder: ``srsRAN/srsEPC`` :: 

	sudo ./srsepc_if_masq.sh <interface>

If it has executed successfully you will see the following message::

	Masquerading Interface <interface>
	
The configuration files, user DB and UE are now set up appropriately to allow the COTS UE to connect to the eNB and Core. 


Network Set-up
**************

<RUN EXPERIMENT>

Core
==== 

gNB
=====


UE
===

Ping
==== 

Limitations
***********

<HARDWARE AND SOFTWARE>

Troubleshooting
***************