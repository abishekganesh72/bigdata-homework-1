#!/bin/sh
sudo hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.2.1.jar \
 -input /user/training/shakespeare/* \
 -output /user/training/outputs/output2 \
 -file /mnt/hgfs/Shared/BD_HW_1/BD_HW_1_1_mapper.py \
 -mapper /mnt/hgfs/Shared/BD_HW_1/BD_HW_1_1_mapper.py \
 -file /mnt/hgfs/Shared/BD_HW_1/BD_HW_1_1_reducer.py \
 -reducer /mnt/hgfs/Shared/BD_HW_1/BD_HW_1_1_reducer.py

