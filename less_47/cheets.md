## Helm
```bash
helm install jenkins jenkins/jenkins --set controller.admin.username=admin --set controller.admin.password=secret --namespace jenkins --create-namespace

kubectl -n $KUBE_NS port-forward service/$SVC_NAME 5000:5000
```

## Jobs
```bash
kubectl wait --for=condition=complete --timeout=300s job/db-migrate-job -n $KUBE_NS
```

