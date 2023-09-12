# Organ Management System

The Organ Management System is a comprehensive application designed to streamline the management and tracking of organ donations and transplantations. This system is built with Flask, providing a user-friendly interface for healthcare professionals and administrators to efficiently manage critical organ-related data.

## Features

- **Organ Donation Records:** Keep detailed records of organ donations, including donor information, organ type, and medical history.

- **Transplantation Management:** Manage organ transplant procedures, track recipient details, and monitor the transplantation process.

- **User Authentication:** Secure login and user roles to control access based on user types, ensuring data privacy and integrity.

- **Real-time Notifications:** Receive alerts and notifications for critical events such as organ availability and urgent transplant requirements.

- **Organ Inventory:** Maintain an inventory of available organs, including information on organ compatibility and status.

- **Reporting and Analytics:** Generate reports and analytics to assess organ donation and transplantation trends and outcomes.

Flask is utilized to build a web application. Flask routes are defined to handle HTTP requests, allowing you to render HTML templates for dynamic content. MySQL, managed via mysql.connector, is employed to interact with a database, enabling data retrieval and manipulation. HTML templates are used to create web pages, with Flask rendering them and passing data from MySQL queries to display dynamic content.

However, the primary focus of this project is Cloud computing, with deployment on the AWS cloud infrastructure. It involves a web application designed for Organ Management, where AWS services play a pivotal role. RDS (Relational Database Service) is used for secure data storage, while the web application is hosted on EC2 instances. Nginx is employed for load balancing to ensure optimal performance, and GitHub Actions automates testing processes to maintain code quality and reliability.




