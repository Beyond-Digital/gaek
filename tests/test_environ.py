#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_environ
----------------------------------

Tests for `environ` module.
"""

import os
import unittest

from google.appengine.api import app_identity
from google.appengine.api import modules
from google.appengine.api import namespace_manager
from google.appengine.ext import testbed

from gaek import environ


class TestEnviron(unittest.TestCase):

    def setUp(self):
        # Setups app engine test bed.
        # http://code.google.com/appengine/docs/python/tools/localunittesting.html
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        # Declare which service stubs you want to use.
        self.testbed.init_app_identity_stub()
        self.testbed.init_modules_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_app_identity_functions(self):
        assert app_identity.get_application_id == environ.get_application_id
        assert app_identity.get_default_version_hostname == environ.get_default_version_hostname
        assert app_identity.get_service_account_name == environ.get_service_account_name

    def test_modules_functions(self):
        assert modules.get_current_instance_id == environ.get_current_instance_id
        assert modules.get_current_module_name == environ.get_current_module_name
        assert modules.get_current_version_name == environ.get_current_version_name
        assert modules.get_default_version == environ.get_default_version
        assert modules.get_hostname == environ.get_hostname
        assert modules.get_modules == environ.get_modules
        assert modules.get_versions == environ.get_versions

    def test_namespace_functions(self):
        assert namespace_manager.get_namespace == environ.get_namespace
        assert namespace_manager.google_apps_namespace == environ.google_apps_namespace


if __name__ == '__main__':
    unittest.main()
