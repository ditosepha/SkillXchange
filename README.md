# SkillXchange Platform

Welcome to the SkillXchange platform repository! SkillXchange is a versatile platform designed for individuals eager to learn new skills and participate in various courses.

## Features

- **Token-Based Authentication**: Enables secure authentication using tokens.
- **Role-Based Permissions**: Admins, tutors, and students have distinct permissions based on their roles.
- **Course Management**: Tutors can create, modify, and delete courses.
- **Enrollment Validation**: Validates student enrollment based on maximum course capacity.
- **Pagination and Filters**: basic pagination and filters enhance user experience.
- **Feedback System**: Students can provide feedback on courses through ratings and reviews.

## User Roles and Permission Sets

- **Tutor**: Offers courses to students and manages their own courses. Cannot modify courses created by other tutors.
- **Student**: Learns new skills, views available courses, and enrolls in desired courses.

## Functionality

SkillXchange implements token-based authentication for secure user authentication. Role-based permissions ensure that each user has access to appropriate functionalities based on their role.

## Models

- **User**: Extends Django's built-in User model and includes customizations.
- **Skill Class**: Contains detailed information about courses, including name, description, tutor, running times, and maximum number of students.
- **Enrollment**: Tracks student involvement in specific courses.
- **Review**: Enables users to rate courses on a 5-point scale and provide reviews.

## Viewsets Logic

- **Tutors**: Can create and manage courses. Only authorized to modify courses they own.
- **Enrollment Process**: Includes validations based on the maximum capacity of students in a course.

## Database

SkillXchange utilizes PostgreSQL as the database management system to store and manage data efficiently.

## Swagger Documentation

The Swagger documentation for SkillXchange is set up using yasg drf, providing comprehensive API documentation for users and developers.
