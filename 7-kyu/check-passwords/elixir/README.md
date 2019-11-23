We want to be able to check hashed passwords.

We are using hex digest of sha256 hashed passwords.

Write a method `check(password, hashed_password)` that compares a password with a previously hashed password and returns `true`, `false`.

**Notes:**

- This is not how you should actually store or verify passwords
- Don't actually use this for real passwords. Use *a key derivation function* instead.