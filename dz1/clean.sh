#!/bin/bash

if [ "$EUID" -ne 0 ]; then echo "Please run as root"; exit; fi

sudo rm -Rf Proj*
for((i=1; i<=3; i++)); do userdel I$i; done
for((i=1; i<=5; i++)); do userdel R$i; done
for((i=1; i<=4; i++)); do userdel A$i; done
