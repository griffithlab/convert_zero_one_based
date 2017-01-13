class Coordinate:
    """Coordinate validates coordinate data and converts coordinate systems.

    Chromosome, start, stop, reference and variant values are validated to
    a one-based or zero-based coordinate system. Following validation the
    coordinate data is converted to one-based or zero-based coordinate systems
    using the to_base() function.

    Attributes:
        chromosome (str): Chromosome name.
        start (int): Starting coordinate.
        stop (int): Ending coordinate.
        ref (str): Genome reference base.
        var (str): Variant base.
        coordinate_system (1 or 0): 1 if coordinate is one-based, 0 if
            zero-based.
        mutation_type ('snv', 'ins', 'del', 'sub'): Specifies mutation type.
    """

    def __init__(self, chromosome, start, stop, ref, var):
        """Initialize and validate coordinate.

        Args:
            chromosome (str): Chromosome name.
            start (str): Starting coordinate.
            stop (str): Ending coordinate.
            ref (str): Genome reference base.
            var (str): Variant base.
        """
        self._set_coordinate(chromosome, start, stop, ref, var)

    def _set_coordinate(self, chromosome, start, stop, ref, var):
        """"""
        self.chromosome = chromosome
        self.start = int(start)
        self.stop = int(stop)
        self.ref = ref
        self.var = var
        self._determine_mutation_type()
        self._determine_coordinate_system()

    def _determine_mutation_type(self):
        """Determines the mutation type from start, stop, ref, var"""
        if self.ref in ['-', '.', '0']:
            self.mutation_type = 'ins'
        elif self.var in ['-', '.', '0']:
            self.mutation_type = 'del'
        elif len(self.ref) == 1 and len(self.var) == 1:
            self.mutation_type = 'snv'
        elif len(self.ref) == len(self.var) and len(self.ref) > 1:
            self.mutation_type = 'sub'
        else:
            raise ValueError('The coordinate, {0} inputs do not resolve to a '
                             'valid variant type (snv, ins, '
                             'del, sub).'.format(self.to_string()))

    def _determine_coordinate_system(self):
        """Determines the coordinate system using the coordinates and inferred
        mutation type."""
        if self.mutation_type is 'snv':
            if self.start + 1 == self.stop:
                self.coordinate_system = 0
            elif self.start == self.stop:
                self.coordinate_system = 1
            else:
                raise ValueError('The reference and variant fields indicate a '
                                 'single nucleotide variant, however the '
                                 'coordinates ({0} and {1}) are not valid '
                                 'for this mutation type. Coordinate: '
                                 '{2}'.format(self.start, self.stop,
                                              self.to_string()))
        elif self.mutation_type is 'ins':
            if self.start == self.stop:
                self.coordinate_system = 0
            elif self.start == self.stop - 1:
                self.coordinate_system = 1
            else:
                raise ValueError('For the coordinate {0}, the reference and '
                                 'variant fields indicate an insertion '
                                 'variant, however the coordinates ({1} and '
                                 '{2}) are not valid for these mutation '
                                 'types.'.format(self.to_string(),
                                                 self.start, self.stop))
        elif self.mutation_type in ['del', 'sub']:
            if self.start + len(self.ref) == self.stop:
                self.coordinate_system = 0
            elif self.stop - self.start == len(self.ref) - 1:
                self.coordinate_system = 1
            else:
                raise ValueError('For the coordinate {0}, the reference and '
                                 'variant fields indicate an deletion or '
                                 'substitution variant, however the '
                                 'coordinates ({1} and {2}) are not valid for '
                                 'these mutation types.'.format(
                    self.to_string(), self.start, self.stop))

    def to_zero_based(self):
        """Converts coordinate to zero-based and returns a tab-delimited string.

        Returns:
            Tab-delimited string of coordinates in zero-based coordinate
                system. Values are positionally formatted as chromosome, start,
                stop, reference, variant.
        """
        if self.coordinate_system == 0:
            zero_based = '\t'.join([self.chromosome, str(self.start),
                                    str(self.stop), self.ref, self.var])
        elif self.coordinate_system == 1:
            if self.mutation_type is 'snv':
                zero_based = '\t'.join([self.chromosome, str(self.start - 1),
                                        str(self.stop), self.ref, self.var])
            elif self.mutation_type is 'ins':
                zero_based = '\t'.join([self.chromosome, str(self.start),
                                        str(self.stop - 1), self.ref, self.var])
            elif self.mutation_type in ['del', 'sub']:
                zero_based = '\t'.join([self.chromosome, str(self.start - 1),
                                        str(self.stop), self.ref, self.var])
            else:
                raise ValueError("Coordinate, {0}, is not valid mutation "
                                 "type".format(self.to_string()))
        else:
            raise ValueError("Coordinate, {0}, is not valid coordinate "
                             "system".format(self.to_string()))
        return zero_based

    def to_one_based(self):
        """Converts coordinate to one-based and returns a tab-delimited string.

        Returns:
            Tab-delimited string of coordinates in one-based coordinate system.
                Values are positionally formatted as chromosome, start, stop,
                reference, variant.
        """
        if self.coordinate_system == 1:
            one_based = '\t'.join([self.chromosome, str(self.start),
                                   str(self.stop), self.ref, self.var])
        elif self.coordinate_system == 0:
            if self.mutation_type is 'snv':
                one_based = '\t'.join([self.chromosome, str(self.start + 1),
                                       str(self.stop), self.ref, self.var])
            elif self.mutation_type is 'ins':
                one_based = '\t'.join([self.chromosome, str(self.start),
                                       str(self.stop + 1), self.ref, self.var])
            elif self.mutation_type in ['del', 'sub']:
                one_based = '\t'.join([self.chromosome, str(self.start + 1),
                                       str(self.stop), self.ref, self.var])
            else:
                raise ValueError("Coordinate, {0}, is not valid mutation "
                                 "type".format(self.to_string()))
        else:
            raise ValueError("Coordinate, {0}, is not valid coordinate "
                             "system".format(self.to_string()))
        return one_based

    def to_string(self):
        return '{0}:{1}-{2}{3}>{4}'.format(self.chromosome, self.start,
                                           self.stop, self.ref, self.var)
