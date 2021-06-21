## CRUD_OPERATIONS
<td>
This is a simple Python3.7 CRUD API project 'CRUD' which has one application 'CRUD_APP'. 
</td>

# INSTALLATON
install python v 3.7 and Django v 3.2.4
</br >

# Instructions and setup
Make Sure you have Python (3.7)  installed. 

* After you instal python and django, run python manage.py runsrver and navigate to the folder TestCases. 
* you can now run testcases of all the CRUD operations here by running 'pytest filename.py'
* Also, you can navigate to Application_testing folder and test each operations by providing your inputs. 
* can run each function of test cases by commenting others and open another terminal and run 'python test1.py'
* API document is provided under Application_testing folder.
</br >

# details explaination

* for example you have to insert a user (id,name,email). Navigate to CRUD_APP>Application_testing and you can comment other functions except create_new_User() in test1.py and run python test1.py.
* on the other hand  if you want to  delete a user id which is not present in DB. you can simply uncomment delete_unknown_User and pass an unknow id and check that will print User id not available in our system.
* You can also naviagate to TestCases under CRUD_APP application. I have used Pytest to check each testcases using assert keyword. Each operation has it's sepeate test case.


### Thank You!

**Connect with Me**
---
[<img align="left" alt="LinkedIn - Rohan Das" width="30px" src="https://www.flaticon.com/svg/static/icons/svg/733/733561.svg" />](https://www.linkedin.com/in/mudittripathi/) 
