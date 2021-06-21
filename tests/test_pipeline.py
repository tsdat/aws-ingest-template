import os
import sys
import unittest

# Add the project directory to the pythonpath
test_dir = os.path.dirname(os.path.realpath(__file__))
project_dir = os.path.dirname(test_dir)
lambda_dir = os.path.join(project_dir, 'lambda_function')
data_dir = os.path.join(project_dir, 'data')
sys.path.insert(0, lambda_dir)

from pipelines.runner import run_pipeline


class TestPipeline(unittest.TestCase):
    """-------------------------------------------------------------------
    Tests running the suite of a2e tsdat pipelines on the local
    filesystem.
    -------------------------------------------------------------------"""
    def setUp(self) -> None:
        # Set the environment variables for storage
        os.environ['STORAGE_CLASSNAME'] = 'tsdat.io.FilesystemStorage'
        os.environ['RETAIN_INPUT_FILES'] = 'True'
        os.environ['ROOT_DIR'] = os.path.join(data_dir, 'storage')

    def tearDown(self) -> None:
        super().tearDown()

    def test_buoy(self):
        run_pipeline([os.path.join(data_dir, 'a2e_buoy_ingest/humboldt/buoy.z05.00.20201201.000000.zip')])
        run_pipeline([os.path.join(data_dir, 'a2e_buoy_ingest/morro/buoy.z06.00.20201201.000000.zip')])


if __name__ == '__main__':
    unittest.main()
