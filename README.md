# Scrapy-Modis

### Installation
```sh
$ pip install -r requirements.text
```
or
```sh
$ conda install --file requirements.txt
```
---

### Development
First, set environment variable for authentication MODIS website.
- MacOS
```sh
$ export MODIS_USERNAME='username'
$ export MODIS_PASSWORD='password
```
- Windows
```sh
$ set MODIS_USERNAME='username'
$ set MODIS_PASSWORD='password
```

Second, run scrapy
```sh
$ scrapy crawl modis
```