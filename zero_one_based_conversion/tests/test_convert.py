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
        zero_based = '''1	880975	880976	T	G
1	2443098	2443099	A	T
1	11187133	11187134	C	T
7	14053447	14053450	AAG	CAT
7	14053447	14053447	-	TTA
7	14053447	14053448	A	-'''
        zero_based_extra_columns = '''1	880975	880976	T	G	S
1	2443098	2443099	A	T	S
1	11187133	11187134	C	T	S
7	14053447	14053450	AAG	CAT	F
7	14053447	14053447	-	TTA	F
7	14053447	14053448	A	-	F'''
        mixed_coords = '''1	880975	880975	T	G
1	2443098	2443098	A	T
1	11187133	11187133	C	T
7	14053448	14053450	AAG	CAT
7	14053447	14053448	-	TTA
7	14053448	14053448	A	-
1	2443098	2443099	A	T
1	11187133	11187134	C	T
7	14053447	14053450	AAG	CAT
7	14053447	14053447	-	TTA
7	14053447	14053448	A	-'''
        self.assertEquals(convert.coordinate_system(one_based,
                                                    'to_zero_based'),
                          zero_based)
        self.assertEquals(convert.coordinate_system(one_based_extra_columns,
                                                    'to_zero_based'),
                          zero_based_extra_columns)
        self.assertEquals(convert.coordinate_system(zero_based,
                                                    'to_one_based'),
                          one_based)
        self.assertEquals(convert.coordinate_system(mixed_coords,
                                                    'to_zero_based'),
                          zero_based+'\n'+zero_based)
