# -*- coding: utf-8 -*-
from misc_test_utils import fixture_session_dns_resource_prefix
from misc_test_utils import fixture_session_resource_prefix
from misc_test_utils import get_vault
from misc_test_utils import set_vault
from misc_test_utils import vault
from misc_test_utils import VaultNotSetError
from misc_test_utils import VaultSetToProductionTierError
import pytest
from secrets_manager import Vault

from .fixtures import fixture_aa_set_testing_vault

__fixtures__ = [
    fixture_session_resource_prefix,
    fixture_session_dns_resource_prefix,
    fixture_aa_set_testing_vault,
]


def test_get_vault__raises_error_if_vault_not_set():
    vault._vault_namespace.vault = None  # pylint: disable=protected-access
    with pytest.raises(VaultNotSetError):
        get_vault()


def test_set_vault__raises_error_if_vault_in_production_mode():
    v = Vault(deployment_tier="production")
    with pytest.raises(VaultSetToProductionTierError):
        set_vault(v)


def test_session_resource_prefix__creates_the_string(
    aa_set_testing_vault, session_resource_prefix
):
    assert isinstance(session_resource_prefix, str)
    assert "zztest" in session_resource_prefix
    # clean up
    vault._vault_namespace.vault = None  # pylint: disable=protected-access


def test_session_dns_resource_prefix__replaces_underscores_with_hyphens(
    aa_set_testing_vault, session_dns_resource_prefix
):
    assert "_" not in session_dns_resource_prefix
    assert session_dns_resource_prefix[0] != "-"
