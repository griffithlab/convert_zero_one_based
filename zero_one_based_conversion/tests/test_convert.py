from unittest import TestCase
from zero_one_based_conversion import convert


class TestConvert(TestCase):
    def test_convert(self):
        one_based = '''1	880975	880975	T	G
1	2443098	2443098	A	T
1	11187133	11187133	C	T
7	14053448	14053450	AAG	CAT
7	14053447	14053448	-	TTA
7	14053448	14053448	A	-'''
        one_based_extra_columns = '''1	880975	880975	T	G	S
1	2443098	2443098	A	T	S
1	11187133	11187133	C	T	S
7	14053448	14053450	AAG	CAT	F
7	14053447	14053448	-	TTA	F
7	14053448	14053448	A	-	F'''
        zero_based = '''1	880974	880975	T	G
1	2443097	2443098	A	T
1	11187132	11187133	C	T
7	14053447	14053450	AAG	CAT
7	14053447	14053447	-	TTA
7	14053447	14053448	A	-'''
        zero_based_extra_columns = '''1	880974	880975	T	G	S
1	2443097	2443098	A	T	S
1	11187132	11187133	C	T	S
7	14053447	14053450	AAG	CAT	F
7	14053447	14053447	-	TTA	F
7	14053447	14053448	A	-	F'''
        mixed_coords = '''1	880975	880975	T	G
1	2443098	2443098	A	T
1	11187133	11187133	C	T
7	14053448	14053450	AAG	CAT
7	14053447	14053448	-	TTA
7	14053448	14053448	A	-
1	880974	880975	T	G
1	2443097	2443098	A	T
1	11187132	11187133	C	T
7	14053447	14053450	AAG	CAT
7	14053447	14053447	-	TTA
7	14053447	14053448	A	-'''
        one_based_empty_lines = '''1	880975	880975	T	G
1	2443098	2443098	A	T
1	11187133	11187133	C	T
7	14053448	14053450	AAG	CAT

7	14053447	14053448	-	TTA
7	14053448	14053448	A	-
'''
        misformated_coords_string = '''1	880975	880975	T	G
1	2443098	2443098	A	T
1	11187133	11187133	5	T
7	A	14053450	AAG	CAT
-	14053447	14053448	-	TTA
7	14053448	14053448	A	-'''
        one_to_zero = convert.coordinate_system(one_based, 'to_zero_based')
        self.assertMultiLineEqual(one_to_zero, zero_based)
        one_to_zero_extra_cols = convert.coordinate_system(
            one_based_extra_columns, 'to_zero_based')
        self.assertMultiLineEqual(one_to_zero_extra_cols,
                                  zero_based_extra_columns)
        zero_to_one = convert.coordinate_system(zero_based, 'to_one_based')
        self.assertMultiLineEqual(zero_to_one, one_based)
        mixed_coords_convert = convert.coordinate_system(mixed_coords,
                                                         'to_zero_based')
        self.assertMultiLineEqual(mixed_coords_convert,
                                  zero_based+'\n'+zero_based)
        one_based_empty_lines_to_zero = convert.coordinate_system(
            one_based_empty_lines, 'to_zero_based')
        self.assertMultiLineEqual(one_based_empty_lines_to_zero, zero_based)
        self.assertRaises(ValueError, convert.coordinate_system,
                          misformated_coords_string, 'to_zero_based')
