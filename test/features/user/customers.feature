# Created by agras at 7/30/2022
Feature: Customers
  As a user i want to work with the customers API request

  Background:
    Given User logged into the system

  @customers
  Scenario: Getting customers without been authorized
    Given User is not login in the system
    When User attempts to get customers without being logged
    Then An error should be shown by the system

  @customers
  Scenario: Getting customers
    When User attempts to get customers
    Then System response with the customers

  @customers
  Scenario: Delete a customers
    Given User has a customers
    When User attempts to delete customers
    Then System response will delete the customers

  @customers
  Scenario: Get customers by its identification
    Given User has a customers
    When User attempts to get customers by its id
    Then System response with the customers

  @customers
  Scenario Outline: Get customers cars by its identification
    Given User has a customers
    When User attempts to get customers "<property>" by its id
    Then System response with the property selected "<property>"
    Examples:
      | property  |
      | cards     |
      | addresses |
