.. _feature_list:

srsRAN 4G Features
------------------

srsUE
*****

srsUE is a 4G LTE UE modem with prototype 5G NR features implemented entirely in software. Running as 
an application on a standard Linux-based operating system, srsUE connects to any LTE 
network and provides a standard network interface with high-speed mobile connectivity.

The SRS UE includes the following features:

- LTE Release 10 aligned with features up to release 15
- Prototype 5G NSA and SA support
- TDD and FDD configurations
- Tested LTE bandwidths: 1.4, 3, 5, 10, 15 and 20 MHz
- Tested 5G SA bandwidths: 5, 10, 15 and 20 MHz
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
- Highly optimized Turbo Decoder available in Intel SSE4.1/AVX2 (+150 Mbps)
- Channel simulator for EPA, EVA, and ETU 3GPP channels
- QoS support
- 150 Mbps DL in 20 MHz MIMO TM3/TM4 or 2xCA configuration (195 Mbps with QAM256)
- 75 Mbps DL in 20 MHz SISO configuration (98 Mbps with QAM256)
- 36 Mbps DL in 10 MHz SISO configuration
- Supports Ettus USRP B2x0/X3x0 families, BladeRF, LimeSDR

Read the :ref:`UE User Manual <ue_intro>`. for further info on the UE.

srsENB
******

The srsENB LTE eNodeB includes the following features:

- LTE Release 10 aligned with features up to release 15
- Prototype 5G NR support for both 5G NSA and SA 
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

Read the :ref:`ENB User Manual <enb_intro>`. for further info on the eNB.

srsEPC
******

srsEPC is a lightweight implementation of a complete LTE core network (EPC). The 
srsEPC application runs as a single binary but provides the key EPC components 
of Home Subscriber Service (HSS), Mobility Management Entity (MME), Service Gateway 
(S-GW) and Packet Data Network Gateway (P-GW). The srsEPC application is not intended
for deployment but can be used for testing.

Read the :ref:`EPC User Manual <epc_intro>`. for further info on the EPC.


