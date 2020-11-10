.. _app_notes:

.. srsLTE documentation master file, created by
   sphinx-quickstart on Dec 13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

srsLTE Application Notes
=========================

srsLTE is a free and open-source 4G LTE software suite. Using srsLTE, you can build an end-to-end software radio mobile network.
For more information, see `www.srslte.com <https://www.srslte.com>`_. These application notes provide guides for specific srsLTE use-cases.

.. image:: .imgs/srs_architecture.png

| Use srsLTE without RF hardware in the loop:
|   - :ref:`ZeroMQ Application Note <zeromq_appnote>`


| Carrier Aggregation:
|   - :ref:`Carrier Aggregation Application Note <2ca_appnote>`


| Use eMBMS to support multicast/broadcast traffic using srsLTE:
|   - :ref:`eMBMS Application Note <embms_appnote>`

| Use srsLTE to explore NB-IoT deployments:
|   - :ref:`NB-IoT Application Note <nbiot_appnote>`

| Running srsLTE on the Raspberry Pi 4:
|   - :ref:`Raspberry Pi 4 Application Note <pi4_appnote>`


| Experiment with CV2X signalling with srsLTE:
|   - :ref:`CV2X Application Note <cv2x_appnote>`

| Connect a COTS UE to srsLTE:
|   - :ref:`COTS UE Application Note<cots_ue_appnote>`

| Simulate Intra-eNB & S1 Handover using ZMQ:
|   - :ref:`Handover Application Note<handover_appnote>`

.. toctree::
   :maxdepth: 1

   zeromq/source/index.rst

   2ca/source/index.rst

   embms/source/index.rst

   nbiot/source/index.rst

   pi4/source/index.rst

   cv2x/source/index.rst
   
   cots_ue/source/index.rst
   
   handover/source/index.rst

