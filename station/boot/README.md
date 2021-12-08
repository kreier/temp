# boot 

Submits successfull boot and wifi to http://temp.kreier.org/boot/boot.php

Results at https://kreier.org/temp/boot/

Version v0.1.20121208

## data in database

- ID  48 bit (6byte) in uint_64t which is the chipID or Macadress
- time_t 64bit when did this boot happened
- version string of the software version (for remote update)
- ntp if it knows the actual time
- lipo voltage of the lithium battery (or zero)
- time_to_submit in ms to see for wifi issues
- temp recent measured temperature (or zero)
