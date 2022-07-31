# Created by agras at 7/31/2022
Feature: # Enter feature name here
  As a user i want to work with the cards API requests

  Background:
    Given User logged into the system

#    GET
  @cards
  Scenario: Getting cards without been authorized
    Given User is not login in the system
    When User attempts to get cards without being logged
    Then An error should be shown by the system

  @cards
  Scenario: Getting cards
    When User attempts to get cards
    Then System response with the card


  @cards
  Scenario: Getting cards
    When User attempts to get cards by id
    Then System response with the list of cards

#POST
  @cards
  Scenario: Creating cards without been authorized
    Given User is not login in the system
    When User attempts to create a new cards without being logged
    Then An error should be shown by the system

  @cards
  Scenario: Creating cards without been authorized
    Given User is not login in the system
    When User attempts to create a new card
    Then System should create the new card


#    DELETE
  @cards @current_test
  Scenario: Getting cards
    Given User has a card
    When User attempts to delete a card by its id
    Then Card should not exists in the system



