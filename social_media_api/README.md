User Authentication
This API uses token-based authentication to manage user authentication securely.

Endpoints:
User Registration:

URL: /accounts/register/

Method: POST

Request Data: username, email, password

Response: Returns a token upon successful registration.

User Login:

URL: /accounts/login/

Method: POST

Request Data: username, password

Response: Returns a token upon successful authentication.

User Profile Management:

URL: /accounts/profile/

Method: GET (requires authentication)

Response: Returns user profile details.

Custom User Model
This project features a custom user model that extends Django's default AbstractUser.

Key Fields:
bio: A textual description or biography of the user.

profile_picture: An uploaded image representing the user's profile.

followers: A Many-to-Many relationship field allowing users to follow and be followed.

The custom user model ensures scalability and flexibility for advanced social media features.