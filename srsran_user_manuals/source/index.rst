
.. srsRAN documentation master file, created by
   sphinx-quickstart on Dec 13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

srsRAN |version| Documentation
==============================

.. image:: .imgs/srsran_architecture.png

.. meta::
    :description lang=en:
        Documentation for the srsRAN 4G/5G project. User manuals for the srsRAN UE, 
        eNodeB, gNodeB and EPC applications. Up-to-date installation guides. Step-by-step 
        application notes for some of the most interesting srsRAN use-cases.


srsRAN is a free and open-source 4G and 5G software radio suite. 

Featuring both UE and eNodeB/gNodeB applications, srsRAN can be used with third-party core network solutions to build complete end-to-end mobile wireless networks. For more information, see `www.srsran.com <https://www.srsran.com>`_. 

The srsRAN suite currently includes:

- **srsUE:** a full-stack 4G and 5G NSA / SA UE application
- **srsENB:** a full-stack 4G eNodeB with 5G NSA / SA gNodeB capabilities 
- **srsGNB:** a full-stack 5G SA gNodeB application **(coming 2022)**
- **srsEPC:** a light-weight 4G EPC implementation with MME, HSS and S/P-GW

All srsRAN software runs in linux with off-the-shelf compute and radio hardware.

.. toctree::
   :maxdepth: 2
   
   getting_started.rst
   feature_list.rst
   general/source/index.rst
   usermanuals/source/index.rst 
   app_notes/source/index.rst