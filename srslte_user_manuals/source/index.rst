
.. srsLTE documentation master file, created by
   sphinx-quickstart on Dec 13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

srsLTE User Manual
==================

What is srsLTE?
---------------

srsLTE is a free and open-source 4G LTE software suite. Using srsLTE, you can build a complete end-to-end 4G mobile network.

.. image:: .imgs/srs_architecture.png

The srsLTE suite includes:

- srsUE - a complete SDR LTE UE (User Equipment) application
- srsENB - a complete SDR LTE eNodeB (Basestation) application
- srsEPC - a light-weight LTE EPC (Core Network) implementation with MME, HSS and S/P-GW

All srsLTE software runs in linux with off-the-shelf compute and radio hardware.

Install the latest srsLTE release on Ubuntu::

   $ sudo add-apt-repository ppa:srslte/releases
   $ sudo apt-get update
   $ sudo apt-get install srslte -y

Source
------

| The srsLTE source code is available on `GitHub <https://github.com/srslte/srslte>`_.
| srsLTE is developed and maintained by `Software Radio Systems <https://softwareradiosystems.com>`_.

User Manuals
------------

.. toctree::
   :maxdepth: 1

   srsue/source/index.rst


.. toctree::
   :maxdepth: 1

   srsenb/source/index.rst


.. toctree::
   :maxdepth: 1

   srsepc/source/index.rst



