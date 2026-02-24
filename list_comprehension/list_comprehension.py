"""
Comprehension Practice Examples
Author: Musa Acıbalık

This file contains practice examples for:
- List Comprehension
- Conditional Expressions
- Dictionary Comprehension
- Nested Comprehension
"""

# -------------------------------------------------
# 1️⃣ Basic List Comprehension
# Classic for-loop vs comprehension comparison
# -------------------------------------------------

# sayilar = []
# for i in range(5):
#     sayilar.append(i)
# print(sayilar)

sayilar = [i for i in range(5)]
print("Basic List:", sayilar)


# -------------------------------------------------
# 2️⃣ Filtering with List Comprehension
# Get even numbers from a list
# -------------------------------------------------

numbers = [1, 2, 3, 4, 5]
even_numbers = [i for i in numbers if i % 2 == 0]
print("Even Numbers:", even_numbers)


# -------------------------------------------------
# 3️⃣ If-Else Inside List Comprehension
# If even keep number, if odd make it negative
# -------------------------------------------------

modified_numbers = [i if i % 2 == 0 else -i for i in range(1, 7)]
print("Modified Numbers:", modified_numbers)


# -------------------------------------------------
# 4️⃣ Divisible by 12 Example
# Filtering numbers divisible by 12
# -------------------------------------------------

divisible_by_12 = [i for i in range(100) if i % 12 == 0]
print("Divisible by 12:", divisible_by_12)


# -------------------------------------------------
# 5️⃣ Extract Digits from String
# Using string methods inside comprehension
# -------------------------------------------------

text = "hello 12345 world"
digits = [char for char in text if char.isdigit()]
print("Digits:", digits)


# -------------------------------------------------
# 6️⃣ Conditional Text Example
# Temperature warning example
# -------------------------------------------------

temperatures = [20, 15, 0, -5, -2]
weather_status = [
    temp if temp >= 4 else "buzlanma tehlikesi"
    for temp in temperatures
]
print("Weather Status:", weather_status)


# -------------------------------------------------
# 7️⃣ Dictionary Comprehension
# Create dictionary from two lists
# Only include students with grade > 50
# -------------------------------------------------

students = ["ali", "ahmet", "canan"]
grades = [50, 60, 70]

student_dict = {
    students[i]: grades[i]
    for i in range(len(students))
    if grades[i] > 50
}
print("Student Dictionary:", student_dict)


# -------------------------------------------------
# 8️⃣ Square of Even Numbers (1–20)
# -------------------------------------------------

even_squares = [i**2 for i in range(1, 21) if i % 2 == 0]
print("Even Squares:", even_squares)


# -------------------------------------------------
# 9️⃣ Uppercase Words Starting with 'a'
# -------------------------------------------------

words = ["apple", "banana", "avocado", "cherry", "apricot"]
a_words_upper = [word.upper() for word in words if word.startswith("a")]
print("A Words Upper:", a_words_upper)


# -------------------------------------------------
# 🔟 Filter + Conditional Transformation
# If >10 → square if even, cube if odd
# -------------------------------------------------

nums = [5, 12, 7, 18, 3, 20]
processed_nums = [
    i**2 if i % 2 == 0 else i**3
    for i in nums
    if i > 10
]
print("Processed Numbers:", processed_nums)


# -------------------------------------------------
# 1️⃣1️⃣ Dictionary Comprehension with Length Filter
# -------------------------------------------------

words_small = ["apple", "banana", "cherry"]
length_dict = {
    word: len(word)
    for word in words_small
    if len(word) > 5
}
print("Length Dictionary:", length_dict)


# -------------------------------------------------
# 1️⃣2️⃣ Nested Dictionary Comprehension
# Group words by their first letter
# -------------------------------------------------

words_group = ["apple", "banana", "avocado", "cherry", "apricot"]

grouped_words = {
    letter: [word for word in words_group if word[0] == letter]
    for letter in set(word[0] for word in words_group)
}

print("Grouped Words:", grouped_words)