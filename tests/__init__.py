#!/usr/bin/env python

import unittest
import subprocess
import tempfile
import os
import shutil
import pipi

class TestMain(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestMain, self).__init__(*args, **kwargs)
        self.maindir = os.getcwd()

class TestFunctions(TestMain):

    def test_package_slug(self):
        self.assertEqual(pipi.package_slug("test==4.4.4"), 'test')
        self.assertEqual(pipi.package_slug("test-package==4.4.4"), 'test-package')
        self.assertEqual(pipi.package_slug("test-package>=4.4.4"), 'test-package')
        self.assertEqual(pipi.package_slug("test-package~=4.4.4"), 'test-package')

    def test_requirements(self):
        path = pipi.create_req_if_not_exists(self.maindir)
        self.assertEqual('%s/requirements.txt' % (self.maindir), path)

        file_exists = False
        if os.path.isfile(path):
            file_exists = True
        self.assertTrue(file_exists)
        os.unlink(path)

class TestResults(TestMain):

    def test_results(self):
        command = "pipi tornado".split()
        proc = subprocess.Popen(command, cwd=self.maindir, stdout=subprocess.PIPE)
        data, err = proc.communicate()
        self.assertIsNone(err)

if __name__ == '__main__':
    unittest.main()
