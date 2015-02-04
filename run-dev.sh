#!/bin/bash

echo `date +"%Y%m%d%H%M"` > swarmdocs/layouts/partials/cache_datestamp.html
cd swarmdocs && hugo server -ws .
