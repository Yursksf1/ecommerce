docker run -d --name db3 \
  -e POSTGRES_PASSWORD=password \
  -p 5430:5432 \
  -v $(pwd)/:/home/ \
  -v $(pwd)/../postgres-data:/var/lib/postgresql/data \
  postgres:12
