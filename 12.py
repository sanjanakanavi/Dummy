# bitwise operators
'are used on bits or binary numbers'
'& -> and'
'| -> or'
'^ -> xor, if both bits are different then it gives 1 ,if same it gives 0'
'~ -> not or compliment, ~x=-(x+1)'
'<< -> left shift,x<<n= x*(2**n),  bits are not discarded ,it gains the bits'
'>> -> right shift,x>>n= x/(2**n),  bits are discarded ,it looses the bits'
a, b = 5, 4
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 2)
print(b >> 2)
