import subprocess 
class Brightness(object):
     """Set brightness"""
     def __init__(self):
          self.get_cur_brightness_per = subprocess.getoutput(cmd='brightness -l')


     def set_brightness(self, brightness_percent: int):
          """
       Automatically set brightness
       percent [type - int]
       example: 25; 50; 75; 100(max)
       :param brightness_percent:
       :return: Successfully
       """

          if not isinstance(brightness_percent, int):
               raise ValueError('Type value of brightness must be ', {int})

          else:
               if brightness_percent == 100:
                    brightness_percent -= brightness_percent + 1
                    subprocess.getoutput(cmd=f'brightness 1')

               elif isinstance(brightness_percent / 10, float):
                    brightness_percent *= 10
                    subprocess.getoutput(cmd=f'brightness 0.{brightness_percent}')

               else:
                    subprocess.getoutput(cmd=f'brightness 0.{brightness_percent}')

     def set_max_brightness(self):
          """
       Set max brightness of
       screen equal one hundred.
       :return: Successfully
       """
          subprocess.getoutput(cmd='brightness -v 1')

     def set_min_brightness(self):
          """
       Set min brightness of
       screen equal zero.
       :return: Successfully
       """

          subprocess.getoutput(cmd='brightness -v 0')
     def increase_brightness(self):
          """Set brightness increase by 1 division"""
          subprocess.getoutput(cmd="""osascript -e 'tell application "System Events"' -e 'key code 144' -e ' end tell'""")
     def lower_brightness(self):
          """Set brightness lower by 1 division"""

          subprocess.getoutput(cmd="""osascript -e 'tell application "System Events"' -e 'key code 145' -e ' end tell'""")


     @property
     def get_brightness(self):
          return round(float(self.get_cur_brightness_per.split(' ')[-1]), ndigits=2)
