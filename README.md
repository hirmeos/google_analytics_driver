# Google Analytics Driver
[![Build Status](https://travis-ci.org/hirmeos/google_analytics_driver.svg?branch=master)](https://travis-ci.org/hirmeos/google_analytics_driver)


## Run via crontab
```
0 0 * * 0 docker run --rm --name "google_analytics_driver" --env-file /path/to/config.env -v /somewhere/to/store/analysis:/usr/src/app/cache -v /somewhere/to/store/output:/usr/src/app/output openbookpublishers/google_analytics_driver
```
