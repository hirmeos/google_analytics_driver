# Google Analytics Driver
[![Build Status](https://travis-ci.org/hirmeos/google_analytics_driver.svg?branch=master)](https://travis-ci.org/hirmeos/google_analytics_driver)

## API Service Account Key
Obtain the private key of a service account linked to your google analytics views: https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py

## Run via crontab
```
0 0 * * 0 docker run --rm --name "google_analytics_driver" --env-file /path/to/config.env -v /somewhere/to/store/analysis:/usr/src/app/cache -v /path/to/config:/usr/src/app/config -v /somewhere/to/store/output:/usr/src/app/output openbookpublishers/google_analytics_driver
```
