from diskutil import rm

import unittest
import mock


class RmTest(unittest.TestCase):

    @mock.patch('diskutil.os')
    @mock.patch('diskutil.os.path')
    def test_rm(self, mock_os, mock_os_path):
        mock_os_path.isfile.return_value = False

        rm("any_path")

        self.assertFalse(
            mock_os.remove.called,
            "Failed to not remove the file")

if __name__ == '__main__':
    unittest.main()
