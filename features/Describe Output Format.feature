Feature: Provide a file describing the output data format
    As a developer
    I want to be able to see the schema of the output data format
    So that I can make engineering decisions about the footprint of different libraries, methods, etc.
    The output should be in JSON format, to be parsable downstream by other tools.

    Scenario: Provide a file describing the output data format
        Given I have the memory tabulator package
        When I run the schema command
        Then I should be provided the schema file

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
