'''
Not to be confused with `tests/helpers.py`, this file contains tests
for code in the `screen_brightness_control/helpers.py` file
'''
import os
import sys
import unittest

import helpers
from helpers import TestCase

sys.path.insert(0, os.path.abspath('./'))
import screen_brightness_control as sbc  # noqa: E402


class TestEDID(TestCase):
    def test_parser(self):
        monitors = [i for i in sbc.list_monitors_info() if isinstance(i['edid'], str)]

        for monitor in monitors:
            edid = monitor['edid']
            mfg_id, manufacturer, model, name, serial = sbc.helpers.EDID.parse(edid)

            self.assertIsInstance(mfg_id, (str, type(None)))
            if mfg_id is not None:
                self.assertEqual(len(mfg_id), 3)

            self.assertIsInstance(manufacturer, (str, type(None)))
            self.assertIsInstance(model, (str, type(None)))
            self.assertIsInstance(name, (str, type(None)))
            self.assertIsInstance(serial, (str, type(None)))


class TestMonitorBrandLookup(unittest.TestCase):
    def test_code(self):
        test_codes = sbc.helpers.MONITOR_MANUFACTURER_CODES.keys()
        for code in test_codes:
            variations = [
                code, code.lower(), code.upper(),
                code.lower().capitalize()
            ]
            for var in variations:
                self.assertEqual(
                    sbc.helpers._monitor_brand_lookup(var),
                    (code, sbc.helpers.MONITOR_MANUFACTURER_CODES[code])
                )

    def test_name(self):
        reverse_dict = {v: k for k, v in sbc.helpers.MONITOR_MANUFACTURER_CODES.items()}
        test_names = reverse_dict.keys()
        for name in test_names:
            variations = [
                name, name.lower(), name.upper(),
                name.lower().capitalize()
            ]
            for var in variations:
                try:
                    self.assertEqual(
                        sbc.helpers._monitor_brand_lookup(var),
                        (reverse_dict[name], name)
                    )
                except AssertionError:
                    # for duplicate keys. EG: Acer has codes "ACR" and "CMO"
                    assert sbc.helpers.MONITOR_MANUFACTURER_CODES[reverse_dict[name]] == name

    def test_invalid(self):
        invalids = ['TEST', 'INVALID', 'ITEMS']
        for item in invalids:
            self.assertEqual(sbc.helpers._monitor_brand_lookup(item), None)


class TestLogarithmicRange(unittest.TestCase):
    def test_normal(self):
        for l_bound, u_bound in ((0, 100), (0, 10), (29, 77), (99, 100)):
            l_range = list(sbc.helpers.logarithmic_range(l_bound, u_bound))
            n_range = list(range(l_bound, u_bound))

            self.assertLessEqual(len(l_range), len(n_range))
            self.assertLessEqual(max(l_range), u_bound)
            self.assertGreaterEqual(min(l_range), l_bound)

            self.assertTrue(all(isinstance(i, int) for i in l_range))

    def test_skip_intervals(self):
        for l_bound, u_bound in (
            (0, 100), (0, 50), (50, 100), (0, 25), (25, 50), (50, 75), (75, 100)
        ):
            l_range = list(sbc.helpers.logarithmic_range(l_bound, u_bound))

            # assert the lower value items have a lower diff than higher items
            self.assertLessEqual(l_range[1] - l_range[0], l_range[-1] - l_range[-2])

            l_range = list(sbc.helpers.logarithmic_range(u_bound, l_bound, -1))

            # assert higher value items have higher diff than lower items
            self.assertGreaterEqual(l_range[0] - l_range[1], l_range[-2] - l_range[-1])


if __name__ == '__main__':
    if '--synthetic' in sys.argv:
        sys.argv.remove('--synthetic')
        helpers.TEST_FAST = True
    else:
        helpers.TEST_FAST = False

    unittest.main()
