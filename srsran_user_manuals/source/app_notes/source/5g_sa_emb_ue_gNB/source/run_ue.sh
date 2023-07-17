#!/bin/bash

valid_BW=(52 106)

BW=$1
if [[ "$BW" == "" ]]; then
  BW=52
fi;

if [[ ! " ${valid_BW[*]} " =~ " ${BW} " ]]; then
  echo "The script was called with invalid parameter, valid values are [52, 106]"
  exit 1
fi;

if [[ "$BW" == "${valid_BW[0]}" ]]; then
  echo "Using 52PRB config"
  devmem 0xa004039c w 1 && devmem 0xa0040010 w 1024
else
  echo "Using 106PRB config"
  devmem 0xa004039c w 1 && devmem 0xa0040010 w 2048
fi;

mount -t tmpfs -o size=200m tmpfs /home/root/tmpfs

./srsue ue_${BW}prb.conf
