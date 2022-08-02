#!/bin/bash

/sbin/insmod srs_dma_driver.ko
/sbin/insmod ue_nr_datamover_driver.ko

drivers_not_found=false

if ! dmesg | tail | grep -iq "srs_rx_dma: Successfully probed"; then
  echo "failed to probe RX DMA driver for baseband samples transfers (srs_dma_driver)"
  drivers_not_found=true
fi;

if ! dmesg | tail | grep -iq "srs_tx_dma: Successfully probed"; then
  echo "failed to probe TX DMA driver for baseband samples transfers (srs_dma_driver)";
  drivers_not_found=true
fi;

if ! dmesg | tail | grep -iq "ue_nr_datamover_0: Successfully probed!"; then
  echo "failed to probe DMA driver for decoded PDSCH bits reception (ue_nr_datamover_driver)";
  drivers_not_found=true
fi;

if ! $drivers_not_found; then
  echo "All drivers have been loaded succesfully"
fi;
