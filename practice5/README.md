# Practice 5

## Topics

This practice is about:

- Reading files
- Working with text files
- Regular Expressions
- Searching patterns
- Extracting data from text

## Files

- `receipt_parser.py` - parses receipt information
- `raw.txt` - contains raw receipt data
- `RegEx/` - contains Regular Expression tasks

## Regular Expressions

Regular Expressions are used to find specific patterns in text.

Examples:

`\d+` - finds numbers

`\w+` - finds letters, numbers and underscore

`\d{2}` - finds exactly two digits

`\.` - finds a dot

`+` - one or more characters

`*` - zero or more characters

## Example

```python
import re

text = "My phone is +77001234567"

phone = re.findall(r"\+7\d{10}", text)

print(phone)