# Chapter 12 - Practice Questions

## Selenium

Another way without __geckodriver__:

See: https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path

`pip install webdriver-manager`

```
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
```

1. `webbrowser` opens a browser to a specific page. `requests` can download files and web pages. `bs4` helps in parsing HTML. `selenium` is helpful to control a web browser (fill forms and simulate mouse clicks).
2. `requests.model.Response`, a __Response__ object. To access the content as a string value use the `text` method on the Response object (`res.text`).
3. `res.raise_for_status`.
4. `status_code`.
5. Open a new file in __write binary__ mode `wb`: `myFile = open('file.txt', 'wb')`. Then loop over the Response object's `iter_content()` to write chinks to the file: `for chunk in res.iter_content(100000): myFile.write(chunk)`.
6. `F12` is used to open a browser's developer tools (Chrome). For Firefox use Ctrl+Shift+C.
7. Inspect element.
8. `'#main'`.
9. `'.highlight'`.
10. `'div1 div2'`.
11. `'button[value="favorite"]'`.
12. Using `getText()` method: `spam.getText()`.
13. `linkElem = mybs4TagObject.attrs`.
14. `from selenium import webdriver`.
15. `find_element_*` return a single WebElement object, the first matching query. `find_elements_*` return a list of WebElement_* objects for every matching element of the page.
16. `click()` and `send_keys()`.
17. Using the `submit()` method on any element within a form.
18. `browser.forward()`, `browser.back()` and `browser.refresh()`.