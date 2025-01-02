# Created by IanMckinney at 12/9/2024
Feature: Sign In functionality on Target.com

  Scenario: Verify a logged-out user can navigate to the Sign In page
    Given Open main page of target
    When Click Sign In button in the header
    And Click "Sign In" link from the right-side navigation menu
    Then See the Sign In form

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open sign in page
    When Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original
