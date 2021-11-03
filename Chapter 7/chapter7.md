# Chapter 7 - Practice Questions

1. `regex.compile()`.
2. Raw strings are used so that backslashes don't need to be escaped.
3. `search()` method returns a *match object*.
4. Using the `group()` method.
5. From `r'(\d\d\d)-(\d\d\d-\d\d\d\d)'`, group 0 covers the whole match (for example 123-456-7890). Group 1 covers the first parentheses (123), while group 2 covers the second parentheses (456-7890).
6. You need to escape them with a backslash `\` (`\(` and `\.`).
7. If the regex has no groups, `findall()` returns a list of strings. If there are groups, it returns a list of tuples of strings.
8. The pipe `|` means logical *or* (one or the other).
9. The question mark `?` can be used to match 0 or 1 of the preceding group or declaring a non-greedy match.
10. `+` means 1 or more, while `*` means 0 or more of the preceding group.
11. `{3}` means exactly 3, while `{3,5}` means between 3 and 5 of the preceding group.
12. `\d`, `\w` and `\s` match a digit, word or space character, respectively.
13. `\D`, `\W` and `\S` match anything except a digit, word or space character, respectively.
14. `.*` matches anything, while `.*?` matches anything in a *non-greedy* fashion.
15. `[0-9a-z]` or `[a-z0-9]`.
16. By using `re.I` or `re.IGNORECASE` as the second argument of the `re.compile` method.
17. The `.` (wildcard character) matches any character except for a newline. Using `re.DOTALL` includes matching newlines as well.
18. X drummers, X pipers, five rings, X hens.
19. Ignoring whitespace and comments inside the regular expression string.
20. `re.compile(r'^\d{1,3}(,\d{3})*$')`.
21. `re.compile(r'[A-Z][a-zA-Z]*\sWatanabe')`.
22. `re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)`