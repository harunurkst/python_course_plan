# Class 01
## use python as a calculator
```python
>>> 2 + 3  # all basic operation, + - * /
>>> 17 // 3  # floor division discards the fractional part
>>> 17 % 3  # the % operator returns the remainder of the division
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128
>>> 10 + _  # last executed value with _
25

```
## comparison
```python
>>> 10 > 5
True
>>> 3 <1
False
>>> 5 = 5
  File "<stdin>", line 1
SyntaxError: cannot assign to literal
>>> 5 == 5
True
>>> 2 == 2 and 5 == 5
True
>>> 2 == 2 or 5 ==3
True

# != , >=, <=
```
## String
```python
>>> "my name is Harun"
'my name is Harun'
>>> "a" + "b"
'ab'
>>> "a" *3
'aaa'
>>> "He's a man"
"He's a man"
>>> "First line\n Second line"
'First line\n Second line'
>>> print("Fist line \n Second line")
Fist line 
 Second line
```
## Variable
### কিভাবে ভ্যারিয়েবল কাজ করে
```python
>>> width  = 5
>>> hight = 10
>>> area = width * hight
>>> area
50
>>> b = "bangladesh"
>>> "b" in b
True
```
## Reserve Keyword
```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass','raise', 'return', 'try', 'while', 'with', 'yield']
```
## String Indexing
```python
>>> "bangladesh"[0]
'b'
>>> "bangladesh"[-1]
'h'
>>> "bangladesh"[:]
'bangladesh'
>>> "bangladesh"[:6]
'bangla'
>>> "bangladesh"[5:]
'adesh'
>>> "bangladesh"[6:]
'desh'
```
** also show indexing with variable
## TypeCasting
```python
>>> type(2)
<class 'int'>
>>> type("2")
<class 'str'>
>>> int("2")
2
>>> str(2)
'2'
```
## Operator
** Different type of operator
1. Arithmetic operator  
2. Comparison operator  
3. Assignment operator  
4. Logical operators (and, or, not)  
5. Membership operators (in, not in)  
6. Identity operator (is, not is)  
```python
>>> a = 1, 
>>> b = 1
>>> a is b
True
>>> a = 276
>>> b = 275
>>> a is b 
False
```
