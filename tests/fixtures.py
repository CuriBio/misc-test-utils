# -*- coding: utf-8 -*-
from misc_test_utils import set_vault
from misc_test_utils import vault
import pytest
from secrets_manager import Vault


@pytest.fixture(scope="session", name="aa_set_testing_vault")
def fixture_aa_set_testing_vault():
    # needs the 'aa' prefix to make sure it executes first
    v = Vault()
    set_vault(v)
    yield v

    # clean up
    # Note: the test using this fixture should also clean itself up. This has to be session-scoped because session_resource_prefix is session scoped...but the cleanup should occur at the function level
    vault._vault_namespace.vault = None  # pylint: disable=protected-access
