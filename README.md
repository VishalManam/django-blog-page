# Fully Functional Blogging Platform using Django, AWS S3 and IAM

## Introduction
The blogging platform is a fully functional web application built using Django, AWS S3, and AWS IAM. It offers users a seamless experience to create, manage, and share blog posts. With essential features like user authentication, post creation, editing, and deletion, as well as password management and email validation, the platform provides a secure and user-friendly environment for bloggers to express their thoughts.

## Key Features
1. **User Authentication**: The platform enables users to create accounts, log in, and log out securely. Passwords are encrypted and stored following industry best practices.

2. **Password Management**: Users can reset their passwords while logged in, ensuring that they can maintain the security of their accounts easily.

3. **Forgotten Password Recovery**: The "Forgot Password" feature allows users to reset their forgotten passwords via email verification, providing a reliable way to regain access to their accounts.

4. **Blog Post Management**: Users can create, update, and delete blog posts from their accounts. This empowers bloggers to easily share their thoughts and manage their content efficiently.

5. **User Profiles**: The platform allows users to view their profiles, which showcase their personal information and blog posts, providing a sense of identity and personalization.

6. **AWS S3 Integration**: Photos and media files uploaded by users are securely stored and served using Amazon S3 (Simple Storage Service), ensuring efficient handling of media content.

7. **Email Validation**: Users must validate their email addresses during the registration process, enhancing security and preventing misuse of the platform.

## How to Run the Project
1. **Clone the Repository**: Start by cloning the repository to your local machine using the command: `git clone https://github.com/VishalManam/django-blog-page.git`
2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using: `pip install -r requirements.txt`
3. **Set up AWS S3 and IAM**: Obtain your AWS S3 and IAM credentials and configure them in the appropriate settings files.
4. **Database Configuration**: Configure the database settings according to your preferences in the Django settings file.
5. **Apply Migrations**: Apply the initial database migrations using: `python manage.py migrate`
6. **Run the Server**: Start the development server using: `python manage.py runserver`


## Conclusion
In conclusion, the blogging platform built with Django, AWS S3, and AWS IAM offers an extensive set of features for bloggers to manage their posts effectively. With secure user authentication, robust password management, and email validation, users can rest assured that their accounts are well-protected. The integration with AWS S3 ensures seamless handling and storage of media content. By following the provided instructions, you can easily set up and run the project on your local machine, ready to share your thoughts with the world. Happy blogging!

## Sample Images of the Project
1. Home Page

![alt text](https://raw.githubusercontent.com/VishalManam/django-blog-page/main/images/Screenshot%20(52).png)

2. Login Page

![alt text](https://raw.githubusercontent.com/VishalManam/django-blog-page/main/images/Screenshot%20(53).png)

3. Sign In Page

![alt text](https://raw.githubusercontent.com/VishalManam/django-blog-page/main/images/Screenshot%20(54).png)

4. Reset Password Page

![alt text](https://raw.githubusercontent.com/VishalManam/django-blog-page/main/images/Screenshot%20(55).png)

5. Home Page after Signing In

![alt text](https://raw.githubusercontent.com/VishalManam/django-blog-page/main/images/Screenshot%20(56).png)

6. Profile Info

![alt text](https://raw.githubusercontent.com/VishalManam/django-blog-page/main/images/Screenshot%20(57).png)

7. Post Operations

![alt text](https://raw.githubusercontent.com/VishalManam/django-blog-page/main/images/Screenshot%20(58).png)

8. AWS S3 console for storing profile photos of users

![alt text](https://raw.githubusercontent.com/VishalManam/django-blog-page/main/images/Screenshot%20(59).png)

9. Admin Login

![alt text](https://raw.githubusercontent.com/VishalManam/django-blog-page/main/images/Screenshot%20(60).png)

10. Admin Database

![alt text](https://raw.githubusercontent.com/VishalManam/django-blog-page/main/images/Screenshot%20(61).png)

11. Create a new post

![alt text](https://raw.githubusercontent.com/VishalManam/django-blog-page/main/images/Screenshot%20(62).png)

12. End of Page || Pagination

![alt text](https://raw.githubusercontent.com/VishalManam/django-blog-page/main/images/Screenshot%20(63).png)
