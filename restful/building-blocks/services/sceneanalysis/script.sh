#!/bin/bash

export SESSION=`uuidgen`
for i in `seq 1 5`; do
    export DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"`
    curl -su 7f5933d2-cd7c-11e4-9fe6-490467a5e114:db19c01e-18e5-4fc2-8b81-7b3d1f44533b \
         -F "attachment://bar=@macgyver.jpg;type=image/jpg" \
         -F 'meta={"async" : false, "image": "attachment://bar", "timestamp" : "'$DATE'", "state": { "session_id": "'$SESSION'"}};type=application/json' \
         https://gate.angus.ai/services/scene_analysis/1/jobs
done
