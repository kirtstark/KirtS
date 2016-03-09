from mock.mock import self

from source.main2 import *
import mock
from unittest import TestCase
from test.plugins.ReqTracer import requirements
import os


class TestMockingGit(TestCase):
    """ class to test mocking objects in Python"""

#    current_file = (str(os.getcwd())) + '\\source\\main2.py'
#    current_file = 'C:\\Users\\Devon\\Documents\\GitHub\\Kirt.Stark\\KirtS\\cst236_lab1\\source\\main2.py'
    current_file = '/home/ubuntu/src/github.com/kirtstark/KirtS/cst236_lab1/cst236_lab1/source/main2.py'
    good = current_file
    normal = ('return nothing', None)
    found = (current_file, None)
    empty = ('', None)
    missing = (None, None)

    @requirements(['#0100'])
    @mock.patch('subprocess.Popen')
    def test_is_path_in_repo(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': (self.good, 'error')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        result = is_file_in_repo(path)
        self.assertTrue(mock_subproc_popen.called)
        self.assertEqual(result, 'No')

    @requirements(['#0100'])
    @mock.patch('subprocess.Popen')
    def test_is_path_in_repo1(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ('output', 'error')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        questions = Interface()
        inquiry = "Is the " + path + " in the repo" + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, 'Yes')

    @requirements(['#0100'])
    def test_is_path_in_repo2(self):
        path = 'source/main3.py'
        questions = Interface()
        inquiry = "Is the " + path + " in the repo" + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, 'No')

    @requirements(['#0100'])
    @mock.patch('subprocess.Popen')
    def test_is_path_in_repo3(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': (self.good, 'error')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        questions = Interface()
        inquiry = "Is the " + path + " in the repo" + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, 'No')

    @requirements(['#0100'])
    @mock.patch('subprocess.Popen')
    def test_is_path_in_repo4(self, mock_subproc_popen):
        lists = (self.normal, self.normal, self.found, self.normal, self.normal, self.normal)
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': lists}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        questions = Interface()
        inquiry = "Is the " + path + " in the repo" + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, 'No')

    @requirements(['#0100'])
    @mock.patch('subprocess.Popen')
    def test_is_path_in_repo5(self, mock_subproc_popen):
        lists = (self.normal, self.normal, self.normal, self.found, self.normal, self.normal)
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': lists}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        questions = Interface()
        inquiry = "Is the " + path + " in the repo" + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, 'Yes')

    @requirements(['#0100'])
    @mock.patch('subprocess.Popen')
    def test_is_path_in_repo6(self, mock_subproc_popen):
        lists = (self.normal, self.normal, self.normal, self.normal, self.found, self.normal)
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': lists}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        questions = Interface()
        inquiry = "Is the " + path + " in the repo" + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, 'No')

    @requirements(['#0100'])
    @mock.patch('subprocess.Popen')
    def test_is_path_in_repo7(self, mock_subproc_popen):
        lists = (self.normal, self.normal, self.normal, self.normal, self.normal, self.found)
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': lists}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        questions = Interface()
        inquiry = "Is the " + path + " in the repo" + chr(0x3F)
        result = questions.ask(inquiry)
        self.assertEqual(result, 'Yes')

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_get_file_status1(self, mock_subproc_popen):
        lists = (self.normal, self.normal, self.found, self.normal)
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': lists}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        questions = Interface()
        inquiry = "What is the status of " + path + chr(0x3F)
        exp_response = os.path.basename(path) + ' has been modified locally'
        result = questions.ask(inquiry)
        self.assertEqual(result, exp_response)

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_get_file_status2(self, mock_subproc_popen):
        lists = (self.found, self.normal, self.normal, self.normal)
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': lists}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        questions = Interface()
        inquiry = "What is the status of " + path + chr(0x3F)
        exp_response = os.path.basename(path) + ' has been modified locally'
        result = questions.ask(inquiry)
        self.assertEqual(result, exp_response)

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_get_file_status3(self, mock_subproc_popen):
        lists = (self.found, self.normal, self.found, self.normal)
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': lists}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        questions = Interface()
        inquiry = "What is the status of " + path + chr(0x3F)
        exp_response = os.path.basename(path) + ' has been modified locally'
        result = questions.ask(inquiry)
        self.assertEqual(result, exp_response)

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_get_file_status4(self, mock_subproc_popen):
        lists = (self.normal, self.normal, self.normal, self.normal, self.found, self.found)
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': lists}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        questions = Interface()
        inquiry = "What is the status of " + path + chr(0x3F)
        exp_response = os.path.basename(path) + ' has been not been checked in'
        result = questions.ask(inquiry)
        self.assertEqual(result, exp_response)

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_get_file_status5(self, mock_subproc_popen):
        lists = (self.normal, self.normal, self.normal, self.normal, self.normal, self.normal, self.normal, self.normal,
                 self.normal, self.normal)
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': lists}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        questions = Interface()
        inquiry = "What is the status of " + path + chr(0x3F)
        exp_response = os.path.basename(path) + ' is a dirty repo'
        result = questions.ask(inquiry)
        self.assertEqual(result, exp_response)

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_get_file_status6(self, mock_subproc_popen):
        lists = (self.normal, self.normal, self.normal, self.normal, self.normal, self.normal, self.empty, self.empty,
                 self.empty, self.empty)
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': lists}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        questions = Interface()
        inquiry = "What is the status of " + path + chr(0x3F)
        exp_response = os.path.basename(path) + ' is up to date'
        result = questions.ask(inquiry)
        self.assertEqual(result, exp_response)

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_get_file_status7(self, mock_subproc_popen):
        lists = (self.normal, self.normal, self.normal, self.normal, self.normal, self.normal, self.normal, self.normal,
                 self.found, self.found)
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': lists}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        questions = Interface()
        inquiry = "What is the status of " + path + chr(0x3F)
        exp_response = os.path.basename(path) + ' is a dirty repo'
        result = questions.ask(inquiry)
        self.assertEqual(result, exp_response)

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_get_file_status8(self, mock_subproc_popen):
        lists = (self.normal, self.normal, self.normal, self.normal, self.normal, self.normal, self.found, self.found,
                 self.normal, self.normal)
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': lists}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        questions = Interface()
        inquiry = "What is the status of " + path + chr(0x3F)
        exp_response = os.path.basename(path) + ' is a dirty repo'
        result = questions.ask(inquiry)
        self.assertEqual(result, exp_response)

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_get_file_status9(self, mock_subproc_popen):
        lists = (self.normal, self.normal, self.normal, self.normal, self.normal, self.normal, self.empty, self.empty,
                 self.normal, self.normal)
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': lists}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        questions = Interface()
        inquiry = "What is the status of " + path + chr(0x3F)
        exp_response = os.path.basename(path) + ' is a dirty repo'
        result = questions.ask(inquiry)
        self.assertEqual(result, exp_response)

    @requirements(['#0102'])
    @mock.patch('subprocess.Popen')
    def test_get_file_info1(self, mock_subproc_popen):
        lists = {"H": "145","cd": "february", "an": "Kirt Stark"}
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ("#333  February 16  Kirt Stark", None)}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        questions = Interface()
        inquiry = "What is the deal with " + path + chr(0x3F)
        exp_response = "#333  February 16  Kirt Stark"
        result = questions.ask(inquiry)
        self.assertEqual(result, exp_response)

    @requirements(['#0103'])
    @mock.patch('subprocess.Popen')
    def test_get_repo_branch1(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ("KirtS", None)}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main2.py'
        questions = Interface()
        inquiry = "What branch is " + path + chr(0x3F)
        exp_response = "KirtS"
        result = questions.ask(inquiry)
        self.assertEqual(result, exp_response)

    @requirements(['#0104'])
    @mock.patch('subprocess.Popen')
    def test_get_repo_url1(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ("https://github.com/OregonTech/KirtS", None)}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = self.good
        questions = Interface()
        inquiry = "Where did " + path + " come from " + chr(0x3F)
        exp_response = "https://github.com/OregonTech/KirtS"
        result = questions.ask(inquiry)
        self.assertEqual(result, exp_response)

    @requirements(['#0105'])
    @mock.patch('subprocess.Popen')
    def test_get_repo_root(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': ("https:\\github.com\\OregonTech\\KirtS", None)}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = self.good
        questions = Interface()
        inquiry = "What is the repo root for " + path + chr(0x3F)
        exp_response = "https:\\github.com\\OregonTech\\KirtS"
        result = questions.ask(inquiry)
        self.assertEqual(result, exp_response)

    @requirements(['#0106'])
    @mock.patch('subprocess.Popen')
    def test_get_file_status9b(self, mock_subproc_popen):
        lists = (self.normal, self.normal, self.normal, self.normal, self.normal, self.normal, self.empty, self.empty,
                 self.normal, self.normal)
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': lists}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        path = 'source/main3.py'
        questions = Interface()
        inquiry = "What is the status of " + path + chr(0x3F)
        self.assertRaisesRegexp(Exception, "Too many extra parameters", questions.ask, inquiry)