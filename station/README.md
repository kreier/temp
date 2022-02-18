# Temp project - measurement station

For simplicity we program the measurement station in Arduino C.  The software has main 3 tasks to perform

- Measure the temperature
- Connect to the WiFi
- Connect to the server/API and submit the data

Further extensions can include

- Analyse the response from the server for successful submission
- Have the station powered by a LiIon backup battery
- Check battery voltage and adjust power consumption (deep_sleep) accordingly
- Store measurements locally if submission to the database is not possible
