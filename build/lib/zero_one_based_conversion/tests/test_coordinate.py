from unittest import TestCase

from zero_one_based_conversion.coordinate import Coordinate


class TestCoordinate(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid_one_based_snv = Coordinate('7', '140534448', '140534448',
                                             'A', 'T')
        cls.valid_zero_based_snv = Coordinate('7', '140534447', '140534448',
                                              'A', 'T')
        cls.valid_one_based_sub = Coordinate('7', '140534448', '140534450',
                                             'AGG', 'CAT')
        cls.valid_zero_based_sub = Coordinate('7', '140534447', '140534450',
                                              'AGG', 'CAT')
        cls.valid_one_based_insertion = Coordinate('7', '140534447',
                                                   '140534448', '-', 'TTA')
        cls.valid_zero_based_insertion = Coordinate('7', '140534447',
                                                    '140534447', '-', 'TTA')
        cls.valid_one_based_deletion = Coordinate('7', '140534448',
                                                  '140534448', 'A', '-')
        cls.valid_zero_based_deletion = Coordinate('7', '140534447',
                                                   '140534448', 'A', '-')
        cls.valid_one_based_multideletion = Coordinate('7', '140534448',
                                                       '140534450', 'AGG', '-')
        cls.valid_zero_based_multideletion = Coordinate('7', '140534447',
                                                        '140534450',
                                                        'AGG', '-')

    def test_coordinate_initialization(self):
        self._assert_valid_coordinate_match(self.valid_one_based_snv, '7',
                                            140534448, 140534448, 'A', 'T', 1,
                                            'snv')
        self._assert_valid_coordinate_match(self.valid_zero_based_snv, '7',
                                            140534447, 140534448, 'A', 'T', 0,
                                            'snv')
        self._assert_valid_coordinate_match(self.valid_one_based_sub, '7',
                                            140534448, 140534450, 'AGG', 'CAT',
                                            1, 'sub')
        self._assert_valid_coordinate_match(self.valid_zero_based_sub, '7',
                                            140534447, 140534450, 'AGG', 'CAT',
                                            0, 'sub')
        self._assert_valid_coordinate_match(self.valid_one_based_insertion,
                                            '7', 140534447, 140534448, '-',
                                            'TTA', 1, 'ins')
        self._assert_valid_coordinate_match(self.valid_zero_based_insertion,
                                            '7', 140534447, 140534447, '-',
                                            'TTA', 0, 'ins')
        self._assert_valid_coordinate_match(self.valid_one_based_deletion, '7',
                                            140534448, 140534448, 'A', '-', 1,
                                            'del')
        self._assert_valid_coordinate_match(self.valid_zero_based_deletion,
                                            '7', 140534447, 140534448, 'A',
                                            '-', 0, 'del')
        self._assert_valid_coordinate_match(
            self.valid_one_based_multideletion, '7', 140534448, 140534450,
            'AGG', '-', 1, 'del')
        self._assert_valid_coordinate_match(
            self.valid_zero_based_multideletion, '7', 140534447, 140534450,
            'AGG', '-', 0, 'del')
        self.assertRaises(ValueError, Coordinate, '7', 140534448,
                          140, 'A', 'T')
        self.assertRaises(ValueError, Coordinate, '7', 140534448,
                          140, '-', 'T')
        self.assertRaises(ValueError, Coordinate, '7', 140534448,
                          140, 'A', '-')
        self.assertRaises(ValueError, Coordinate, '7', 140534448, 140534448,
                          'AG', 'T')
        self.assertRaises(ValueError, Coordinate, '7', 140534447, 140534448,
                          'AG', 'T')
        self.assertRaises(ValueError, Coordinate, '7', 140534448, 140534448,
                          'AG', '-')
        self.assertRaises(ValueError, Coordinate, '7', 140534447, 140534450,
                          'AG', '-')

    def test_to_zero_based(self):
        self.assertEquals(self.valid_one_based_snv.to_zero_based(),
                          '\t'.join(['7', '140534447',
                                     '140534448', 'A', 'T']))
        self.assertEquals(self.valid_zero_based_snv.to_zero_based(),
                          '\t'.join(['7', '140534447',
                                     '140534448', 'A', 'T']))
        self.assertEquals(self.valid_one_based_sub.to_zero_based(), '\t'.join(
            ['7', '140534447', '140534450', 'AGG', 'CAT']))
        self.assertEquals(self.valid_zero_based_sub.to_zero_based(), '\t'.join(
            ['7', '140534447', '140534450', 'AGG', 'CAT']))
        self.assertEquals(self.valid_one_based_insertion.to_zero_based(),
                          '\t'.join(
                              ['7', '140534447', '140534447', '-', 'TTA']))
        self.assertEquals(self.valid_zero_based_insertion.to_zero_based(),
                          '\t'.join(
                              ['7', '140534447', '140534447', '-', 'TTA']))
        self.assertEquals(self.valid_one_based_deletion.to_zero_based(),
                          '\t'.join(['7', '140534447', '140534448', 'A', '-']))
        self.assertEquals(self.valid_zero_based_deletion.to_zero_based(),
                          '\t'.join(['7', '140534447', '140534448', 'A', '-']))
        self.assertEquals(self.valid_one_based_multideletion.to_zero_based(),
                          '\t'.join(
                              ['7', '140534447', '140534450', 'AGG', '-']))
        self.assertEquals(self.valid_zero_based_multideletion.to_zero_based(),
                          '\t'.join(
                              ['7', '140534447', '140534450', 'AGG', '-']))

    def test_to_one_based(self):
        self.assertEquals(self.valid_one_based_snv.to_one_based(),
                          '\t'.join(['7', '140534448',
                                     '140534448', 'A', 'T']))
        self.assertEquals(self.valid_zero_based_snv.to_one_based(),
                          '\t'.join(['7', '140534448',
                                     '140534448', 'A', 'T']))
        self.assertEquals(self.valid_one_based_sub.to_one_based(), '\t'.join(
            ['7', '140534448', '140534450', 'AGG', 'CAT']))
        self.assertEquals(self.valid_zero_based_sub.to_one_based(), '\t'.join(
            ['7', '140534448', '140534450', 'AGG', 'CAT']))
        self.assertEquals(self.valid_one_based_insertion.to_one_based(),
                          '\t'.join(
                              ['7', '140534447', '140534448', '-', 'TTA']))
        self.assertEquals(self.valid_zero_based_insertion.to_one_based(),
                          '\t'.join(
                              ['7', '140534447', '140534448', '-', 'TTA']))
        self.assertEquals(self.valid_one_based_deletion.to_one_based(),
                          '\t'.join(['7', '140534448', '140534448', 'A', '-']))
        self.assertEquals(self.valid_zero_based_deletion.to_one_based(),
                          '\t'.join(['7', '140534448', '140534448', 'A', '-']))
        self.assertEquals(self.valid_one_based_multideletion.to_one_based(),
                          '\t'.join(
                              ['7', '140534448', '140534450', 'AGG', '-']))
        self.assertEquals(self.valid_zero_based_multideletion.to_one_based(),
                          '\t'.join(
                              ['7', '140534448', '140534450', 'AGG', '-']))

    def _assert_valid_coordinate_match(self, coordinate, chrom, start, stop,
                                       ref, var,
                                       coordinate_system, mutation_type):
        self.assertEquals(coordinate.chromosome, chrom)
        self.assertEquals(coordinate.start, start)
        self.assertEquals(coordinate.stop, stop)
        self.assertEquals(coordinate.ref, ref)
        self.assertEquals(coordinate.var, var)
        self.assertEquals(coordinate.coordinate_system, coordinate_system)
        self.assertEquals(coordinate.mutation_type, mutation_type)

    def _assert_invalid_coordinate_match(self, coordinate, chrom, start, stop,
                                         ref, var,
                                         coordinate_system, mutation_type):
        self.assertEquals(coordinate.chromosome, chrom)
        self.assertEquals(coordinate.start, start)
        self.assertEquals(coordinate.stop, stop)
        self.assertEquals(coordinate.ref, ref)
        self.assertEquals(coordinate.var, var)
        self.assertEquals(coordinate.coordinate_system, coordinate_system)
        self.assertEquals(coordinate.mutation_type, mutation_type)
