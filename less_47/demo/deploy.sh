#!/bin/bash

KUBE_NS="job-demo"

kubectl -n ${KUBE_NS} delete -f job.yaml &> /dev/null
kubectl -n ${KUBE_NS} apply -f job.yaml

kubectl wait --for=condition=complete --timeout=300s job/migrator -n $KUBE_NS
kubectl apply -f app.yaml
