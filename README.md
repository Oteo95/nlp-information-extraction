# Table of Contentents

- [Information Extraction Using NLP Techniques](#information-extraction-using-nlp-techniques)
  * [Run the project in local](#run-the-project-in-local)
    + [For setting up the input data](#for-setting-up-the-input-data)
  * [Changing the tag list in the tool](#changing-the-tag-list-in-the-tool)
  * [Next steps](#next-steps)
 
<!-- toc -->
# Information Extraction Using NLP Techniques

This repository presents a tool for the development of applications focused on extracting information from text documents. The back end is fully developed using python as well as the models for the information extraction task. The front end uses VUE and a bit of java, where the main tagging component is based on the work published in the github of Doccano (https://github.com/doccano/doccano).

The following image present a short overview about the flow of the tool since the user annotates the document to how the information of the tags is stored in the data base.

![](./assets/Peek%202021-12-03%2017-30.gif)

## Run the project in local

1. Download the repository and Build the images:
```bash
docker-compose -f dockerfiles/prod/docker-compose.yml build
```
2. Run the aplication:
```bash
docker-compose -f dockerfiles/prod/docker-compose.yml up
```

If you wante insert directly the dataset into the data base:
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

## Changing the tag list in the tool

Currently the tags that are shown in the front are defined in a ```src/webui/src/config/config.js``` Using the same structure, you can set any tag, for example 'conference' with the associated 'id', 'suffixKey', 'backgroundColor', an,ño..,kd 'textColor':

<p align="center">
  {
      text: 'Conference',<br>
      backText: 'conference',<br>
      id: 1000,<br>
      suffixKey: 'c',<br>
      backgroundColor: '#B7C859',<br>
      textColor: '#000000',
    },
</p>

## Next steps

- Add functionality to the next and previous doc buttons.

- Avoid having predefined code elements such as tags in config.js. Use instead the database to have all the information for the configuration of the tool.

- Automate tagging using models to assist the user. These annotations are stored in the annotation space instead of the user's annotation space.

- Add components to the tool to aproach other tasks.

- Develop the possibility to have multiple taks and datasets running at the same time.
