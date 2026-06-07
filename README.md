## База

```bash
docker build -t k8s-lab5-backend:1.0 backend
docker build -t k8s-lab5-frontend:1.0 frontend
kubectl apply -k k8s/
kubectl get pods,svc -n lab5-fastapi
```

## GHCR

```bash
kubectl set image deployment/backend-deployment backend=REG-backend:latest -n lab5-fastapi
kubectl set image deployment/frontend-deployment frontend=REG-frontend:latest -n lab5-fastapi
```

## Ingress

```bash
helm upgrade --install ingress-nginx ingress-nginx --repo https://kubernetes.github.io/ingress-nginx -n ingress-nginx --create-namespace
```

## Prometheus + метрики + Loki
```bash
kubectl rollout restart deployment/backend-deployment -n lab5-fastapi
kubectl apply -k k8s/observability/
```

## HPA + нагрузка
```bash
kubectl apply -f k8s/hpa-backend.yaml
kubectl apply -f k8s/jobs/load-backend-hpa.yaml
kubectl get hpa -n lab5-fastapi -w
```

## Удалить всё

```bash
kubectl delete job lab5-load-backend -n lab5-fastapi
kubectl delete namespace lab5-fastapi
kubectl delete clusterrolebinding lab5-promtail
kubectl delete clusterrole lab5-promtail
```
