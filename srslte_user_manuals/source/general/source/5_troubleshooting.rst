.. _gen_troubleshooting:

Troubleshooting
==================

Building with Debug Symbols
**************************************

First make sure srsRAN has been downloaded, and you have created and navigated to the build folder::
  
  git clone https://github.com/srsran/srsran.git
  cd srsran
  mkdir build
  cd build
  
To build srsRAN with debug symbols, the following steps can be taken. If srsRAN has already been built, the original build folder should be cleared before proceeding.  
This can be done with the following command:: 

  rm -rf *
  make clean  

The following command can then be used to build srsRAN with debug symbols enabled::

  cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo ../
  make
  make test
  
The log file containing the debug info can be found in the ``srsran_backtrace.log`` file.

.. _Wireshark:

Examining PCAPs with Wireshark
******************************

The srsRAN applications support packet capture at the MAC and NAS layers of the network stack.

Packet capture files (pcaps) can be viewed using Wireshark (www.wireshark.org). pcaps are encoded in compact mac-lte-framed form. They can be found in the */tmp* folder where other logs are located. 
To view in wireshark, edit the preferences of the DLT_USER dissector. 

Add an entry with the following to decode MAC pcaps:

	* DLT=147
	* Payload Protocol=mac-lte-framed
	
To decode NAS pcaps add and entry with the following: 

	* DLT=148
	* Payload Protocol=nas-eps

For more information, see https://wiki.wireshark.org/MAC-LTE.

