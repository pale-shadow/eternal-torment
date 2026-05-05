collect:
	docker-compose build ml-gnn-collect
	@echo "Tagging image:  $(shell docker images -q | head -1)"
	docker tag $(shell docker images -q | head -1) gcr.io/gcp-gcs-pso/ml-gnn-collect:latest
	docker push gcr.io/gcp-gcs-pso/ml-gnn-collect:latest
