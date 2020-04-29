.. _enb_advanced:

Advanced Usage
==============

MIMO
****

The srsENB supports MIMO transmission modes 2, 3, and 4. You only need to set up the transmission mode and the number of eNb ports in the ``enb.conf`` file:

.. code::

  ...
  [enb]
  ...
  tm = 3
  nof_ports = 2
  ...
  
The eNb configures the UE for reporting the Rank Indicator for transmission modes 3 and 4. You can set the rank indicator periodic report in the file ``rr.conf`` field ``m_ri``. This value is multiples of CQI report period. For example, if the CQI period is 40ms and ``m_ri`` is 8, the rank indicator will be reported every 320ms.


Carrier Aggregation
*******************

.. warning::


  TBA


