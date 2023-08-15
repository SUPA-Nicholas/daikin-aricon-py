## Description

API for Daikin thermostat with BRP15B61 WiFi adapter

## Usage

```python
# discover daikin thermostat in your network
# return basic info of all thermostats as dist
Aircon.discover()

# get power status
Aircon.get_power(host)

# get current mode
Aircon.get_mode(host)

# get target temperature
Aircon.get_target_temp(host)

# get fan speed
Aircon.get_frate(host)

# set power status
Aircon.set_power(host)

# set current mode
Aircon.set_mode(host)

# set target temperature
Aircon.set_target_temp(host)

# set fan speed
Aircon.set_frate(host)
```

## Parameters

pow:
off = 0
on = 1

mode:
fan = 0
heat = 1
cool = 2
dry = 7

temperature (no decimal):
cool: 17-32
heat: 16-31

fan rate:
0 = auto
1 = low
3 = medium
5 = high