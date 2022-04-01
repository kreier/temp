# Temp
[![GitHub release](https://img.shields.io/github/release/kreier/temp.svg)](https://GitHub.com/kreier/temp/releases/)
[![MIT license](https://img.shields.io/github/license/kreier/temp)](https://kreier.mit-license.org/)

Test framework for remote data collection and visualization. Here is [a document on how it works](documentation.md).

## Components of this project

- Data collection unit ESP32, connected to the internet
  - Solar powered
  - Remote software update possible
- Website [kreier.org/temp/](https://kreier.org/temp/) to display the measurements
  - The most recent data is available
  - Some graphical visualization represent last day, week, month, year
  - Data read from a database MySQL via PHP on the website
- Backend of website
  - Data can be submitted via json
  - Data files are created into the [/data](https://kreier.org/temp/data/) subfolder

## History

### 2021/12/01 Start physical site

Some scaffold data was uploaded to [kreier.org/temp/](https://kreier.org/temp/). Now you get a http response.

Further inspiration is taken from Rui Santos and an example from Germany:
- [https://randomnerdtutorials.com/esp32-esp8266-mysql-database-php/](https://randomnerdtutorials.com/esp32-esp8266-mysql-database-php/)
- [http://wetter.cuprum.de/](http://wetter.cuprum.de/)

### 2021/11/19 New start with ESP32

The project was sticking in my head for some time. I would need this framework as foundation for larger data collection projects like solar- and wind data. The new project [github.com/kreier/temp](https://github.com/kreier/temp/) was born.

### 2020/12/16 New hardware with ESP8266 and LM35

A less expensive approach was started in December 2020. The hardware was succesfully build, but the database was never implemented.

![https://github.com/kreier/temp.hofkoh.de/blob/main/documentation/2020_esp8266.jpg](https://github.com/kreier/temp.hofkoh.de/blob/main/documentation/2020_esp8266.jpg)

### 2013/11/23 Start of temp.hofkoh.de

A similar project was started in November 2013. It submitted data until summer 2016. A documentation of the code and data can be found here on Github under [github.com/kreier/temp.hofkoh.de](https://github.com/kreier/temp.hofkoh.de)
