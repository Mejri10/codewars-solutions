# Is the string uppercase?

## Task

Create a method `is_uppercase()` to see whether the string is ALL CAPS.  For example:

```python
is_uppercase("c") == False
is_uppercase("C") == True
is_uppercase("hello I AM DONALD") == False
is_uppercase("HELLO I AM DONALD") == True
is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ") == False
is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ") == True
```
```elixir
upper_case?("c") == false
upper_case?("C") == true
upper_case?("hello I AM DONALD") == false
upper_case?("HELLO I AM DONALD") == true
upper_case?("ACSKLDFJSgSKLDFJSKLDFJ") == false
upper_case?("ACSKLDFJSGSKLDFJSKLDFJ") == true
```

## Corner Cases

For simplicity, you will not be tested on the ability to handle corner cases (e.g. ```"%*&#()%&^#"``` or similar strings containing alphabetical characters at all) - **an ALL CAPS (uppercase) string will simply be defined as one containing no lowercase letters**.  Therefore, according to this definition, strings with no alphabetical characters (like the one above) should ```return True```.