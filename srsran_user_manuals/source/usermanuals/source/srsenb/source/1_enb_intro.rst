.. _enb_intro:

Introduction
============

.. image:: .imgs/srsenb_logo.png

Overview
********

SrsENB is an LTE eNodeB basestation implemented entirely in software. Running as an application on a standard Linux-based operating system, srsENB connects to any LTE core network (EPC) and creates a local LTE cell. To transmit and receive radio signals over the air, srsENB requires SDR hardware such as the Ettus Research USRP.

To provide an end-to-end LTE network, use srsENB with srsEPC and srsUE.

This User Guide provides all the information needed to get up and running with the srsENB application, to become familiar with all of the key features and to achieve optimal performance. For information on extending or modifying the srsENB source code, please see the srsENB Developers Guide.

Features
********

The srsENB LTE eNodeB includes the following features:

- LTE Release 10 aligned
- FDD configuration
- Tested bandwidths: 1.4, 3, 5, 10, 15 and 20 MHz
- Transmission mode 1 (single antenna), 2 (transmit diversity), 3 (CCD) and 4 (closed-loop spatial multiplexing)
- Frequency-based ZF and MMSE equalizer
- Evolved multimedia broadcast and multicast service (eMBMS)
- Highly optimized Turbo Decoder available in Intel SSE4.1/AVX2 (+150 Mbps)
- Detailed log system with per-layer log levels and hex dumps
- MAC layer wireshark packet capture
- Command-line trace metrics
- Detailed input configuration files
- Channel simulator for EPA, EVA, and ETU 3GPP channels
- ZeroMQ-based fake RF driver for I/Q over IPC/network
- Intra-ENB and Inter-ENB (S1) mobility support
- Proportional-fair and round-robin MAC scheduler with FAPI-like C++ API
- SR support
- Periodic and Aperiodic CQI feedback support
- Standard S1AP and GTP-U interfaces to the Core Network
- 150 Mbps DL in 20 MHz MIMO TM3/TM4 with commercial UEs (195 Mbps with QAM256)
- 75 Mbps DL in SISO configuration with commercial UEs
- 50 Mbps UL in 20 MHz with commercial UEs
- User-plane encryption

srsENB has been tested and validated with a broad range of COTS handsets including:

- LG Nexus 5 and 4
- Motorola Moto G4 plus and G5
- Huawei P9/P9lite, P10/P10lite, P20/P20lite
- Huawei dongles: E3276 and E398

eNodeB architecture
*******************

.. figure:: .imgs/enb_basic.svg
    :width: 400px
    :align: center
    :alt: alternate text
    :figclass: align-center

    Basic eNodeB Architecture

The srsENB application includes layers 1, 2 and 3 as shown in the figure above.

At the bottom of the protocol stack, the Physical (PHY) layer carries all information from the MAC over the air interface. It is responsible for link adaptation and power control.

The Medium Access Control (MAC) layer multiplexes data between one or more logical channels into Transport Blocks (TBs) which are passed to/from the PHY layer. The MAC is responsible for scheduling uplink and downlink transmissions for connected UEs via control signalling, retransmission and error correction (HARQ) and priority handling between logical channels.

The Radio Link Control (RLC) layer can operate in one of three modes: Transparent Mode (TM), Unacknowledged Mode (UM) and Acknowledged Mode (AM). The RLC manages multiple logical channels or bearers for each connected UE. Each bearer operates in one of these three modes. Transparent Mode bearers simply pass data through the RLC. Unacknowledged Mode bearers perform concatenation, segmentation and reassembly of data units, reordering and duplication detection. Acknowledged Mode bearers additionally perform retransmission of missing data units and resegmentation.

The Packet Data Convergence Protocol (PDCP) layer is responsible for ciphering of control and data plane traffic, integrity protection of control plane traffic, duplicate discarding and in-sequence delivery of control and data plane traffic to/from the RRC and GTP-U layers respectively. The PDCP layer also performs header compression (ROHC) of IP data if supported.

The Radio Resource Control (RRC) layer manages control plane exchanges between the eNodeB and connected UEs. It generates the System Information Blocks (SIBs) broadcast by the eNodeB and handles the establishment, maintenance and release of RRC connections with the UEs. The RRC also manages security functions for ciphering and integrity protection between the eNodeB and UEs.

Above the RRC, the S1 Application Protocol (S1-AP) layer provides the control plane connection between the eNodeB and the core network (EPC). The S1-AP connects to the Mobility Management Entity (MME) in the core network. Messages from the MME to UEs are forwarded by S1-AP to the RRC layer, where they are encapsulated in RRC messages and sent down the stack for transmission. Messages from UEs to the MME are similarly encapsulated by the UE RRC and extracted at the eNodeB RRC before being passed to the S1-AP and on to the MME.

The GPRS Tunnelling Protocol User Plane (GTP-U) layer within srsENB provides the data plane connection between the eNodeB and the core network (EPC). The GTP-U layer connects to the Serving Gateway (S-GW) in the core network. Data plane IP traffic is encapsulated in GTP packets at the GTP-U layer and these GTP packets are tunneled through the EPC. That IP traffic is extracted from the tunnel at the Packet Data Network Gateway (P-GW) and passed out into the internet.
