# Created by IanMckinney at 12/9/2024
Feature: Tests for cart functionality for target.com

  Scenario: For an empty cart 'Your cart is empty' message is shown
    Given Open target main page
    When Click on Cart icon
    Then Verify message of "Your cart is empty" is shown

  Scenario: Add a product to the cart and verify it
    Given Open target main page
    When Add to cart Coca-Cola
    And Add Coca-Cola to the cart in the right-side menu
    Then Should see the product in my cart

