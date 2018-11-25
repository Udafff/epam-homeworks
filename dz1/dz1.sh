#!/bin/bash

if [ "$EUID" -ne 0 ]; then echo "Please run as root"; exit; fi

# Create projects directories
mkdir -m a=-,u=rwx Proj{1,2,3}

# Create users
for((i=1; i<=3; i++)); do useradd --password $(openssl passwd -1 P@ssw0rd) --shell /bin/bash --comment "Info manager $i" I$i; done
for((i=1; i<=5; i++)); do useradd --password $(openssl passwd -1 P@ssw0rd) --shell /bin/bash --comment "Developer $i" R$i; done
for((i=1; i<=4; i++)); do useradd --password $(openssl passwd -1 P@ssw0rd) --shell /bin/bash --comment "Analyst $i" A$i; done

# Set projects permissions
setfacl -Rm u:R2:rwX,u:R3:rwX,u:R5:rwX,u:A1:rwX,u:A4:rX Proj1
setfacl -Rdm u:R2:rwX,u:R3:rwX,u:R5:rwX,u:A1:rwX,u:A4:rX Proj1

setfacl -Rm u:R1:rwX,u:R5:rwX,u:A1:rwX,u:A2:rX,u:A3:rX Proj2
setfacl -Rdm u:R1:rwX,u:R5:rwX,u:A1:rwX,u:A2:rX,u:A3:rX Proj2

setfacl -Rm u:R1:rwX,u:R2:rwX,u:R4:rwX,u:A2:rwX,u:A1:rX,u:A4:rX Proj3
setfacl -Rdm u:R1:rwX,u:R2:rwX,u:R4:rwX,u:A2:rwX,u:A1:rX,u:A4:rX Proj3
