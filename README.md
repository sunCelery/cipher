<h1>cipher</h1>

<h2>Table of content</h2>

- [Description](#description)
- [Install](#install)
- [Usage](#usage)
- [To Do](#to-do)

## Description ## \
Library that contains cipher algorithms for any language.

You only need to specify language see Usage(#usage) section

For now:
- only viginere algorithm implemented
- only EN, RU implemented
- You could add any language support with one line, but need tests, see [Usage](#adding-Turkish-language)

## Install ##
**To install the Library just clone it, it needs no additional dependencies**

- if poetry:
```
git clone https://github.com/sunCelery/cipher.git
```

## Usage ##
**Python Interactive Mode examples:**

**adding Turkish language**
```
>>> from cipher import *
>>> Alphabet.add_alphabet("TR", "abcçdefgğhıijklmnoöprsştuüvyz")
```

**encrypt / decrypt**
```
>>> encrypt(viginere, "örnek", "doldurmak", "TR")
'şğbhğ'
>>> decrypt(viginere, 'şğbhğ', "doldurmak", "TR")
'örnek'
```

## To Do ##

- I don't like how decrypt and encrypt funcrion written,
I think it's bad practice to give function to them as an argument, mb I wrong?
- Add other algorithms
