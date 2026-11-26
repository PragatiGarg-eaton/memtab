# SPDX-FileCopyrightText: 2026 Eaton Corporation
# SPDX-License-Identifier: MIT
"""Schema validation feature tests."""

import os
from functools import partial
from typing import Generator

from jsonschema import Draft7Validator
from pytest_bdd import given, parsers, then, when
from pytest_bdd import scenario as _scenario_base

from memtab.memtab import Memtab

####################
# boilerplate to shorten the scenario names
####################
feature_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../features")
scenario = partial(_scenario_base, os.path.join(feature_dir, "Schema Validation.feature"))

root_dir = os.path.dirname(os.path.abspath(__file__))


################################
# BDD Scenarios
################################
@scenario("Validate ELF section types in output schema")
def test_validate_elf_section_types_in_output_schema() -> None:
    """Validate ELF section types in output schema."""


################################
# BDD Given Statements
################################
@given("I have the memory tabulator package", target_fixture="memtab")
def given_memtab_package() -> Generator[Memtab, None, None]:
    """I have the memory tabulator package."""
    orig_dir = os.getcwd()
    os.chdir(root_dir)
    yield Memtab()
    os.chdir(orig_dir)


################################
# BDD When Statements
################################
@when("I inspect the elf_section type schema", target_fixture="elf_section_validator")
def when_i_inspect_the_elf_section_type_schema(memtab: Memtab) -> Generator[Draft7Validator, None, None]:
    """I inspect the elf_section type schema."""
    section_type_schema = memtab.schema["$defs"]["elf_section"]["properties"]["type"]
    yield Draft7Validator(section_type_schema)


################################
# BDD Then Statements
################################
@then(parsers.re(r'the schema should (?P<validity>accept|reject) the section type "(?P<section_type>.*)"'))
def then_the_schema_should_validate_the_section_type(elf_section_validator: Draft7Validator, validity: str, section_type: str) -> None:
    """The schema should accept or reject the section type."""
    is_valid = elf_section_validator.is_valid(section_type)
    if validity == "accept":
        assert is_valid, f"Expected schema to accept section type '{section_type}'"
    elif validity == "reject":
        assert not is_valid, f"Expected schema to reject section type '{section_type}'"
    else:
        raise ValueError(f"Unknown validity expected: {validity}")
