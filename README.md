# Scrapy-Modis

### Installation
- using ```pip```
```sh
$ pip install -r requirements.text
```
or
- using ```conda```
```sh
$ conda install --file requirements.txt
```
---

### Development
First, Register ```username``` and ```password```. This [link](https://urs.earthdata.nasa.gov/users/new)

Second, set environment variable for authentication MODIS website. 

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

Last, run scrapy
```sh
$ scrapy crawl modis
```