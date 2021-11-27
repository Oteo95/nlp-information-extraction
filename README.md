# Information Extraction Using NLP Techniques

## Production

1. Build the production images:
```bash
docker-compose -f dockerfiles/prod/docker-compose.yml build
```
2. Run the aplication:
```bash
docker-compose -f dockerfiles/prod/docker-compose.yml up
```

With the new version do:
```bash
DATASET={filename.csv} docker-compose -f dockerfiles/prod/docker-compose.yml up
```
Or
```bash
export DATASET={filename.csv}
docker-compose -f dockerfiles/prod/docker-compose.yml up
```

|Container| PORT |
|--|--|
|webapi| http://localhost:8001/webapi |
|webui| http://localhost:8082 |
|mongo| 0.0.0.0:27018 |
|mongo express|http://localhost:8083/ |


### For setting up the input data
If you start from an empty mongo DB, you need to populate it:
1. In the python Devcontainer
2. Load cases into local MongoDB
```bash
python src/extraction/scripts/documents_to_mongo.py
```
3. TODO: Auto annotation documents with transformer model:
