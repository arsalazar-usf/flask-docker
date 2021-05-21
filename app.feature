Feature: Flask webpage
  A webserver that says hello and bye 

  Scenario: Ensure that bye works when given request data
    When the bye endpoint is hit with correct params
    Then the param is returned with bye prepended  
