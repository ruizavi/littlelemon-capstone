Hi!

------ Admin Credentials
user: admin
password: lemon@123!

------- Extra user for test
user: test
password: lemon@123!

------- Static routes
/restaurant/
/restaurant/about/
/restaurant/reservations/

------- Api routes
/restaurant/menu/ (all user allow GET method)
/restaurant/menu/<int:pk> (all user allow GET method)

/restaurant/booking/tables/ (only authenticated user)
/restaurant/booking/tables/<int:pk> (only authenticated user)

/auth/users/ (all user for register)
/auth/token/login (all user for get token)
/api-token-auth (obtain auth token)