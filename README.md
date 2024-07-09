# Book Archives 

Book Archives is a Python based CLI app for managing books, which runs in the Code Institute mock terminal.
Users can use this app to add and look up books that are filed in the archive. 

Here is the live version (https://book-archives-7f9fe26c25b2.herokuapp.com/)

## How to use the app 

There are four choices to choose from: 

* Add a new book 
* Find a book
* Display all books 
* Exit the program

If the user chooses any other number they will get a validation message telling them to enter
a valid number. 


## Testing

I have tested this project manually by doing the following: 

* Given invalid inputs, any number above 4 will tell the user to enter a valid number.
* Tested the code in local terminal and the mock terminal provided by Code Institute.


### Bugs 

#### Solved bugs

* When i tested the code in the terminal, i noticed that something was wrong with the code, this was
due to a problem within the while loop.

## Deployment

This project was deployed using Code Instutute's mock terminal for Heroku.

* Steps for deployment 
  - Create a new Heroku app
  - Set the buildpacks to Python and NodeJS, it has to be that order
  - Link the Heroku app to the repository
  - Click on Deploy



## Credits

* Code Institute for the terminal used for deployment.





