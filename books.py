#books.py - List Manipulation Fundamentals

#This script demonstrates core Python list operations, including:
#Indexing and slicing (positive and negative indices)
#String formatting with .title()
#Modifying elements, appending, inserting, and deleting (del, pop, remove)
#Sorting operations: temporary (sorted()) vs. permanent (.sort()), and reversing (.reverse())


#Using list function to show my favourite books.
books = [ "Percy Jackson", "Harry Potter", "Hunger Games", "Divergent"]

print(books)

#Displaying every book i love on each line using the index on each of them.

print(books[0])
print(books[1])
print(books[2])
print(books[-1])

#Showing my ranking of my favourite books by adding a string and using title method to display the names of the books in proper format.

print("My most favourite book is", books[0].title())
print("My second most favourite book is", books[1].title())
print("My third most favourite book is", books[2].title())
print("My least favourite book is", books[3].title())

#Changing the last book from Divergent to Verity.
books[3] = "Verity"
print(books)

#Appending Divergent to the list using append method.

books.append('Divergent')
print(books)

#Converting the books list into an empty list.

books = []
print(books)

#Appending books to the empty books list using append method.

books.append('Divergent')
books.append('Percy Jackson')
books.append('Harry Potter')
books.append('Hunger Games')

print(books)

#Inserting another book into a list using insert method.

books.insert( 3, "The Bell Jar")
print(books)

#Deleting a book from the list using del function.

del books[3]
print(books)

#Removing the last book using pop function.

popped_books = books.pop()
print(books)
print(popped_books)

#Popping items from any position in a list by filling index in argument bracket of pop method.

first_read = books.pop(2)
print("The very first book I've ever read is ", first_read)

#Removing an item by value.

books.remove('Percy Jackson')
print(books)

#Appending books using the append method.

books.append('Percy Jackson')
books.append('Harry Potter')
books.append('Hunger Games')
books.append('The Bell Jar')

#Printing the original list.

print("Here is the original list ",books)

#Printing the original list reversed

books.reverse()
print("Here is the reversed list ",books)

#Printing the sorted list using the sorted function.

print("Here is the sorted list ",sorted(books))

#Printing the original list again to show sorted function can be used to show that sorting done through this function is temporary.

print("Here is the original list again ",books)

#Sorting the books in an ascending alphabetically manner using the sort function.

books.sort()
print(books)

#Sorting the books in an descending alphabetically manner using the sort function.

books.sort(reverse = True )
print(books)









