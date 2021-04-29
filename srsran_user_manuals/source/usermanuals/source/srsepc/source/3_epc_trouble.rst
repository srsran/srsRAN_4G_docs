.. _epc_trouble:

Troubleshooting
===============

This section describes some of the most common issues with srsEPC and how to troubleshoot them.

UE did not attach
+++++++++++++++++

If the UE could not attach it is important to see at what point the attach procedure broke down.
The easiest way to do this is to inspect the NAS messages on the EPC PCAP. See the :ref:`observing_res` section for instructions on how to obtain a PCAP from srsEPC.

The most common reasons for an attach failure are either an :ref:`auth_failure` or a :ref:`mismatch_apn`. Some instructions on addressing these issues can be found on the subsections below.

.. _auth_failure:

Authentication failure
----------------------

The most common case of attach failure is authentication failure. In LTE, not only the network must authenticate the UE, but the UE must also authenticate the network.
For that reason, there is an authentication procedure within the attach procedure.

An simplified illustration of the messages involved in the authentication procedure can be found bellow:

.. seqdiag::

   seqdiag {
     === User Authentication Procedure ===
     UE -> MME [label = "Attach Request, PDN Connection Request"];
           MME -> HSS [label = "Auth Info Request (IMSI)"];
           MME <- HSS [label = "Auth Info Answer (Kasme, AUTN, RAND, XRES)"]
     UE <- MME [label = "NAS Authentication Request"];
     UE -> MME [label = "Authentication Response (RES)", note = "MME compares RES with XRES"];
  }

If when the MME compares the RES and XRES and these values do not match, that means that the keys used to generate those values are different and authentication fails.

For authentication, there are four important parameters that must be configured correctly both at the UE and the HSS: the IMSI, the authentication algorithm, the UE key and OP/OPc.
If you misconfigure your IMSI, you will see an `User not found. IMSI <Your_IMSI>` message in the epc.log. If you misconfigure the other parameters, you will see a "NAS Authentication Failure" message in the epc.pcap, with the failure code "MAC Code Failure."

Instructions on how to configure these parameters can be found in the :ref:`config_csv` section.

.. _mismatch_apn:

Mismatched APN
--------------

Within the attach procedure, the UEs sends an APN setting, either in the "PDN connectivity request" message or in the "ESM information transfer" message.
It is necessary that the configuration of the APN in the UE and the EPC match. Important parameters to check are the APN name, the PDN type (must be IPv4), and that no PAP/CHAP authentication is being used.

In srsUE you can configure these parameters in the NAS section of the ue.conf.
If using a COTS UE, go to your APN settings and make sure that the APN configured in the UE matches the one configured in the EPC.

I cannot access the Internet
++++++++++++++++++++++++++++

If the UE attached successfully and can ping the SPGW, that means that the attach procedure went well and that the UE was able to obtain the IP.

That means that not being able to access the Internet is a problem not with srsRAN, but with the network configuration of the system.
The most likely issue is that, by default, Linux will not forward packets from one subnet to another. See the :ref:`connecting_to_net` section on how to enable IP packet forwarding in Linux.
