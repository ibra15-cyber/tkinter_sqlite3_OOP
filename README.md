# tkinter_sqlite3_OOP

same as the previous on euses procedural approach

here we created a class for our backend
imported it in the frontend
then created an object of the class 
which was used to replace backend

then we made the connect to initiliaze during creation as a constructor
we made conn and cur as property of our class at creation
which means they will be available for other part of the code in the class
instead of repeating ourself, we assume the fn are aware of them, we only call them using self

we also closed the connection using a diff fn
hence deleting all the close in the various internal fns so as not to stop operation after the first try

same with commit
