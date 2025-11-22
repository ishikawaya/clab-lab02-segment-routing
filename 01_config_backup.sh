#!/bin/bash

for host in pe1 pe2 pe3 pe4 p1 p2 r1 r2 r5 r6; do
        docker exec -ti clab-lab02-$host bash -c "vtysh -c 'wri mem'"
done
