.. _app_notes:

.. srsRAN documentation master file, created by
   sphinx-quickstart on Dec 13 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

srsRAN Application Notes
=========================

srsRAN is a free and open-source 4G and 5G software radio suite.

Featuring both UE and eNodeB/gNodeB applications, srsRAN can be used with third-party core network solutions to build complete end-to-end mobile wireless networks. For more information, see `www.srsran.com <https://www.srsran.com>`_.

These application notes provide guides for specific srsRAN use-cases, using external applications, and guides on hardware choices and use.

.. image:: .imgs/srsran_architecture.png

| Use srsRAN without RF hardware in the loop:
|   - :ref:`ZeroMQ Application Note <zeromq_appnote>`

| Carrier Aggregation:
|   - :ref:`Carrier Aggregation Application Note <2ca_appnote>`

| Use eMBMS to support multicast/broadcast traffic using srsRAN:
|   - :ref:`eMBMS Application Note <embms_appnote>`

| Use srsRAN to explore NB-IoT deployments:
|   - :ref:`NB-IoT Application Note <nbiot_appnote>`

| Running srsRAN on the Raspberry Pi 4:
|   - :ref:`Raspberry Pi 4 Application Note <pi4_appnote>`

| Experiment with CV2X signalling with srsRAN:
|   - :ref:`CV2X Application Note <cv2x_appnote>`

| Connect a COTS UE to srsRAN:
|   - :ref:`COTS UE Application Note<cots_ue_appnote>`

| Simulate Intra-eNB & S1 Handover using ZMQ:
|   - :ref:`Handover Application Note<handover_appnote>`

| Set-up and test your first 5G NSA network:
|   - :ref:`5G NSA Application Note<5gnsa_appnote>`

| Suggested hardware packages for experimentation & development:
|   - :ref:`Suggested Hardware Packages<suggestedHW_appnote>`

| Set-up and test the embedded 5G NSA DL demonstration system:
|   - :ref:`Embedded 5G NSA DL Demonstration System Application Note<5g_nsa_emb_demo_appnote>`

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

   5g_nsa/source/index.rst

   hw_packs/source/index.rst

   5g_nsa_emb_demo/source/index.rst
