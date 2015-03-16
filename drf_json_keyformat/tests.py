import unittest
from drf_json_keyformat import transformations

class TestToCase(unittest.TestCase):

    def test_str_to_case(self):
        cases = (
            'camels_have_humps',
            'camels_haveHumps',
            'camelsHave_humps',
            'camelsHaveHumps',
            'camels_Have_humps',
            'Camels_Have_Humps',
            'Camels_Have_humps',
            '_camels_have_humps',
            '_Camels_have_humps',
        )
        for case in cases:
            self.assertEqual('camelsHaveHumps', transformations.str_to_camelcase(case))
            self.assertEqual('CamelsHaveHumps', transformations.str_to_pascalcase(case))


    def test_str_to_snake(self):
        cases = (
            'camelsHaveHumps',
            'CamelsHaveHumps',
            'camelsHAVEHumps',
            'camelsHaveHUMPS',
            'CAMELSHaveHumps',
        )
        for case in cases:
            self.assertEqual('camels_have_humps', transformations.str_to_snakecase(case))


    def test_dict_keys(self):
        d = {'key_one': 1, 'key_two': 2}
        cd = {'keyOne': 1, 'keyTwo': 2}
        pd = {'KeyOne': 1, 'KeyTwo': 2}

        # to camel/pascal
        self.assertEqual(cd, transformations.keys_to_camelcase(d))
        self.assertEqual(pd, transformations.keys_to_pascalcase(d))

        # to snake
        self.assertEqual(d, transformations.keys_to_snakecase(cd))
        self.assertEqual(d, transformations.keys_to_snakecase(pd))


    def test_nested_dict_keys(self):
        d = {'key_one': 1, 'key_two': 2, 'key_three': {'nest_data': 'n'}}
        cd = {'keyOne': 1, 'keyTwo': 2, 'keyThree': {'nestData': 'n'}}
        pd = {'KeyOne': 1, 'KeyTwo': 2, 'KeyThree': {'NestData': 'n'}}

        # to camel/pascal
        self.assertEqual(cd, transformations.keys_to_camelcase(d))
        self.assertEqual(pd, transformations.keys_to_pascalcase(d))

        # to snake
        self.assertEqual(d, transformations.keys_to_snakecase(cd))
        self.assertEqual(d, transformations.keys_to_snakecase(pd))


    def test_nested_list_dict_keys(self):
        d = {'key_one': 1, 'key_two': [{'nest_data_one': 1}, {'nest_data_two': 2}]}
        cd = {'keyOne': 1, 'keyTwo': [{'nestDataOne': 1}, {'nestDataTwo': 2}]}
        pd = {'KeyOne': 1, 'KeyTwo': [{'NestDataOne': 1}, {'NestDataTwo': 2}]}

        # to camel/pascal
        self.assertEqual(cd, transformations.keys_to_camelcase(d))
        self.assertEqual(pd, transformations.keys_to_pascalcase(d))

        # to snake
        self.assertEqual(d, transformations.keys_to_snakecase(cd))
        self.assertEqual(d, transformations.keys_to_snakecase(pd))
