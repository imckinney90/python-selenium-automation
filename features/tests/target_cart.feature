# Created by IanMckinney at 12/9/2024
Feature: Tests for cart functionality for target.com

  Scenario: For an empty cart 'Your cart is empty' message is shown
    Given Open target main page
    When Click on Cart icon
    Then Verify message of "Your cart is empty" is shown
