.. _gen_release_notes:

Release Notes
=============

- 22.10

  * Fix DL NAS integrity checks in srsUE
  * Remove Travis and LGTM as CI platforms
  * Remove polarssl as optional dependency (only mbedTLS used and required for security)
  * Allow to specify multiple PLMNs in SIB1
  * Allow non-blocking S1AP connect and expose various other SCTP options
  * Add support to broadcast MAC backoff indicator
  * Seperate T300/T301 timer in srsENB
  * Fix in eMBMS payload buffer handling
  * Fix memleak in NR scheduler

* 22.04.1

  * Bug-fixes in RLC AM and PDCP in NR
  * Fix for UE crashing when attempting to re-establish connection in SA mode
  * Removed fixed coreset0 index for SSB
  * Added support for SIB5 and SIB6 transmission in LTE

- 22.04

  * Added baseline 5G-SA support to srsUE and srsENB
  * Added dynamic loading of RF libraries
  * Added RRC Redirect to srsUE
  * Added support for A5 measurement events to srsENB
  * Added Crest Factor Reduction (CFR) for srsENB downlink and srsUE uplink on LTE carriers
  * Raise C++ standard to C++14
  * Other bug-fixes and improved stability and performance in all parts

* 21.10

  * Created initial version of srsGNB supporting NSA mode with srsENB
  * srsGNB tested with OnePlus Nord 5G
  * Improved interoperability of srsUE in NSA mode
  * Added enhanced instrumentation to file using JSON format
  * Fixed stability issues with Ettus N310
  * Added BLER-adaptive MCS scheduling to srsENB
  * Other bug-fixes and improved stability and performance in all parts

- 21.04

  * Rename project from srsLTE to srsRAN
  * Add initial 5G NSA support to srsUE (including x86-optimized FEC and PHY layer)
  * Add PDCP discard support
  * Add UL power control, measurement gaps and a new proportional fair scheduler to srsENB
  * Extend GTP-U tunneling to support tunnel forwarding over S1
  * Optimize many data structures, remove dynamic memory allocations in data plane
  * Improved S1AP error handling and enhanced event reporting
  * Update ASN.1 packing/unpacking, RRC to Rel 15.11, S1AP to Rel 16.1
  * Update PCAP writer to use UDP framing
  * Other bug-fixes and improved stability and performance in all parts

* 20.10.1

  * Fix eNB issue relating to uplink hybrid ARQ

- 20.10

  * EUTRA mobility support
  * Fix for QAM256 support for eNB
  * New logging framework
  * PHY optimizations
  * Other performance and stability improvements

* 20.04.1

  * Fix for UE MIMO segfault issue
  * Fix for eNodeB SR configuration
  * Clang compilation warning fixes
  * Fix GPS tracking synchronization

- 20.04

  * Carrier Aggregation and Time Alignment in srsENB
  * Complete Sidelink PHY layer (all transmission modes)
  * Complete NB-IoT PHY downlink signals
  * New S1AP packing/unpacking library
  * EVM and EPRE measurements
  * Remove system timers in srsUE and srsENB
  * Refactor eNB to prepare for mobility support
  * Other bug-fixes and improved stability and performance in all parts

* 19.12

  * Add 5G NR RRC and NGAP ASN1 packing/unpacking
  * Add sync routines and broadcast channel for Sidelink
  * Add cell search and MIB decoder for NB-IoT
  * Add PDCP discard
  * Improve RRC Reestablishment handling
  * Improve RRC cell measurements and procedure handling
  * Add multi-carrier and MIMO support to ZMQ radio
  * Refactor eNB scheduler to support multiple carriers
  * Apply clang-format style on entire code base
  * Other bug-fixes and improved stability and performance in all parts

- 19.09

  * Add initial support for NR in MAC/RLC/PDCP
  * Add sync code for NB-IoT
  * Add support for EIA3/EEA3 (i.e. ZUC)
  * Add support for CSFB in srsENB
  * Add adaptation layer to run TTCN-3 conformance tests for srsUE
  * Add High Speed Train model to channel simulator
  * Rework RRC and NAS layer and make them non-blocking
  * Fixes in ZMQ, bladeRF and Soapy RF modules
  * Other bug-fixes and improved stability and performance in all parts

