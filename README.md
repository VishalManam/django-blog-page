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

![Screenshot (52)](https://github.com/VishalManam/django-blog-page/assets/88299493/02a2a4a3-5eab-453d-9392-2143a2a0902b)



2. Login Page

![Screenshot (53)](https://github.com/VishalManam/django-blog-page/assets/88299493/a39c39e1-349f-42cb-8c48-9a9f88d58846)


3. Sign In Page

![Screenshot (54)](https://github.com/VishalManam/django-blog-page/assets/88299493/6ee9813a-ed44-4969-8514-80da2d915e90)


4. Reset Password Page

![Screenshot (55)](https://github.com/VishalManam/django-blog-page/assets/88299493/94609a2a-095d-46c3-9b61-4150f5327757)


5. Home Page after Signing In

![Screenshot (56)](https://github.com/VishalManam/django-blog-page/assets/88299493/b4b2f35a-4f63-46a1-bed2-748c43507fa6)


6. Profile Info

![Screenshot (57)](https://github.com/VishalManam/django-blog-page/assets/88299493/14129dff-a980-4c69-8cd5-d11c2705aa5e)


7. Post Operations

![Screenshot (58)](https://github.com/VishalManam/django-blog-page/assets/88299493/290ddd5c-0f41-4262-9a74-1575c7c60b85)


8. AWS S3 console for storing profile photos of users

![Screenshot (59)](https://github.com/VishalManam/django-blog-page/assets/88299493/a18c9133-1e60-4db3-aa2a-b7c18e37f43c)


9. Admin Login

![Screenshot (60)](https://github.com/VishalManam/django-blog-page/assets/88299493/c9ac00c2-46ab-453c-8ea1-f02b7e010a36)


10. Admin Database

![Screenshot (61)](https://github.com/VishalManam/django-blog-page/assets/88299493/c21772b0-709b-435d-a25e-9498694c97f4)


11. Create a new post

![Screenshot (62)](https://github.com/VishalManam/django-blog-page/assets/88299493/0b00a45d-b217-4906-9f71-aff9b98d43b3)


12. End of Page || Pagination

![Screenshot (63)](https://github.com/VishalManam/django-blog-page/assets/88299493/51968dfe-fece-494b-bde2-97befd8eb956)


## Contributions

Contributions to this project are welcome! If you have any suggestions or improvements, feel free to create a pull request. Please ensure to follow the project's code of conduct.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

The development of the fully functional Django blog page would not have been possible without the contributions, support, and inspiration from various individuals and resources. Special thanks to the Django community, open-source and the Python community.
