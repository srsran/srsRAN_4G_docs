.. srsRAN Carrier Aggregation Application Note

.. _2ca_appnote:

Carrier Aggregation
===================


Introduction
************

Before getting hands-on we recommend reading about `Carrier Aggregation <https://www.sharetechnote.com/html/Lte_Advanced_CarrierAggregation.html>`_.

The srsRAN software suite supports 2-carrier aggregation in both srsENB and srsUE. To experiment with carrier aggregation using srsRAN over-the-air, you will need an RF device that can tune different frequencies in different channels, for example the USRP X300 series from Ettus Research (NI). We've tested with UHD 3.15 LTS and UHD 4.0.

Alternatively, experiment with carrier aggregation without SDR hardware using our ZeroMQ-based RF layer emulation. See our :ref:`ZeroMQ Application Note <zeromq_appnote>` for more information about RF layer emulation.

Carrier Aggregation using SDR Hardware
**************************************

eNodeB Configuration
--------------------

To configure the eNodeB for carrier aggregation, we must first configure the RF front-end. We must then configure srsENB for multiple cells and define the primary/secondary relationships between them.

If you're using a real RF device such as the USRP X300 it's advisable to use an external clock reference, either using the 10 MHz/1 PPS input (``clock=external``) or the GPSDO (``clock=gpsdo``).
For the X300, especially for newer UHD versions, it's also required to specific the sample rate upon radio initialization. For example, if you're planning to use 10 MHz cells (50 PRB)
the sample rate of the radio will be 11.52 Msamples/s, hence a ``sampling_rate=11.52e6`` shall be used. For 20 MHz cells (100 PRB) the sample rate will be 23.04 Msamples/s, hence ``sampling_rate=23.04e6`` shall be used.

.. code::

  [rf]
  device_name = uhd
  device_args = type=x300,clock=external,sampling_rate=23.04e6


The second step is to configure srsENB with two cells. For this, one needs to modify ``rr.conf``:

.. code::

  
  cell_list =
  (
    {
      rf_port = 0;
      cell_id = 0x01;
      tac = 0x0007;
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
      tac = 0x0007;
      pci = 4;
      root_seq_idx = 268;
      dl_earfcn = 3050;

      // CA cells
      scell_list = (
        {cell_id = 0x01; cross_carrier_scheduling = false; scheduling_cell_id = 0x02; ul_allowed = true}
      )
    }
  )

With these changes, simply run srsENB as usual.


UE Configuration
----------------

In the UE, we must again set the RF configuration and configure the UE capabilities.

For the RF configuration, we need to set the list 
of EARFCNs according to the cells configured in the eNodeB and set the 
number of carriers to 2:

.. code::

  [rf]
  dl_earfcn = 2850,3050
  nof_carriers = 2

Adding more EARFCNs in the list makes the UE scan these frequencies 
and the number of carriers makes the UE use more RF channels.


For the UE capabilities, we need to report at least release 
10 and category 7:

.. code::

  [rrc]
  ue_category        = 7
  ue_category_dl     = 10
  release            = 10

With these changes, simply run srsUE as usual.


Carrier Aggregation using ZeroMQ RF emulation
*********************************************

To experiment with carrier aggregation using the ZeroMQ RF emulation instead of SDR hardware,
we simply need to configure srsENB and srsUE to use the ``zmq`` RF device.

eNodeB Configuration
--------------------

For srsENB, configure the ``zmq`` RF device as follows:

.. code::

  [rf]
  device_name = zmq
  device_args = fail_on_disconnect=true,id=enb,tx_port0=tcp://*:2000,tx_port1=tcp://*:2002,rx_port0=tcp://localhost:2001,rx_port1=tcp://localhost:2003


UE Configuration
----------------

For srsUE, configure the ``zmq`` RF device as follows:

.. code::

  [rf]
  device_name = zmq
  device_args = tx_port0=tcp://*:2001,tx_port1=tcp://*:2003,rx_port0=tcp://localhost:2000,rx_port1=tcp://localhost:2002,id=ue,tx_freq0=2510e6,tx_freq1=2530e6,rx_freq0=2630e6,rx_freq1=2650e6


Since the ZMQ module is frequency agnostic, it is important that Tx and 
Rx frequencies are set in ZMQ config. This makes internal carrier 
switching possible.

Known issues
************

* The eNodeB ignores UE's band capabilities
* CPU hungry and real time errors for more than 10 MHz
