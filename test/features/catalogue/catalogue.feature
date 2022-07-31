Feature: Catalogue
  As a user i wan to work with the customers API request

  Background:
    Given User logged into the system

  @catalogue
  Scenario: Getting all catalogues in the system
    When User attempts to get whole catalogues list
    Then System response with the catalogues

  @catalogue
  Scenario: Getting catalogue by id
    Given User has a catalogue
    When User attempts to get catalogues by its id
    Then System response with the catalogue selected

  @catalogue
  Scenario: Getting total of catalogue
    When User attempts to get total of catalogue
    Then System response with the total of catalogue available

  @catalogue
  Scenario: Getting catalogue tags
    When User attempts to get all tags
    Then System returns all tags available