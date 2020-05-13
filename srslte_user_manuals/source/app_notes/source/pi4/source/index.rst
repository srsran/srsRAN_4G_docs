.. srsLTE Pi4 Application Note

.. _pi4_appnote:

Raspberry Pi 4 Application note
===============================


Introduction
************
srsLTE is a full end-to-end LTE solution including a core network and an eNodeB. Most people in the srsLTE community run the software on high performance computers, however the eNodeB and core network can also be run on the low power Raspberry Pi 4.

The concept of an ultra low cost, low power and open source SDR LTE femtocell has a lot of people excited!


Standalone Pi4 LTE Network Hardware Requirements
************************************************
The setup instructions provided below have been tested with a **Raspberry Pi 4B /4GB rev 1.2** running the Ubuntu Server 20.04 LTS x64 arm64 image. It has not been tested with the rev 1.1 board, boards with 2GB of RAM or alternative operating systems. The Ubuntu image can be downloaded from the official `Ubuntu website <https://ubuntu.com/download/raspberry-pi>`_. You can visually identify your Pi4 hardware revision -- `this doc from Cytron <https://tutorial.cytron.io/2020/02/22/how-to-check-if-your-raspberry-pi-4-model-b-is-rev1-2/>`_ shows you how. 

.. note::
  This setup has been tested with a USRP B210, a LimeSDR-USB and a LimeSDR-Mini. While the software executes with each of these SDR configurations, at the time of writing this doc, UEs can **only join the cell produced by the USRP B210**. A cell is created when using a LimeSDR and UEs camp on it, however the UE never establishes a data connection. This needs further investigation.

Due to the power requirements of the SDRs, you must use an external power source. This can be achieved with a 'Y' cable, such as this:

.. image:: .imgs/usb.png

Software Setup
**************

First thing is to install the SDR drivers and build srsLTE. UHD drivers are required for USRPs, SoapySDR/LimeSuite are required for the LimeSDRs. 

**UHD Drivers** can be installed with:

.. code::

  sudo apt install libuhd-dev libuhd3.15.0 uhd-host
  sudo /usr/lib/uhd/utils/uhd_images_downloader.py

  ## Then test the connection by typing:
  sudo uhd_usrp_probe


**SoapySDR** and **LimeSuite** can be installed with:

.. code::

  git clone https://github.com/pothosware/SoapySDR.git
  cd SoapySDR
  git checkout tags/soapy-sdr-0.7.2
  mkdir build && cd build
  cmake ..
  make -j4
  sudo make install
  sudo ldconfig

.. code::

  sudo apt install libusb-1.0-0-dev
  git clone https://github.com/myriadrf/LimeSuite.git
  cd LimeSuite
  git checkout tags/v20.01.0
  mkdir build && cd build
  cmake ../
  make -j4
  sudo make install
  sudo ldconfig
  cd ..
  cd udev-rules
  sudo ./install.sh

  ## Then test the connection by typing:
  LimeUtil --find
  LimeUtil --update
  SoapySDRUtil --find


Next, **srsLTE** can be compiled:

.. code::

  git clone https://github.com/srsLTE/srsLTE.git
  cd srsLTE
  git checkout tags/release_19_12
  mkdir build && cd build
  cmake ../
  make -j4
  sudo make install
  sudo ldconfig

  ## copy configs to root
  sudo srslte_install_configs.sh user


And finally, modify the **Pi CPU scaling_governor** to ensure it is running in performance mode:

.. code::

  sudo systemctl disable ondemand
  sudo apt install linux-tools-raspi

  sudo nano /etc/default/cpufrequtils
  * insert:
  * GOVERNOR="performance"

  ## reboot

  sudo cpupower frequency-info
  * should show that the CPU is running in performance mode, at maxiumum clock speed


Standalone Pi4 LTE Network Config
*********************************

During testing, the following eNB config options have been shown to be stable for 24hr+, so should be a good starting point for you.

This eNB produces a 3MHz wide 2x2 MIMO cell on the USRP in LTE B3 (1800MHz band), DL=1878.40 UL=1783.40. This sits inside the UK's new "1800MHz shared access band", for which you can legally obtain a low cost, `low power shared access spectrum licence from Ofcom <https://www.ofcom.org.uk/manage-your-licence/radiocommunication-licences/shared-access>`_ if you are working in the UK.


.. Note::
  Download working configs here:

  * :download:`enb.conf for USRP (tested B210)<enb_usrp.conf>`.
  * :download:`enb.conf for LimeSDR (tested LimeSDR-USB and LimeSDR-Mini)<enb_lime.conf>`.


.. code::
  
  sudo nano /root/.config/srslte/enb.conf
 
  [enb]
  ...
  mcc = <yourMCC>
  mnc = <yourMNC>
  n_prb = 15
  tm = 2
  nof_ports = 2

  [rf]
  dl_earfcn = 1934
  tx_gain = 80
  rx_gain = 40
  device_name = UHD
  device_args = auto

Next, edit the EPC config:

.. code::

  sudo nano /root/.config/srslte/epc.conf

  [mme]
  ...
  mcc = <yourMCC>
  mnc = <yourMNC>

And finally, edit the HSS file to add your SIM cards:

.. code::

  sudo nano /root/.config/srslte/user_db.csv


Running the Standalone Pi4 LTE Network 
**************************************

Launch the software in separate ssh windows, or using screen. 
Remember to use an external power source for your USRP.

.. code::

  sudo srsepc /root/.config/srslte/epc.conf
  sudo srsenb /root/.config/srslte/enb.conf
  sudo /usr/local/bin/srsepc_if_masq.sh eth0

.. code::

  sudo apt install screen

  ## launch and detatch
  sudo screen -S ENB -d -m  srsenb /root/.config/srslte/enb.conf
  sudo screen -S EPC -d -m  srsepc /root/.config/srslte/epc.conf
  sudo /usr/local/bin/srsepc_if_masq.sh eth0

  ## reattach 
  screen -r ENB
  screen -r EPC

The following htop screenshot shows the resource utilisation when running the software on the Pi 4B /4GB RAM with x2 UEs attached to the cell. The srsLTE software has been running for more than 18 hours without any problems. Only half of the RAM is used, and the CPU cores are sitting at around 25%. There is a chance, therefore, that this software configuration will work with the Pi 4B /2GB RAM version, and maybe also on other recent Arm based dev boards. If you can get a working cell going with alternative hardware, let the srslte-users mailing list know!

.. image:: .imgs/htop.png

Known issues
************

* When running with the soapy driver and a LimeSDR, UE will not connect. The message "UE is not ECM connected" is printed in the srsepc console
* Stability issues were noted on the Pi with the most recent release of srsLTE (v20.04), hence srsLTE version 19.12 is being used.






