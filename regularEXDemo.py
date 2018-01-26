import re
text= '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa
MetaCharacters (need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
913-523-5225
913.777.6877

Mr. Vamshi
Mr Vk
Mrs Vaishali
Ms Preethi
Mr. T
cat
mat
bat
pat

# vamshinunna2607@gmail.com
# vaishali.jula@gmail.net
# www.pip-installer@yahoo.org
https://www.google.com
http://coreyms.com
https://www.youtube.com
https://www.nasa.gov

'''
Sentence = 'Start a sentence and then bring it to an end'
pattern =re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches=pattern.finditer(text)

# subUrls = pattern.sub(r'\2\3',text)
# print(subUrls)

for match in matches:
    print (match.group(3))

