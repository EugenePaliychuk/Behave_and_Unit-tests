Feature: Fibonacci Sequence Testing_1

  Scenario Outline: Verify that we generate proper values for valid indexes
    Given I have input value "<input>" as index
    When I generate fibonacci value for selected index
    Then I should get "<result>"
  Examples:
    | input | result |
    | 1     | 1      |
    | 15    | 610    |
    | 0     | 0      |

    

  Scenario: Verify that exception is raised for invalid indexes
    Given I have input value "-1" as index
    When User wants to generate fibonacci value for selected index
    Then User should get appropriate exception


