# Download satellite extractor


## Credentials

1. **Credentials for GCP**: Please follow the instructions as explained [here](https://developers.google.com/earth-engine/guides/service_account#use-a-service-account-with-a-private-key) and add update your credentials as follows.
      1. Inside of `src/satellite-extractor-dockerized/config.py`, update `service_account` with your new service account.
      1. Store the GCP json key inside of  `src/satellite-extractor-dockerized/data_config`  

1. **Credentials for SentinelHub**: The best of this project is that you can download data for free using the Free Tier from SentinelHub. Follow the instructions to create your username and password [here](https://docs.sentinel-hub.com/api/latest/api/overview/authentication/). Please remember it is a free trial, access is limited! 


## Docker pipeline

If you want to download data using docker,  please update the [config file](https://github.com/sebasmos/satellite.extractor/blob/main/src/satellite-extractor-dockerized/config.py) as desired and follow the next commands.

```
docker build -f Dockerfile -t docker .
```

Run with syncronized volume:

```
docker run -v /home/sebasmos/Desktop/satellite.extractor/src/satellite-extractor-dockerized:/Dengue -ti docker /bin/bash
```
Finally, run `python satellite.extractor.py` to download the satellites as customized.
