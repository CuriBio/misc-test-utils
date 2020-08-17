# -*- coding: utf-8 -*-
import uuid

import domain_model
from domain_model import DomainModel
from domain_model import DomainModelWithUuid
from misc_test_utils import copy_dict_with_key_removed
from misc_test_utils import domain_model_validate_internals_test
from misc_test_utils import domain_model_validation_test
from misc_test_utils import misc_test_utils
import pytest


def test_copy_dict_with_key_removed__creates_copy_of_dict():
    test_dict = {"key1": 1, "key2": 2}
    actual = copy_dict_with_key_removed(test_dict)
    assert actual == test_dict
    assert actual is not test_dict


def test_copy_dict_with_key_removed__removes_key_if_specified():
    test_dict = {"key1": 1, "key2": 2}
    actual = copy_dict_with_key_removed(test_dict, key_to_remove="key2")
    assert actual == {"key1": 1}


def test_domain_model_validation_test__creates_DomainModel_object(mocker):
    mocked_init = mocker.patch.object(
        domain_model.DomainModel, "__init__", autospec=True, return_value=None
    )
    domain_model_validation_test(DomainModel)
    mocked_init.assert_called_once()


def test_domain_model_validation_test__calls_validate_with_no_expected_error(mocker):
    mocked_validate = mocker.patch.object(
        domain_model.DomainModelWithUuid, "validate", autospec=True
    )
    test_uuid = uuid.UUID("abc8a386-b6e0-47ed-a752-f2721545f3c6")
    domain_model_validation_test(DomainModelWithUuid, "uuid", test_uuid)
    mocked_validate.assert_called_once()


def test_domain_model_validation_test__calls_validate_with_no_expected_error__and_uuid_passed_as_additional_kwarg(
    mocker,
):
    mocked_validate = mocker.patch.object(
        domain_model.DomainModelWithUuid, "validate", autospec=True
    )
    test_uuid = uuid.UUID("abc8a386-b6e0-47ed-a752-f2721545f3c6")
    domain_model_validation_test(
        DomainModelWithUuid, additional_kwargs={"uuid": test_uuid}
    )
    mocked_validate.assert_called_once()


def test_domain_model_validation_test__catches_error(mocker):
    spied_raises = mocker.spy(misc_test_utils.pytest, "raises")
    expected_error = ValueError()
    mocker.patch.object(
        domain_model.DomainModelWithUuid,
        "validate",
        autospec=True,
        side_effect=expected_error,
    )
    test_uuid = uuid.UUID("abc8a386-b6e0-47ed-a752-f2721545f3c6")
    domain_model_validation_test(
        DomainModelWithUuid, "uuid", test_uuid, expected_error=ValueError
    )
    spied_raises.assert_called_once()


def test_domain_model_validation_test__catches_error_with_text(mocker):
    spied_raises = mocker.spy(misc_test_utils.pytest, "raises")
    expected_text = "test"
    expected_error = ValueError(expected_text)
    mocker.patch.object(
        domain_model.DomainModelWithUuid,
        "validate",
        autospec=True,
        side_effect=expected_error,
    )
    test_uuid = uuid.UUID("abc8a386-b6e0-47ed-a752-f2721545f3c6")
    domain_model_validation_test(
        DomainModelWithUuid,
        "uuid",
        test_uuid,
        expected_error=ValueError,
        expected_texts_in_error=expected_text,
    )
    spied_raises.assert_called_once()


def test_domain_model_validation_test__raises_assertion_error_if_single_expected_text_is_not_in_expected_error(
    mocker,
):
    expected_text = "test"
    expected_error = ValueError()
    mocker.patch.object(
        domain_model.DomainModelWithUuid,
        "validate",
        autospec=True,
        side_effect=expected_error,
    )
    test_uuid = uuid.UUID("abc8a386-b6e0-47ed-a752-f2721545f3c6")
    with pytest.raises(AssertionError):
        domain_model_validation_test(
            DomainModelWithUuid,
            "uuid",
            test_uuid,
            expected_error=ValueError,
            expected_texts_in_error=expected_text,
        )


