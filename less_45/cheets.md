## Taint
```bash
kubectl taint nodes worker-node-02 run=false:NoSchedule
kubectl describe node worker-node-02 | grep -A4 Taints
```

```yaml
---
# no toleration pod
apiVersion: v1
kind: Pod
metadata:
  name: ordinary-pod
spec:
  containers:
    - name: nginx
      image: nginx:latest
      
---
# toleration pod
apiVersion: v1
kind: Pod
metadata:
  name: toleration-pod
spec:
  containers:
    - name: nginx
      image: nginx:latest
  tolerations:
    - key: "run"
      operator: "Equal"
      value: "false"
      effect: "NoSchedule"
```

## RBAC
```bash
openssl genrsa -out developer.key 2048
openssl req -new -key developer.key -out developer.csr -subj "/CN=developer/O=developers"
sudo openssl x509 -req -in developer.csr -CA /etc/kubernetes/pki/ca.crt -CAkey /etc/kubernetes/pki/ca.key -CAcreateserial -out developer.crt -days 365

kubectl --kubeconfig=...
```

```yaml
apiVersion: rbac.authorization.k8s.io/v1
```

## Calico
```yaml
apiVersion: crd.projectcalico.org/v1
```

## Ingress
```bash
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

helm install ingress-nginx ingress-nginx/ingress-nginx   --set controller.service.type=NodePort   --set controller.service.nodePorts.http=32080   --set controller.service.nodePorts.https=32443

kubectl get pods -n default -l app.kubernetes.io/name=ingress-nginx
```

nginx

```
server {
  listen 80;
  server_name <domain>;

  location / {
    return 301 https://$host$request_uri;
  }
}

server {
  listen 443 ssl;
  server_name <domain>;

  ssl_certificate <cert-path>;
  ssl_certificate_key <key-path>;

  ssl_protocols TLSv1.2 TLSv1.3;
  ssl_prefer_server_ciphers on;

  location / {
    proxy_pass http://upsstream;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
  }
}
```
