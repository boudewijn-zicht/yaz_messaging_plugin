# 1.0.0
- Adds cleanup and check tasks

# 1.0.1
- Adds fix task
- Adds yaz-messaging script to user bin directory

# 1.0.2
- Using yaz.Error for feedback without call stack
- Allow --verbose in cleanup, check, and fix tasks

# 1.0.3
- No parsing for types: bool, float, int, null, and timestamp.  This
  results in parsing which is much more compatible with how Symfony
  handles it's translations

# 1.0.4
- Fixes bug where an empty translation file would give an assertion

# 1.0.5
- Allow unicode in resulting yaml files

# 1.1.0
- Use the `googletrans` library to translate missing values during sync

# 1.1.1
- Fix unit tests
- Fix bug when trying to google translate an empty string
- Add support for `!foo` placeholders using google translate
- Show the diff when a change is detected (allowing someone to manually fix it)

# 1.1.2
- Will now also look in `"src/Resources/translations/"` for potential
  translation files