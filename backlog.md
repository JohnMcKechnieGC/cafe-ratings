# Project Backlog

## Input Validation
- [ ] Add checks for user inputs, especially for the rating, to ensure it's within the
      expected range (1-5).


## Maintainability
- [ ] Documentation: Add docstrings to classes and methods to improve maintainability.
- [ ] Testing: Adding unit tests and integration tests for each component to build
      confidence that they work as expected independently and when integrated.


## UI Enhancements
- [ ] Feedback Display: When displaying all feedback, format the output for better
      readability rather than printing the raw data structure.


## Done
- [ ] Error Handling: Improve error handling by adding more specific exceptions,
      especially in database interactions, and provide user-friendly error
      messages. This will also improve security as we don't want raw error strings
      in the UI. At the moment, the SQLite DB class writes error messages to the
      console. This is inconsistent with the MySQL DB class.
      Created custom database connection exception which the MySQL and SQLite
      classes both now raise.
- [ ] Logging: Instead of just printing errors, implement a logging system to log
      errors and important system events. This will preserve the raw error messages
      for diagnostic purposes while avoiding exposing them to the (potentially
      malicious) user.
- [ ] Configurable Settings: Move configuration settings to environment variables
      to ensure that files with db credentials are not accidentally shared.
