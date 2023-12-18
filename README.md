<h1>1.Python practice programs:</h1>
<p>1. Create a table with a large number of records (you can find it with a google search or use this
link - https://github.com/datacharmer/test_db). Use MySQL Database. One can setup MySQL on
localhost. Write some basic queries using python. Suppose you want to process/fetch a large
number of records using python while keeping your memory usage low. Think of approaches on
how to accomplish this and implement it.
<br>Hint: Use Generator</p>
<p>2. Define a class Person and its two child classes: Male and Female. All classes have
a method "get_gender" which can print "Male" for Male class and "Female" for Female
Class.
<br>Bonus: Make class Person an abstract class and make get_gender an abstract method in the
same class. The two child classes must inherit and implement get_gender. i.e., When trying to
initialize an object of class Person, the program must throw an error.
Hint:
Use ABC library (comes natively with Python3
</p>
<p>3. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this
list after removing all duplicate values with original order reserved.
Hint: Use set() to store a number of values without duplicates.</p>

<p>4. Write a program that can map() to make a list whose elements are squares of numbers
between 1 and 20 (both included).
<br>Hints:
Use map() to generate a list.
Use Lambda to define anonymous functions.</p>

<p>5. Write a program anti_html.py that takes a URL as an argument, downloads the HTML from
the web, and prints it after stripping HTML tags.</p>

<h1>Flask API:</h1>
<p>a. Create a Rest API in python using flask which supports the following operations on the
Northwind dataset –
  <ol>
        <li>Insert, update and select on customers</li>
        <li>Insert, update and select on orders</li>
        <li>Insert, update and select on products</li>
        <li>Order history of the given customer</li>
  </ol>
</p>
<p>
  b. Use any popular IDE for development and integrate it with git for version control c.
Follow industry standards while writing the code and include basic schema and data
validations and also use MVC model (with appropriate folder structure) and ORM d.
Write unit test cases mocking all external service calls
</p>

