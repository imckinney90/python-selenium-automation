# Created by IanMckinney2 at 12/14/2024
Feature: Feature: Product Page Functionality

  Scenario: Check that a product has multiple color variations
    Given Open product page
    When  Product has multiple color options
    Then  Verify that color has been selected
