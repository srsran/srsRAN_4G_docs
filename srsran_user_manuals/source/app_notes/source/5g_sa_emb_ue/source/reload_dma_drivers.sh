#!/bin/bash

script_path=$(pwd)

/sbin/rmmod ue_nr_datamover_driver
/sbin/rmmod srs_dma_driver
cd /sys/bus/platform/drivers/xilinx-vdma/
echo a0090000.dma > unbind

# generate reset in FPGA
devmem 0xa004039c w 1

echo "Removed DMA drivers from the kernel, going to reload..."

echo a0090000.dma > bind
cd $script_path
./install_srsue_drivers.sh

