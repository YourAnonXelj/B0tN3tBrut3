#!/bin/sh

# Debian ZMap Install

apt-get update -y

apt-get install build-essential cmake libgmp3-dev gengetopt libpcap-dev flex byacc libjson-c-dev pkg-config libunistring-dev -y

apt-get install zmap -y