def test_domain_model_validation_test__raises_assertion_error_if_one_of_multiple_expected_texts_not_in_expected_error(
    mocker,
):
    expected_texts = ["test1", "test2"]
    expected_error = ValueError("test1")
    mocker.patch.object(
        domain_model.DomainModelWithUuid,
        "validate",
        autospec=True,
        side_effect=expected_error,
    )
    test_uuid = uuid.UUID("abc8a386-b6e0-47ed-a752-f2721545f3c6")
    with pytest.raises(AssertionError):
        domain_model_validation_test(
            DomainModelWithUuid,
            "uuid",
            test_uuid,
            expected_error=ValueError,
            expected_texts_in_error=expected_texts,
        )


def test_domain_model_validate_internals_test__creates_DomainModel_object(mocker):
    mocked_init = mocker.patch.object(
        domain_model.DomainModel, "__init__", autospec=True, return_value=None
    )
    domain_model_validate_internals_test(DomainModel)
    mocked_init.assert_called_once()


def test_domain_model_validate_internals_test__calls_validate_with_no_expected_error(
    mocker,
):
    mocked_validate = mocker.patch.object(
        domain_model.DomainModelWithUuid, "validate_internals", autospec=True
    )
    test_uuid = uuid.UUID("abc8a386-b6e0-47ed-a752-f2721545f3c6")
    domain_model_validate_internals_test(DomainModelWithUuid, "uuid", test_uuid)
    mocked_validate.assert_called_once()


def test_domain_model_validate_internals_test__calls_validate_with_no_expected_error__and_uuid_passed_as_additional_kwarg(
    mocker,
):
    mocked_validate = mocker.patch.object(
        domain_model.DomainModelWithUuid, "validate_internals", autospec=True
    )
    test_uuid = uuid.UUID("abc8a386-b6e0-47ed-a752-f2721545f3c6")
    domain_model_validate_internals_test(
        DomainModelWithUuid, additional_kwargs={"uuid": test_uuid}
    )
    mocked_validate.assert_called_once()


def test_domain_model_validate_internals_test__catches_error(mocker):
    spied_raises = mocker.spy(misc_test_utils.pytest, "raises")
    expected_error = ValueError()
    mocker.patch.object(
        domain_model.DomainModelWithUuid,
        "validate_internals",
        autospec=True,
        side_effect=expected_error,
    )
    test_uuid = uuid.UUID("abc8a386-b6e0-47ed-a752-f2721545f3c6")
    domain_model_validate_internals_test(
        DomainModelWithUuid, "uuid", test_uuid, expected_error=ValueError
    )
    spied_raises.assert_called_once()


def test_domain_model_validate_internals_test__catches_error_with_text(mocker):
    spied_raises = mocker.spy(misc_test_utils.pytest, "raises")
    expected_text = "test"
    expected_error = ValueError(expected_text)
    mocker.patch.object(
        domain_model.DomainModelWithUuid,
        "validate_internals",
        autospec=True,
        side_effect=expected_error,
    )
    test_uuid = uuid.UUID("abc8a386-b6e0-47ed-a752-f2721545f3c6")
    domain_model_validate_internals_test(
        DomainModelWithUuid,
        "uuid",
        test_uuid,
        expected_error=ValueError,
        expected_texts_in_error=expected_text,
    )
    spied_raises.assert_called_once()


def test_domain_model_validate_internals_test__raises_assertion_error_if_single_expected_text_is_not_in_expected_error(
    mocker,
):
    expected_text = "test"
    expected_error = ValueError()
    mocker.patch.object(
        domain_model.DomainModelWithUuid,
        "validate_internals",
        autospec=True,
        side_effect=expected_error,
    )
    test_uuid = uuid.UUID("abc8a386-b6e0-47ed-a752-f2721545f3c6")
    with pytest.raises(AssertionError):
        domain_model_validate_internals_test(
            DomainModelWithUuid,
            "uuid",
            test_uuid,
            expected_error=ValueError,
            expected_texts_in_error=expected_text,
        )


def test_domain_model_validate_internals_test__raises_assertion_error_if_one_of_multiple_expected_texts_not_in_expected_error(
    mocker,
):
    expected_texts = ["test1", "test2"]
    expected_error = ValueError("test1")
    mocker.patch.object(
        domain_model.DomainModelWithUuid,
        "validate_internals",
        autospec=True,
        side_effect=expected_error,
    )
    test_uuid = uuid.UUID("abc8a386-b6e0-47ed-a752-f2721545f3c6")
    with pytest.raises(AssertionError):
        domain_model_validate_internals_test(
            DomainModelWithUuid,
            "uuid",
            test_uuid,
            expected_error=ValueError,
            expected_texts_in_error=expected_texts,
        )
