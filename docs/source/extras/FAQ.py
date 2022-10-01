'''
## General FAQ
### Why doesn't the library support Mac?
I don't have a Mac to develop the library on so I have no way to test if the code works.
If you have a Mac and you would like to contribute, please do not hesitate to [create a pull request](https://github.com/Crozzers/screen_brightness_control/pulls).

### Library throws exception - `NameError: name '_OS_MODULE' is not defined`
This error is thown when attempting to use the library on unsupported platforms.

Upon import, the library will check which OS it is running on and will attempt to import the
relevant, OS specific sub-modules. When running on an unsupported OS, this will not be possible and
so `_OS_MODULE` will not be defined.

In the past, a `NotImplementedError` would have been raised at this stage, letting you know the issue.
This behaviour was changed in v0.16.0 to simply log a warning.

## Windows FAQ
### The model of my monitor/display is not what the program says it is
If your display is a laptop screen and can be adjusted via a Windows brightness slider then there is no easy way to get the monitor model that I am aware of.
If you know how this might be done, feel free to [create a pull request](https://github.com/Crozzers/screen_brightness_control/pulls) or to ping me an email [captaincrozzers@gmail.com](mailto:captaincrozzers@gmail.com)


### When I call `get_brightness()` the returned value isn't what I set it to
Not all monitors can set the brightness for every value between 0 and 100. Some of them have a number of 'levels' that they can be set to.
You can likely see this if you open your display settings and very slowly move the brightness slider.  
You can find out your brightness 'levels' by running the following python code:
```python
import wmi
monitor = wmi.WMI(namespace='wmi').WmiMonitorBrightness()[0]
#the number of levels the monitor can be set to
print(monitor.Levels)
#the actual brightness values your monitor can be set to
print(monitor.Level)
```


## Linux FAQ
### Why do I always get `ScreenBrightnessError`?
Linux often requires a bit of tweaking to get working out of the box. This either means installing a 3rd party program or
granting extra permissions to the user.

These steps are covered in detail on the [Installing On Linux](Installing%20On%20Linux.html) page.


## None of these answered my question
Please [raise an issue](https://github.com/Crozzers/screen_brightness_control/issues/new) on the GitHub repo or email me at [captaincrozzers@gmail.com](mailto:captaincrozzers@gmail.com) with your question.
'''
