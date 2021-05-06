from unittest import TestCase

from joblib import delayed

from ngs_utils import utils

from . import mixins


class TestUtils(mixins.TestMixin, TestCase):

    def test_ParallelWithProgress(self):
        utils.ParallelWithProgress(
            delayed(mixins.dummy_function)() for _ in range(10)
        )

    def test_is_gzip(self):
        self.assertTrue(utils.is_gzip(self.fastq_gz_path))
        self.assertFalse(utils.is_gzip(self.fastq_path))
