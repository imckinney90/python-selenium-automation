# Created by IanMckinney at 12/10/24
Feature: Tests for search

  Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify search results shown for tea

  Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify search results shown for coffee

  Scenario: User can search for a mug
    Given Open target main page
    When Search for soccer ball
    Then Verify search results shown for soccer ball

  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search results shown for <product>
    Examples:
    |product    |
    |coffee     |
    |tea        |
    |soccer ball|