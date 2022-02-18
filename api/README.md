# API

The temp target domain provides the following functions:

## register.php

Add the unique ID (MAC address) to the database of eligable stations to submit temperature values. A hash is generated during this registration process that should be included in the code to submit temperature values.

## index.php

Returns the temperature values of last day / week / month / year as a graph. One sensor is preselected, but with a pulldown menu others can be selected.

## data.php?json="data" - writing to database

Interface to upload measurements to the database. The parameters of the json descriptor are:

- **id** - sensor id, usually the last 6 bytes of the MAC address, as hex "0xACFF00"
- **hash** - identifier for id to ensure correct submission. Has was created during registration
- **time** - time_64t time when the measurement was taken
- **temperature** - float64 temperature value in degree Celcius

## temp.php?json="data" - read from the database

This is used for embedded websites or an developed app.

## stations.php

Lists the registered stations
