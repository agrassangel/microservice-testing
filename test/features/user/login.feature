# Created by agras at 7/30/2022
Feature: # Enter feature name here
  # Enter feature description here
  @login
  Scenario: Validating successful user authorization
    Given User has a credentials
    When User requires access to the system
    Then System will authorize the user

  @login
  Scenario Outline: Invalid user authorization
    Given User has a credentials
    When User requires access to the system with the invalid field "<field>"
    Then System wont authorize the user
    Examples:
      | field    |
      | username |
      | password |
      | all      |