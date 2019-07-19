.. _ue_advanced:

Advanced Usage
==============

MIMO
****

External USIM
*************

Using an actual SIM card to authenticate the user against the network is an advanced feature.
It requires a SIM card reader attached to the PC running srsUE that is supported by
`PCSClite <https://pcsclite.apdu.fr/>`_.

Before using a SIM card, please make sure to disable PIN activation using a regular phone.

In order to compile srsUE with support for it, the pcsclite development headers as well as the
pcsc daemon need to be installed and running.
On Ubuntu (or other Debian derivates), this can be done with::

    sudo apt-get install libpcsclite-dev pcscd pcsc-tools

After this is done, please verify you've got a PCSC-compatible reader by running 'pcsc_scan'.

Now, CMake should pick up the pcsc libraries and build the support code for it. If that is not the case,
try with a clean build folder or remove your exisiting ``CMakeCache.txt``::

    $ cmake ..
    ...
    -- PCSC LIBRARIES: /usr/lib/x86_64-linux-gnu/libpcsclite.so
    -- PCSC INCLUDE DIRS: /usr/include/PCSC
    -- Building with PCSC support.
    ...
    $ make

After the build is complete, you can verify the correct operation with the ``pcsc_usim_test`` application.
Please verify that the IMSI can be read from the card::


    $ ./srsue/test/upper/pcsc_usim_test
    ..
    09:06:36.064073 [USIM] [D] SCARD: MNC length=2
    09:06:36.064079 [USIM] [D] MNC length 2
    IMSI: 21XXXXXXXXXXXX
    09:06:36.064095 [USIM] [D] SCARD: UMTS auth - RAND
                 0000: bc 4c b0 27 b3 4b 7f 51 21 5e 56 5f 67 3f de 4f
    09:06:36.064102 [USIM] [D] SCARD: UMTS auth - AUTN
                 0000: 5a 17 77 3c 62 57 90 01 cf 47 f7 6d b3 a0 19 46
    09:06:36.064107 [USIM] [D] SCARD: scard_transmit: send
                 0000: 00 11 00 81 22 10 bc ac b1 17 13 4b 6f 51 21 5e
                 0010: 47 47 6d b3 a0 19 46
    09:06:36.119675 [USIM] [D] SCARD: SCardTransmit: recv
                 0000: 98 62
    09:06:36.119707 [USIM] [D] SCARD: UMTS alg response
                 0000: 98 62
    09:06:36.119717 [USIM] [W] SCARD: UMTS auth failed - MAC != XMAC
    09:06:36.119725 [USIM] [E] SCARD: Failure during USIM UMTS authentication
    09:06:36.119732 [USIM] [D] SCARD: deinitializing smart card interface


If those steps completed successfully we can now start srsUE by either enabling the PCSC USIM in
the config file or by passing the option as an command line argument, e.g., run::

    $ ./srsue/src/srsue --usim.mode=pcsc

eMBMS
*****

Carrier Aggregation
*******************

TDD
***


