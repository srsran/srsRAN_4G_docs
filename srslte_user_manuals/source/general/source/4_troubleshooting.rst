.. _gen_troubleshooting:

Troubleshooting
==================

Building with Debug Symbols
**************************************

First make sure srsLTE has been downloaded, and you have created and navigated to the build folder::
  
  git clone https://github.com/srsLTE/srsLTE.git
  cd srsLTE
  mkdir build
  cd build
  
To build srsLTE with debug symbols, the following steps can be taken. If srsLTE has already been built, the original build folder should be cleared before proceeding.  
This can be done with the following command:: 

  rm -rf *
  make clean  

The following command can then be used to build srsLTE with debug symbols enabled::

  cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo ../
  make
  make test
  
The log file containing the debug info can be found in the ``srsLTE_backtrace.log`` file.

