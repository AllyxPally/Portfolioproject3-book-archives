# Book Archives 

Book Archives is a Python based CLI app for managing books, which runs in the Code Institute mock terminal.
Users can use this app to add and look up books that are filed in the archive. 

https://book-archives-7f9fe26c25b2.herokuapp.com/

## How to use the app 

There are four choices to choose from, 1. Add a book


## Testing

I have tested this project manually by doing the following: 

* Given invalid inputs, any number above 4 will tell the user to enter a valid number.
* Tested the code in local terminal and the mock terminal provided by Code Institute.


### Bugs 

#### Solved bugs

* When i tested the code in the terminal, i noticed that something was wrong with the code, this was
due to a problem within the while loop. 

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`



