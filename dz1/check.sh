#!/bin/bash
exec 2>/dev/null

if [ "$EUID" -ne 0 ]; then echo "Please run as root"; exit; fi


function CheckPerm {
   echo "#### Check $1 user permission"
   su -c "echo -n '$1 check Proj1 [ls]: '; ls -R Proj1/ 1>/dev/null && echo 'OK' || echo 'Failure'" $1
   su -c "echo -n '$1 check Proj1 [mkdir]: '; mkdir Proj1/$1dir && echo 'OK' || echo 'Failure'" $1
   su -c "echo -n '$1 check Proj1 [touch]: '; touch Proj1/$1file && echo 'OK' || echo 'Failure'" $1
   su -c "echo -n '$1 check Proj1 [touch]: '; touch Proj1/$1dir/$1file && echo 'OK' || echo 'Failure'" $1

   su -c "echo -n '$1 check Proj2 [ls]: '; ls -R ./Proj2/ 1>/dev/null && echo 'OK' || echo 'Failure'" $1
   su -c "echo -n '$1 check Proj2 [mkdir]: '; mkdir Proj2/$1dir && echo 'OK' || echo 'Failure'" $1
   su -c "echo -n '$1 check Proj2 [touch]: '; touch Proj2/$1file && echo 'OK' || echo 'Failure'" $1
   su -c "echo -n '$1 check Proj2 [touch]: '; touch Proj2/$1dir/$1file && echo 'OK' || echo 'Failure'" $1


   su -c "echo -n '$1 check Proj3 [ls]: '; ls -R ./Proj3/ 1>/dev/null && echo 'OK' || echo 'Failure'" $1
   su -c "echo -n '$1 check Proj3 [mkdir]: '; mkdir Proj3/$1dir && echo 'OK' || echo 'Failure'" $1
   su -c "echo -n '$1 check Proj3 [touch]: '; touch Proj3/$1file && echo 'OK' || echo 'Failure'" $1
   su -c "echo -n '$1 check Proj3 [touch]: '; touch Proj3/$1dir/$1file && echo 'OK' || echo 'Failure'" $1
   echo
   }


CheckPerm "R1"
CheckPerm "R2"
CheckPerm "R3"
CheckPerm "R4"
CheckPerm "R5"

CheckPerm "A1"
CheckPerm "A2"
CheckPerm "A3"
CheckPerm "A4"
