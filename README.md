# SecurityByDesign-csv-file-permissions-and-rules

This program is able to read and write to the .csv file, as well to support multiple levels of user access (Guest, User, Superuser, and Administrator).
All of the user types need to enter their credentials (such as username and password), but all of them have different permissions and levels of access. 

Administrator account cannot view user information, or create user accounts. However, the Administrator can view only the information of the Superuser accounts, as well as create Superuser accounts.

Superuser can create new users, add and view data in their accounts. They can also view information on their own account, but not other Superusers and they cannot create Superuser accounts. 

Guest and User types can only see their own personal data and cannot create any type of accounts or see data from the other user types.