* 19.06

  * Add QAM256 support in srsUE
  * Add QoS support in srsUE
  * Add UL channel emulator
  * Refactor UE and eNB architecture
  * Many bug-fixes and improved stability and performance in all parts

- 19.03

  * PHY library refactor
  * TDD support for srsUE
  * Carrier Aggregation support for srsUE
  * Paging support for srsENB and srsEPC
  * User-plane encryption for srsENB
  * Channel simulator for EPA, EVA, and ETU 3GPP channels
  * ZeroMQ-based fake RF driver for I/Q over IPC/network
  * Many bug-fixes and improved stability and performance in all parts

* 18.12

  * Add new RRC ASN1 message pack/unpack library
  * Refactor EPC and add encryption support
  * Add IPv6 support to srsUE
  * Fixed compilation issue for ARM and AVX512
  * Add clang-format file
  * Many bug-fixes and improved stability and performance in all parts

- 18.09

  * Improved Turbo Decoder performance
  * Configurable SGi interface name and M1U params
  * Support for GPTU echo mechanism
  * Added UE detach capability
  * Refactor RLC/PDCP classes
  * Various fixes for ARM-based devices
  * Added support for bladeRF 2.0 micro
  * Many bug-fixes and improved stability and performance in all parts

* 18.06.1

  * Fixed RLC reestablish
  * Fixed aperiodic QCI retx
  * Fixed eNB instability
  * Fixed Debian packaging

- 18.06

  * Added eMBMS support in srsUE/srsENB/srsEPC
  * Added support for hard SIM cards
  * Many bug-fixes and improved stability and performance in all parts

* 18.03.1

  * Fixed compilation for NEON
  * Fixed logging and RLC AM issue

- 18.03

  * Many bug-fixes and improved stability and performance in all parts

* 17.12

  * Added support for MIMO 2x2 in srsENB (i.e. TM3/TM4)
  * Added srsEPC, a light-weight core network implementation
  * Added support for X2/S1 handover in srsUE
  * Added support for user-plane encryption in srsUE
  * Many bug-fixes and improved stability and performance in srsUE/srsENB

- 17.09

  * Added MIMO 2x2 in the PHY layer and srsUE (i.e. TM3/TM4)
  * eMBMS support in the PHY layer
  * Many bug-fixes and improved stability and performance in srsUE/srsENB

* 002.000.000

  * Added fully functional srsENB to srsRAN code
  * Merged srsUE code into srsRAN and reestructured PHY code 
  * Added support for SoapySDR devices (eg LimeSDR)
  * Fixed issues in RLC AM 
  * Added support for NEON and AVX in many kernels and Viterbi decoder
  * Added support for CPU affinity
  * Other minor bug-fixes and new features 

- 001.004.000

  * Fixed issue in rv for format1C causing incorrect SIB1 decoding in some networks
  * Improved PDCCH decoding BER (fixed incorrect trellis initialization)
  * Improved PUCCH RX performance

* 001.003.000

  * Bugfixes: 
    
    * x300 master clock rate
    * PHICH: fixed bug causing more NACKs
    * PBCH: fixed bug in encoding function
    * channel estimation: fixed issue in time interpolation
    * DCI: Fixed bug in Format1A packing
    * DCI: Fixed bug in Format1C for RA-RNTI
    * DCI: Fixed overflow in MIMO formats
  
  * Improvements: 
    
    * Changed and cleaned DCI blind search API
    * Added eNodeB PHY processing functions

- 001.002.000

  * Bugfixes: 
  
    * Estimation of extrapolated of out-of-band carriers 
    * PDCCH REG interleaving for certain cell IDs
    * MIB decoding 
    * Overflow in viterbi in PBCH

  * Improvements: 
  
    * Synchronization in long multipath channels
    * Better calibration of synchronization and estimation
    * Averaging in channel estimation
    * Improved 2-port diversity decoding


* 001.001.000

  * Added support for BladeRF
