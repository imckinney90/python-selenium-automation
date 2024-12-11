# Created by IanMckinney at 12/9/2024
Feature: Sign In functionality on Target.com

  Scenario: Verify a logged-out user can navigate to the Sign In page
    Given Open main paige of target
    When Click Sign In button in the header
    And Click "Sign In" link from the right-side navigation menu
    Then See the Sign In form