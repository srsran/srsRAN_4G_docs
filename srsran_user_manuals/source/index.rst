
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
- **srsEPC:** a light-weight 4G EPC implementation with MME, HSS and S/P-GW

All srsRAN software runs in linux with off-the-shelf compute and radio hardware.

-----


.. toctree::
   :maxdepth: 2
   :caption: General
   
   getting_started.rst
   feature_list.rst

.. toctree::
   :maxdepth: 2
   :caption: First Steps

   general/source/1_installation.rst
   general/source/2_release_notes.rst
   general/source/3_contributions.rst
   general/source/4_troubleshooting.rst

.. toctree::
   :maxdepth: 2
   :caption: User Manuals

   usermanuals/source/srsue/source/index.rst
   usermanuals/source/srsenb/source/index.rst
   usermanuals/source/srsepc/source/index.rst

.. toctree::
   :maxdepth: 2
   :caption: Application Notes

   app_notes/source/5g_sa_E2E/source/index.rst
   app_notes/source/5g_sa_COTS/source/index.rst
   app_notes/source/5g_sa_amari/source/index.rst
   app_notes/source/5g_nsa_zmq/source/index.rst
   app_notes/source/5g_nsa_cots/source/index.rst
   app_notes/source/5g_nsa_amari/source/index.rst
   app_notes/source/zeromq/source/index.rst
   app_notes/source/cots_ue/source/index.rst
   app_notes/source/handover/source/index.rst
   app_notes/source/2ca/source/index.rst
   app_notes/source/cv2x/source/index.rst
   app_notes/source/embms/source/index.rst
   app_notes/source/nbiot/source/index.
   app_notes/source/pi4/source/index.rst
   app_notes/source/hw_packs/source/index.rst





