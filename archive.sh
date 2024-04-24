#!/bin/sh

timestamp=`date "+%Y%m%d-%H%M%S"`
mkdir archive/$timestamp
mv simulation_output archive/$timestamp
mv nohup.out archive/$timestamp