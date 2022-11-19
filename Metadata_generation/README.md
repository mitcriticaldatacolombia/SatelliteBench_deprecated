# MetaDengue

MetaDengue is a unified dataset format that combines satellite imagery and Socioeconomical and environmental metadata.

DengueSet seeks to organize satellite imagery and metadata using a unified and standard dataset, that can be scalable and reproduceable to any geographical area. For this particular project, we have extracted the satellite imagery of the municialities of Colombia from 2016 to 2018 based on the Epiweek using satellite extractor, a proposal based on SentinelHub, and with this proposal we combine Socioeconomical and environmental metadata in JSON files, one for each corresponding image so that the data is temporally and spacially aligned. 


## Proposed Structure 

The following is the desired structured that we propose for DengueSet. There are 2 main folders, one called `images` which contains a subfolder for each corresponding municipality and inside of it, all the temporal satellite imagery for each corresponding municipality. On the second folder, the same structure as the previous one, but on each case, containing the corresponding metadata on JSON files.

```
DATASET/ 
	images/
		5001/
                  images_01_01_2016.tiff
                  images_01_07_2016.tiff
                  .
                  .
		5002/
    .
    .
		500N/
	annotations/
		5001/
                  images_01_01_2016.json
                  images_01_07_2016.json
		      .
                  .
		5002
    .
    .
		500N
```


## Create metadata dataset.

In order to create a customized dataset, please update `config.py` with the corresponding metadata and adapt `build_dataset.py` as required. For DengueSet case, please run `build_dataset.py`. Afterwards, make sure the `images` folder is stored on the same tree hierarchy as the `annotations/` folder.


## Metadata organization: 

```
{
      "image_path": "DATASET/images/41001/image_2016-01-03.tiff",
      "municipality_code": 41001,
      "epiweeks": 201601,
      "dynamic": {
            "cases": {
                  "dengue_cases": 63,
                  "binary_classification": 1,
                  "multiclass": 0
            },
            "environmental_data": {
                  "temperature": [
                        27.47078427209743
                  ],
                  "precipitation": [
                        5.705897276864907
                  ]
            },
            "socioeconomic_data": {
                  "Population": 351933
            }
      },
      "static": {
            "environmental_data": {
                  "elevation": 460.0
            },
            "socioeconomic_data": {
                  "Age0-4(%)": 7.33,
                  "Age5-14(%)": 25.62,
                  "Age>30(%)": 51.86,
                  "AfrocolombianPopulation(%)": 0.63,
                  "IndianPopulation(%)": 0.32,
                  "PeoplewithDisabilities(%)": 7.9,
                  "Peoplewhocannotreadorwrite(%)": 4.0,
                  "Secondary/HigherEducation(%)": 62.42,
                  "Employedpopulation(%)": 38.83,
                  "Unemployedpopulation(%)": 5.54,
                  "Peopledoinghousework(%)": 14.72,
                  "Men(%)": 47.86,
                  "Women(%)": 52.14,
                  "Householdswithoutwateraccess(%)": 2.44,
                  "Householdswithoutinternetaccess(%)": 33.99,
                  "Buildingstratification1(%)": 23.1001,
                  "Buildingstratification2(%)": 38.5433,
                  "Buildingstratification3(%)": 8.2185,
                  "Buildingstratification4(%)": 4.0139,
                  "Buildingstratification5(%)": 0.8625,
                  "Buildingstratification6(%)": 0.0719,
                  "NumberofhospitalsperKm2": 0.10367,
                  "NumberofhousesperKm2": 63.426272
            }
      }
}
```
