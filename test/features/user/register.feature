Feature:
  As a customer I want to test the register CRUD

  @register
  Scenario Outline: Validating schema parameters
    Given I am an invalid user profile "<field>"
    When I try to register in the system
    Then Registration will fail
    Examples:
      | field    |
      | username |
      | mail     |
      | password |

  @register
  Scenario: Register a new valid customer
    Given I am a valid user
    When I register in the system
    Then System will register my account


