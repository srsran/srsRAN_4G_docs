#!/bin/sh
devmem 0xa004039c w 1 && devmem 0xa0040010 w 1024
mount -t tmpfs -o size=200m tmpfs /home/root/tmpfs
./srsue ue.conf

