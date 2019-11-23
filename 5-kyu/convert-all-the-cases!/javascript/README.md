In this kata, you will make a function that converts between `camelCase`, `snake_case`, and `kebab-case`.

You must write a function that changes to a given case. It must be able to handle all three case types:

```javascript
js> changeCase("snakeCase", "snake")
"snake_case"
js> changeCase("some-lisp-name", "camel")
"someLispName"
js> changeCase("map_to_all", "kebab")
"map-to-all"
js> changeCase("doHTMLRequest", "kebab")
"do-h-t-m-l-request"
js> changeCase("invalid-inPut_bad", "kebab")
undefined
js> changeCase("valid-input", "huh???")
undefined
js> changeCase("", "camel")
""
```
```python
py> change_case("snakeCase", "snake")
"snake_case"
py> change_case("some-lisp-name", "camel")
"someLispName"
py> change_case("map_to_all", "kebab")
"map-to-all"
py> change_case("doHTMLRequest", "kebab")
"do-h-t-m-l-request"
py> change_case("invalid-inPut_bad", "kebab")
None
py> change_case("valid-input", "huh???")
None
py> change_case("", "camel")
""
```
```haskell
λ> changeCase "snakeCase" "snake"
Just "snake_case"
λ> changeCase "some-lisp-name" "camel"
Just "someLispName"
λ> changeCase "map_to_all" "kebab"
Just "map-to-all"
λ> changeCase "doHTMLRequest" "kebab"
Just "do-h-t-m-l-request"
λ> changeCase "invalid-inPut_bad" "kebab"
Nothing
λ> changeCase "valid-input" "huh???"
Nothing
λ> changeCase "" "camel"
Just ""
```
```c
c> changeCase("snakeCase", "snake")
"snake_case"
c> changeCase("some-lisp-name", "camel")
"someLispName"
c> changeCase("map_to_all", "kebab")
"map-to-all"
c> changeCase("doHTMLRequest", "kebab")
"do-h-t-m-l-request"
c> changeCase("invalid-inPut_bad", "kebab")
NULL
c> changeCase("valid-input", "huh???")
NULL
c> changeCase("", "camel")
""

Non-null returns will be free'd.
```
```cpp
cpp> changeCase("snakeCase", "snake")
"snake_case"
cpp> changeCase("some-lisp-name", "camel")
"someLispName"
cpp> changeCase("map_to_all", "kebab")
"map-to-all"
cpp> changeCase("doHTMLRequest", "kebab")
"do-h-t-m-l-request"
cpp> changeCase("invalid-inPut_bad", "kebab")
""
cpp> changeCase("valid-input", "huh???")
""
cpp> changeCase("", "camel")
""
```
```java
java> changeCase("snakeCase", "snake")
"snake_case"
java> changeCase("some-lisp-name", "camel")
"someLispName"
java> changeCase("map_to_all", "kebab")
"map-to-all"
java> changeCase("doHTMLRequest", "kebab")
"do-h-t-m-l-request"
java> changeCase("invalid-inPut_bad", "kebab")
null
java> changeCase("valid-input", "huh???")
null
java> changeCase("", "camel")
""
```

Your function must deal with invalid input as shown, though it will only be passed strings. Furthermore, all valid identifiers will be lowercase except when necessary, in other words on word boundaries in `camelCase`.

_**(Any translations would be greatly appreciated!)**_