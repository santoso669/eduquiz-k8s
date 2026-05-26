# EduQuiz - Platform Quiz Online (SDG 4: Pendidikan)

Aplikasi quiz online berbasis Flask yang di-deploy di Kubernetes.

## Fitur
1. Kelola Soal (Guru)
2. Kerjakan Quiz (Siswa)
3. Riwayat Hasil

## Deploy ke Kubernetes (Minikube)

```bash
# 1. Start minikube
minikube start

# 2. Build image di dalam minikube
eval $(minikube docker-env)
docker build -t eduquiz-app:latest .

# 3. Apply manifest
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml

# 4. Akses aplikasi
minikube service eduquiz-service --url
```

## Struktur
- `app/` - Source code Flask
- `k8s/` - Kubernetes manifests (Deployment, Service, HPA)
- `Dockerfile` - Container image definition
