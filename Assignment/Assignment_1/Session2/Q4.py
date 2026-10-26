"""4.Given the following variables for a YouTube video — title, views, likes, is_premium
 — identify which are primitive and which are non-primitive data types, and explain 
 your reasoning in comments."""

# Sample values representing a YouTube video
title = "Python Tutorial for Beginners"  # Primitive (String / str)
views = 150000                           # Primitive (Integer / int)
likes = 12500                            # Primitive (Integer / int)
is_premium = False                       # Primitive (Boolean / bool)

# --- REASONING ---
# 1. Primitive vs. Non-Primitive in Python:
#    - Python treats built-in scalar types (like strings, integers, floats, and booleans) 
#      as primitive or basic types because they hold a single, indivisible value.
#    - Non-primitive types (such as lists, dictionaries, sets, and tuples) are collections 
#      that can store multiple values or complex data structures.
#
# 2. Classification of the given variables:
#    - title (str), views (int), likes (int), and is_premium (bool) are ALL **primitive** 
#      data types because each variable stores a single fundamental piece of data. 
#    - There are no non-primitive (collection/container) data types present in this set.