#!/bin/sh

BW_RB=$1
if ["$BW_RB" == ""]
then
    BW_RB=50
fi

SRSRAN_PATH=/srsRAN/
CFG_PATH=$SRSRAN_PATH/config
GNB_PATH=$SRSRAN_PATH/build/srsenb/src/srsenb
EPC_PATH=$SRSRAN_PATH/build/srsepc/src/srsepc


cd $CFG_PATH

PID=$(pgrep srsepc)
if ["$PID" != ""]
then
    sudo kill -9 $PID
fi

sudo screen -Logfile /tmp/srsepc.log -dmSL epc $EPC_PATH epc.conf

sudo $GNB_PATH enb_${BW_RB}rb.conf
