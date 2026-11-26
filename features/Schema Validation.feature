Feature: Schema Validation
    As a developer
    I want to validate section types against the memtab JSON output schema
    So that binaries from various architectures produce schema-compliant output format.

    Scenario Outline: Validate ELF section types in output schema
        Given I have the memory tabulator package
        When I inspect the elf_section type schema
        Then the schema should <validity> the section type "<section_type>"

        Examples:
            | section_type     | validity |
            | PROGBITS         | accept   |
            | NOBITS           | accept   |
            | ARM_EXIDX        | accept   |
            | ARM_ATTRIBUTES   | accept   |
            | RISCV_ATTRIBUTES | accept   |
            | XTENSA_INFO      | accept   |
            | progbits         | reject   |
            | UNKNOWN_TYPE     | reject   |
            |                  | reject   |
