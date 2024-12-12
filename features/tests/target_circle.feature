# Created by IanMckinney at 12/10/2024
Feature: Verify there are at least 10 benefit cells on Target Circle page

  Scenario: Ensure there are at least 10 benefit cells on the Target Circle page
    Given Open target main page
    When Click Target Circle header button
    Then See at least 10 benefit cells displayed on the page
