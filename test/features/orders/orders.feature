# Created by agras at 7/31/2022
Feature: Orders
  As a user i wan to work with the customers API request

  Background:
    Given User logged into the system

  @orders
  Scenario: Getting orders without been authorized
    Given User is not login in the system
    When User attempts to get orders without being logged
    Then An error should be shown by the system


  @orders
  Scenario: Getting orders
    When User attempts to get orders
    Then System will display all orders

##  There is not schema to map a new order creation
#  @orders @current_test
#  Scenario: Creating a new orders
#    Given User has a new order
#    When User attempts to create a orders
#    Then System will display save teh order