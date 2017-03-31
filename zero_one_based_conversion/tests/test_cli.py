from unittest import TestCase
from zero_one_based_conversion import cli
import os.path
from click.testing import CliRunner


class TestMain(TestCase):
    def test_main(self):
        runner = CliRunner()

        with runner.isolated_filesystem():
            with open('test.bed', 'w') as f:
                f.write('1	143181282	143181282	C	G\n')
                f.write('4	49529381	49529381	C	G\n')
                f.write('4	49529380	49529381	-	G\n')

            result = runner.invoke(cli.main, ['-tb', 'zero',
                                              'test.bed', 'test.bed.zero'])
            self.assertEquals(result.exit_code, 0)
            self.assertTrue(os.path.isfile('test.bed.zero'))
            with open('test.bed.zero') as tf:
                converted = tf.read()
                self.assertMultiLineEqual(converted,
                                          '1\t143181281\t143181282\tC\tG\n'
                                          '4\t49529380\t49529381\tC\tG\n'
                                          '4\t49529380\t49529380\t-\tG\n')
