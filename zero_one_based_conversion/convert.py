import re
from zero_one_based_conversion.coordinate import Coordinate


def coordinate_system(input_string, convert_to_coordinate_system):
    """Converts strings of cordinates to one-based or zero-based

    Args:
        input_string (str): A tab-delimited string of one or many coordinates
            (separated by newline characters). Valid coordinates contain
            chromosome, start position, stop position, reference base, and
            variant base, in that order. Additional columns are accepted and
            appended on the converted string.
        convert_to_coordinate_system ('to_one_based', 'to_zero_based'): The
            coordinate system you would like to convert to.

    Returns:
        str: Tab-delimited string of the converted coordinates, multiple
            coordinates are separated by newline characters.
    """
    output_string = ''
    line_number = 0
    for line in input_string.split('\n'):
        try:
            line_number += 1
            pattern = re.compile("\w+\t\d+\t\d+\t[ACGT\-\.0]+\t[ACGT\-\.0]+.*")
            if line == '':
                continue  # skip empty lines
            elif not pattern.match(line):
                raise ValueError('Invalid format, expected chr, start, stop, '
                                 'ref, var. Line: {0}'.format(line))
            coord = line.split('\t')
            extra_cols = []
            if len(coord) > 5:
                extra_cols = coord[5:]
                del coord[5:]

            if convert_to_coordinate_system is 'to_zero_based':
                out = '\t'.join([Coordinate(coord[0], coord[1], coord[2],
                                            coord[3], coord[4])
                                .to_zero_based()] + extra_cols)
            elif convert_to_coordinate_system is 'to_one_based':
                out = '\t'.join([Coordinate(coord[0], coord[1], coord[2],
                                            coord[3], coord[4])
                                .to_one_based()] + extra_cols)
        except ValueError as error:
            print('Coordinate Error in line {0} or input. Coordinate skipped.'
                  '\n\tMessage: {1}'.format(line_number, error))
            continue
        output_string += out + '\n'
    return output_string.strip()
