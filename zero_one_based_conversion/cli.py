import pkg_resources

import click

from zero_one_based_conversion import convert


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    version = pkg_resources.get_distribution('convert_zero_one_based').version
    click.echo(version)
    ctx.exit()


@click.command()
@click.option('-v', '--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True)
@click.help_option('-h', '--help')
@click.option('--to-base', '-tb', type=click.Choice(['zero', 'one']),
              default='one', help='Specify output file format: one-based or '
                                  'zero-based cordinate systems (default:one)')
@click.option('--header/--no-header',
              default=False,
              help='Specify whether header is present in INPUT_FILE')
@click.argument('input_file', type=click.File('r'))
@click.argument('output_file', type=click.File('w'))
def main(to_base, header, input_file, output_file):
    """
    Converts a tab-separated INPUT_FILE containing chromosome, start, stop,
    reference, and variant (in that order) which is formatted with an unknown
    coordinate system to a tab-separated OUTPUT_FILE which has been formatted
    to the coordinate system specified by the --to-base option.
    """
    if header:
        output_file.write(input_file.readline())

    if to_base == 'one':
        output_file.write(convert.coordinate_system(input_file.read(),
                                                    'to_one_based'))
        # click.echo(converted)
    elif to_base == 'zero':
        output_file.write(convert.coordinate_system(input_file.read(),
                                                    'to_zero_based'))
    else:
        raise RuntimeError('Invalid to-base parameter')
        # click.echo(input_file)


if __name__ == '__main__':
    main()
