Introduction
============

Overview
********

SrsENB is an LTE eNodeB basestation implemented entirely in software. Running as an application on a standard Linux-based operating system, srsENB connects to any LTE core network (EPC) and creates a local LTE cell. To transmit and receive radio signals over the air, srsENB requires SDR hardware such as the Ettus Research USRP.

To provide an end-to-end LTE network, use srsENB with srsEPC and srsUE.

This User Guide provides all the information needed to get up and running with the srsENB application, to become familiar with all of the key features and to achieve optimal performance. For information on extending or modifying the srsENB source code, please see the srsENB Developers Guide.

Features
********

The srsENB LTE eNodeB includes the following features:

.. note::  To be updated.

- LTE Release 15 compliant
- TDD and FDD configurations
- Tested bandwidths: 1.4, 3, 5, 10, 15 and 20 MHz
- Transmission modes 1 (single antenna), 2 (transmit diversity), 3 (CCD) and 4 (closed-loop spatial multiplexing)
- Manually configurable DL/UL carrier frequencies
- Soft USIM supporting XOR/Milenage authentication
- Hard USIM support via PC/SC
- Snow3G and AES integrity/ciphering support
- TUN virtual network kernel interface integration for Linux OS
- Detailed log system with per-layer log levels and hex dumps
- MAC and NAS layer wireshark packet captures
- Command-line trace metrics
- Detailed input configuration files
- Evolved multimedia broadcast and multicast service (eMBMS)
- Frequency-based ZF and MMSE equalizers
- Highly optimized Turbo Decoder available in Intel SSE4.1/AVX2 (+100 Mbps) and standard C (+25 Mbps)
- Supports Ettus USRP B2x0/X3x0 families, BladeRF, LimeSDR

eNodeB architecture
*******************

.. figure:: .imgs/ENB_Architecture_Basic.svg
    :width: 400px
    :align: center
    :alt: alternate text
    :figclass: align-center

    Basic eNodeB Architecture

The srsUE application includes layers 1, 2 and 3 as shown in the figure above.

At the bottom of the UE protocol stack, the Physical (PHY) layer carries all information from the MAC over the air interface. It is responsible for link adaptation, power control, cell search and cell measurement.

The Medium Access Control (MAC) layer multiplexes data between one or more logical channels into Transport Blocks (TBs) which are passed to/from the PHY layer. The MAC is responsible for control and scheduling information exchange with the eNodeB, retransmission and error correction (HARQ) and priority handling between logical channels.

The Radio Link Control (RLC) layer can operate in one of three modes: Transparent Mode (TM), Unacknowledged Mode (UM) and Acknowledged Mode (AM). The RLC manages multiple logical channels or bearers, each of which operates in one of these three modes. Transparent Mode bearers simply pass data through the RLC. Unacknowledged Mode bearers perform concatenation, segmentation and reassembly of data units, reordering and duplication detection. Acknowledged Mode bearers additionally perform retransmission of missing data units and resegmentation.

The Packet Data Convergence Protocol (PDCP) layer is responsible for ciphering of control and data plane traffic, integrity protection of control plane traffic, duplicate discarding and in-sequence delivery of control and data plane traffic to/from the RRC and GW layers respectively. The PDCP layer also performs header compression (ROHC) of IP data if supported.

The Radio Resource Control (RRC) layer manages control plane exchanges between the UE and the eNodeB. It uses System Information broadcast by the network to configure the lower layers of the UE and handles the establishment, maintenance and release of the RRC connection with the eNodeB. The RRC manages cell search to support cell selection as well as cell measurement reporting and mobility control for handover between neighbouring cells. The RRC is also responsible for handling and responding to paging messages from the network. Finally, the RRC manages security functions for key management and the establishment, configuration, maintenance and release of radio bearers.

The Non-Access Stratum (NAS) layer manages control plane exchanges between the UE and entities within the core network (EPC). It controls PLMN selection and manages network attachment procedures, exchanging identification and authentication information with the EPC. The NAS is responsible for establishing and maintaining IP connectivity between the UE and the PDN gateway within the EPC.

The Gateway (GW) layer within srsUE is responsible for the creation and maintenance of the TUN virtual network kernel interface, simulating a network layer device within the Linux operating system. The GW layer permits srsUE to run as a user-space application and operates with data plane IP packets.
