#!/bin/bash
# Start the php service and make it accessible to nginx1
service php5-fpm start && chmod a+rw /var/run/php5-fpm.sock
