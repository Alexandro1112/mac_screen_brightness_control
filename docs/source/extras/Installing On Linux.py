'''
# Without using a 3rd party program

As of version [0.13.0](https://github.com/Crozzers/screen_brightness_control/releases/tag/v0.13.0), you do not need a 3rd party program to adjust your display brightness.  
However, your user will need a few extra permissions.

## Laptop displays

Laptop displays are adjusted by reading and writing to the files in the `/sys/class/backlight` directory.
To avoid having to run this library as root every time, you can do the following:

1. Add a udev rule to allow editing of the brightness files.  
   This command adds a line to your backlight udev rules allowing you to write brightness values to the relevant files.

   ```bash
   echo 'SUBSYSTEM=="backlight",RUN+="/bin/chmod 666 /sys/class/backlight/%k/brightness /sys/class/backlight/%k/bl_power"' | sudo tee -a /etc/udev/rules.d/backlight-permissions.rules
   ```

2. Reload udev rules

   ```bash
   sudo udevadm control --reload-rules && udevadm trigger
   ```

3. If the above steps don't immediately work, reboot.

Credit to [Nayr438's comment](https://linustechtips.com/topic/1246132-allow-non-root-user-to-access-sysclassbacklight/?do=findComment&comment=14015728)
on the LTT forums for this.

## Desktop displays

Desktop displays are dealt with by reading and writing to the I2C buses, located at `/dev/i2c*` on a Linux system.
These are usually part of an `i2c` user group, which you can check by running the command `ls -lh /dev/i2c*`.  

If you add yourself to the `i2c` group your user should be able to read from and write
to the I2C buses without needing to use `sudo`. To add youself to the `i2c` group, run the following command:
```
usermod -a -G i2c [your username here]
```

# Using 3rd Party Programs

## Supported Programs

There are a number of external programs that `screen_brightness_control` can call upon if the native methods fail.
The advantage of using external programs is that, because they are installed using `sudo apt install ...`, they usually allow
users to adjust the backlight without having to manually fiddle with permissions. However, they do need to be installed.

Here is an outline of all of the external programs that `screen_brightness_control` can call upon:

Program       | Works on laptop displays | Works on external monitors | Per-display brightness control        | Requires Special Permissions After Install
--------------|--------------------------|----------------------------|---------------------------------------|-------------------------------------------------------------
ddcutil       | No                       | Yes (slowest) [1]          | Yes                                   | Read/write access for `/dev/i2c*` [2]
xrandr        | Yes                      | Yes           [3]          | Yes                                   | No
light         | Yes                      | No                         | Yes                                   | User must be in the `video` group [3]
[No program]  | Yes                      | Yes (slow)                 | Yes                                   | Read/write access for `/dev/i2c*` and `/sys/class/backlight`

#### Footnotes
[1] While both DDCUtil and the 1st party `linux.I2C` class do similar things over the same interface (I2C),
DDCUtil also supports communicating with monitors that implement the [Monitor Control Command Set over USB](https://www.ddcutil.com/usb)

[2] Read/write access for the `i2c` bus can be granted via the steps outlined in the [Desktop displays](#desktop-displays) section or by running the script using `sudo`.

[3] Xrandr does not actually change the backlight of the display, it just changes the brightness by applying a filter to the pixels to make them look dimmer/brighter.

[4] You can add yourself to the video user group by running `sudo usermod -a -G video [your username]` and then logging out and back in again for the changes to take effect.


## Install Instructions

* Arch
    * Xrandr: `sudo pacman -S xorg-xrandr`
    * DDCUtil: `sudo pacman -S ddcutil`
    * Light: `sudo pacman -S light-git`
* Debian/Ubuntu
    * XRandr: `sudo apt install x11-xserver-utils`
    * DDCUtil: `sudo apt install ddcutil`
    * Light: `sudo apt install light`
* Fedora
    * Xrandr: `sudo dnf install libXrandr`
    * DDCUtil: `sudo dnf install ddcutil`
    * Light: `sudo dnf install light`
'''
