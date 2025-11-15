# Problem Statement:
# write aletter based on following code: 
"""
Dear <|Name|>,
You are selected!
<|Date|>"""
# Write your code here
letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''
print(letter.replace("<|Name|>","Ajay").replace("<|Date|>", "25 OCT 2025"))
# .replace fn can be chained inside.