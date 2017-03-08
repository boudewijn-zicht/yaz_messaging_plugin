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
