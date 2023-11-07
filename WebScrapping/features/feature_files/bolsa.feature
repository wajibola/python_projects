Feature: Accessing Bolsa Website
  Scenario: Getting bolsa information stickers
  Given that the user access bolsa.es
  And the following fields are displayed:
      | Field Name            |
      | Ticker                |
      | Nombre                |
      | Última transacción    |
      | Variación             |
      | Volumen               |
  Then get fields values
