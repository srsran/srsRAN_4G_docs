Introduction
============

Overview
********

srsEPC is a lightweight implementation of a complete LTE core network (EPC). The srsEPC application runs as a single binary but provides the key EPC components of Home Subscriber Service (HSS), Mobility Management Entity (MME), Service Gateway (S-GW) and Packet Data Network Gateway (P-GW).

.. figure:: .imgs/epc_basic.svg
    :align: center
    :alt: alternate text
    :figclass: align-center

    EPC overall architecture

The figure above illustrates the main components of the EPC, along with the main interfaces between them.

* *HSS*: The Home Subscriber Service (HSS) is the user database. It stores information such as the user's id, key, usage limits, etc. It is responsible for authenticating an authorizing the user's access to the network.

* *MME*: Mobility Managment Entity (MME) is the main control element in the network. It handles mobility and attach control messages. It is also responsible for paging UEs in idle mode.

* *S-GW*: The S-GW is the main dataplane gateway for the users, as it provides the mobility anchor for the UEs. It works as an IP router and helps setting up GTP sessions between the eNB and the P-GW.

* *P-GW*: The Packet Gateway (P-GW) is the point of contact with external networks. It enforces the QoS parameters for subscriber sessions.

To provide a complete end-to-end LTE network, use srsEPC with srsENB and srsUE.

This User Guide provides all the information needed to get up and running with the srsEPC application, to become familiar with all of the key features and to achieve optimal performance. For information on extending or modifying the srsEPC source code, please see the srsEPC Developers Guide.

Features
********

The srsEPC LTE core network includes the implementation of the MME, HSS and SPGW entities.
The features of each of these entities is furthered described below.

MME Features
++++++++++++

The srsEPC MME entity provides support for standard compliant NAS and S1AP protocols to provide control plane communication between the EPC and the UEs and eNBs.

At the NAS level, this includes:

* Attach procedure, detach procedure, service request procedure
* NAS Security Mode Command, Identity request/response, authentication  
* Support for the setup of integrity protection (EIA1 and EIA2) and ciphering (EEA0, EEA1 and EEA2)

At the S1AP level, this includes:

* S1-MME Setup/Tear-down
* Transport of NAS messages 
* Context setup/release procedures
* Paging procedures

HSS Features
++++++++++++

The srsEPC HSS entity provides support for configuring UE's authentication parameters and other parameters that can be configured on a per-UE basis.
The HSS entity includes the following features:

* Simple CSV based database
* XOR and MILENAGE authentication algorithms, specified per UE.
* QCI information
* Dynamic or static IP configuration of UEs

SPGW Features
+++++++++++++

The srsEPC SPGW entity provides support for to user plane communication between the EPC and the and eNBs, using S1-U and SGi interfaces.

The SPGW supports the following features:

* SGi interface exposed as a virtual network interface (TUN device)
* SGi < − > S1-U Forwarding using standard compliant GTP-U protocol
* Support of GTP-C procedures to setup/teardown GTP-U tunnels 
* Support for Downlink Data Notification procedures

