#What happens when „1‟== 1 is executed

# When 1 == 1 is executed, Python checks if the integer 1 (on the left) is equal to the integer 1 (on the right). 
# The result will be True because both are of the same type and have the same value.

# However, if the expression is '1' == 1, the result will be False because:

# '1' is a string, and
# 1 is an integer. Python does not automatically convert between different types when checking for equality,
# so the comparison will return False.



print('1' == 1)  # Output: False