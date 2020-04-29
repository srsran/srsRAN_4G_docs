.. srsLTE Two Carrier Aggregation Application Note

.. _2ca_appnote:

ZeroMQ Application note
===========================


Introduction
************

Before getting hand on we recommend reading about Carrier Aggregation in [sharetechnote.com](https://www.sharetechnote.com/html/Lte_Advanced_CarrierAggregation.html).

This Application note requires an RF device that can tune different frequencies in different channels. We recommend X300 series from Ettus Research (NI).

Also, this application note can be done with ZMQ. For this see our Application note regarding no-RF.


eNb Configuration
*******************

The eNb configuration has two parts, one is the RF front end configuration and the second the creation of multiple cells and the linkage between them as secondary cells.

For using real RF devices, auto value is okay. However, the device args for ZMQ would look like this:

.. code::

  device_name = zmq
  device_args = fail_on_disconnect=true,id=enb,tx_port=tcp://*:2000,rx_port=tcp://localhost:2001,tx_port1=tcp://*:2002,rx_port1=tcp://localhost:2003

The second step is instanciating two cells in the eNb. For this, one needs to modify the rr.conf:

..code::

  cell_list =
  (
    {
      rf_port = 0;
      cell_id = 0x01;
      tac = 0x0001;
      pci = 1;
      root_seq_idx = 204;
      dl_earfcn = 2850;

      // CA cells
      scell_list = (
        {cell_id = 0x02; cross_carrier_scheduling = false; scheduling_cell_id = 0x01; ul_allowed = true}
      )
    },
    {
      rf_port = 1;
      cell_id = 0x02;
      tac = 0x0001;
      pci = 4;
      root_seq_idx = 205;
      dl_earfcn = 2910;

      // CA cells
      scell_list = (
        {cell_id = 0x01; cross_carrier_scheduling = false; scheduling_cell_id = 0x02; ul_allowed = true}
      )
    }
  )

That is all the modifications required for the eNb.


UE Configuration
*******************

Let's first start with the RF configuration. One needs to set the list 
of EARFCN according to the one cells instanciated in the eNb and the 
number of carriers to 2:

.. code::

  [rf]
  dl_earfcn = 2850,2910
  nof_carriers = 2

Adding more EARFCN in the list makes the UE scanning these frequencies 
and the number of carriers makes the UE using more RF channels.

In case one wants to use ZMQ we recommend using the following RF device
 arguments:

.. code::

  device_name = zmq
  device_args = tx_port=tcp://*:2001,rx_port=tcp://localhost:2000,tx_port1=tcp://*:2003,rx_port1=tcp://localhost:2002,id=ue,tx_freq=2510e6,rx_freq=2630e6,tx_freq1=2516e6,rx_freq1=2636e6


Since the ZMQ module is frequency agnostic, it is important that Tx and 
Rx frequencies are set in ZMQ. This will make possible internal carrier 
switching.

Finally, the UE needs to report in the UE capabilities at least release 
10 and category 7:

.. code::

[rrc]
ue_category        = 7
ue_category_dl     = 10


Known issues
************

* The eNb ignores UE's band capabilities
* CPU hungry and real time errors for more than 10 MHz
