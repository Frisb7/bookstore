# bookstore
It is Web app for a bookstore (for a school setting). It uses Python and the Django framwork for the backend. For the front end it uses HTML5 and Bootstrap framework, also a bit of CSS.

## To open the webiste on any device on your network

add your server ip to Bookstore/settings.py in ALLOWED_HOSTS and sun server using this comand

python manage.py runserver 0.0.0.0:8000


## There are 4 example users
1. SUPER:  
  email: su@su.com  
  password: 1357531su  
  it can open all the pages
2. Admin  
  email: p@p.com  
  password: 1357531p  
  it can open all the pages  
3. Staff  
  email: t@t.com  
  password: 1357531t  
  it cant open admin page  
  it cant add or delete books but can update  
4. Customer  
  email: s@s.com  
  password: 1357531s  
  it can only open store, cart and receipt page  

User can be registered by going to /register/
