Getting Started
===============

To get started with srsEPC you will require a PC with a GNU/Linux based operating system.
This can be a distribution of your preference, such as Ubuntu, Debian, Fedora, etc.

If you are using Ubuntu, you can install from the binary packages provided::

  sudo add-apt-repository ppa:srslte/releases
  sudo apt-get update
  sudo apt-get install srsepc

If you are using a different distribution, you can install from source using the guide provided in the project's `GitHub page <https://github.com/srsLTE/srsLTE/>`_.

After installing the software you can install the configuration files into the default location (``~/.config/srslte``), by running::

  srslte_install_configs.sh user
 
Running the software
********************

To run srsEPC with default parameters, you can do ``sudo srsepc`` on the command line.
This will start the EPC and it will wait for eNBs and UEs to connect to it.

srsEPC will start a TUN interface ``srs_spgw_sgi`` that will allow user-plane packets to reach the UEs.

Configuration
*************

The EPC can be configured through two configuration files: ``epc.conf`` and ``user_db.csv``.
The ``epc.conf`` will hold general configuration parameters of the MME, SPGW and the HSS. 
This includes PLMN value, integrity/ciphering algorithms, APN, SGi IP address, GTP-U bind address, etc.

The ``user_db.csv`` is used to keep UE specific parameters for the HSS.
This will include IMSI, authentication algorithms, K, OP or OPc, etc. 

In the following subsections, we will cover a few common configuration cases with srsEPC: adding a new UE to the HSS database, running the eNB and EPC on separate machines, and setting up network routing to enable UEs to connect to the Internet.

Adding an UE to HSS database
++++++++++++++++++++++++++++

When adding a UE to be able to the ``user_db.csv`` database that the HSS will use, you must make sure that that parameters in that file match the parameters stored in the UE's USIM card.

Of particular relevance are the IMSI, authentication algorithm, K and OP or OPc (if using the MILENAGE algorithm).
The IMSI is the unique identifier of the SIM card, the K the secret key that the HSS and the UE use to authenticate each other.

The usual authentication algorithm used by SIM cards is MILENAGE, but there are also test SIMs that use XOR authentication.
If you are using the MILENAGE algorithm, you must also know whether you are using OP or OPc and the corresponding value of this parameter.

Once you know these parameters you can replace then in the user_db.csv which has the following format::

  (ue_name),(algo),(imsi),(K),(OP/OPc_type),(OP/OPc_value),(AMF),(SQN),(QCI),(IP_alloc)

So, if you have a SIM card with the following parameters:

  * MILENAGE algorithm
  * IMSI = 901700000000001
  * K = 00112233445566778899aabbccddeeff
  * Using OPc
  * OPc = 63bfa50ee6523365ff14c1f45f88737d

You can configure the ``user_db.csv`` like this::

  ue1,mil,901700000000001,00112233445566778899aabbccddeeff,opc,63bfa50ee6523365ff14c1f45f88737d,9000,000000000000,9,dynamic

eNBs and srsEPC on separate machines
++++++++++++++++++++++++++++++++++++

By default, srsEPC is configured to run with srsENB on the same machine.
When running srsEPC with an eNB on a separate machine, all that is necessary to configure is the ``mme_bind_addr`` and the ``gtpu_bind_addr``.

The MME bind address will specify where the MME will listen for eNB S1AP connections. The GTP-U bind address should be the same as the MME bind address, unless you want to run the user-plane on a different sub-net then the S1AP connection.

So if you want to listen to eNB on the interface with IP *10.0.1.10*, you can do::

  sudo srsepc --mme.mme_bind_addr 10.0.1.10 --spgw.gtpu_bind_addr 10.0.1.10

Connecting UEs to the Internet 
++++++++++++++++++++++++++++++

Often, it is interesting to connect the UEs to the Internet. By default, the Linux kernel will not do packet forwarding from one subnet to another subnet. Also, it is necessary to perform IP masquerading so that the UEs can connect to the Internet, even thought they only have a private IP.

To enable this, you can run a convenience script ``sudo srsepc_if_masq <out_interface>``, where *out_interface* is the interface that connects the PC to the Internet.

.. warning::

  *out_interface* is NOT the *srs_spgw_sgi* interface, but the Ethernet or WiFi ethernet that connects the PC to the Internet.

Observing results
*****************

By default, log files are stored in ``/tmp/epc.log``. This files can be inspected to troubleshoot any issues related to srsEPC.
Log files can have multiple verbosity levels, which can be configured in the ``epc.conf`` or through the command line. They can also be enabled on a per-layer capacity, which is usefull when troubleshooting a specific layer.

The EPC can also record PCAPs with the S1AP messages between the MME and the eNBs. 
This can be enabled on the ``epc.conf`` or command line, by setting the ``pcap.enable`` value to true.
For wireshark to interpret the pcap correctly, it's necessary to associate the Wireshark S1AP dissector and with the value DLT of 150. 
To use the dissector, go to the preferences in Wireshark and edit DLT_USER to add an entry with DLT=150, Payload Protocol=s1ap.

