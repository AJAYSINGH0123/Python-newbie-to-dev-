# Escape Sequence characters: 
# Sequence of characters after backslash, "\" --> Escape sequence characters
# Escape sequence comprise of more than one character but represent one character when used in strings.
# Example: \n,\t, \', \\, etc.
# Note: Use chat gpt to know about functions in strings.

# To print double quote inside double quote, you need to use backslash, \"-----\"
a = "Hello \"World\""
print(a)
# Note: Search chatgpt for new escape sequence characters

# To print variables inside double quotes, use f string-->
name = "Ajay"
print("Good Afternoon", name)
print(f"goood afternooon {name}")
