# Multi-Organizational Management System with Role Management

## Overview
The **Multi-Organizational Management System** is a Django-based web application designed to support multiple organizations, each with its own users and role-based management. The system includes a main organization (Admin Organization) that oversees sub-organizations.

## Features
1. **Multi-Organization Support**:
   - Manage multiple sub-organizations under a main organization.
   - Each organization has users and roles.

2. **Role-Based Access Control**:
   - Roles such as Ceo, Chairman and Associate dictate access levels within an organization.
   - Only organization admins can assign roles to their users.

3. **User and Role Management**:
   - Organization admins can create, view, update, and delete users within their own organization.
   - Main organization admins can manage sub-organizations.

4. **Custom User Model**:
   - Extend Django's user model to associate users with organizations and roles.

## Requirements
- **Backend**: Django (Python)
- **Frontend**: Bootstrap 5, HTML

## Project Structure
- **Models**:
  - `Organization`: Represents an organization with details like name, address, and is_main.
  - `Custom User`: Extends Django's user to include fields for organization and role.
  - `Role`: Defines roles within an organization.

- **Views**:
  - CRUD operations for organizations and users.
  - Role assignment restricted to organization admins.
  - Secure views ensuring users see data specific to their organization and role.

- **Templates**:
  - Bootstrap 5 and HTML for responsive and user-friendly interfaces.

## Installation

### Prerequisites
- Python 3.10
- Django
- Bootstrap 5 (included via CDN in templates)
- SQLite

### Steps
1. Clone the Repository:
   ```bash
   git clone https://github.com/your-repository-url.git
   cd multi-organizational-management

2. Create a Virtual Environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate

3. Install Dependencies:
   ```bash
   pip install -r requirements.txt

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. Create a Superuser:
   ```bash
   python manage.py createsuperuser

6. Start the server:
   ```bash
   python manage.py runserver

7. Access the app in your browser at http://127.0.0.1:8000/.

### Assumptions
1. The main organization admin has full control over sub-organizations.
2. Roles are pre-defined and limited to "Ceo", "Chairman" and "Associate".

### Usage
1. Login as Superuser:
   - Use the superuser account created during setup to log in to the home page.
C
2. Create Roles:
   - Navigate to the Role Management section.
   - Create roles such as CEO, Chairman, and Associate.

3. Create Main Organization:
   - Go to the Organization Management section.
   - Create a new organization and check the "is_main" checkbox to designate it as the main organization.

4. Assign Role to Yourself:
   - Assign the CEO role to your user account to grant yourself superuser privileges within the system.

5. Manage Sub-Organizations:
   - As the superuser (CEO of the main organization), create sub-organizations.
  
6. User and Role Management:
   - Organization admins/CEO can:
      - Add, update, and delete sub-organizations within their organization.
      - Add, update, and delete users within their organization.
      - Assign roles such as Chairman or Associate to users.
      - Assign tasks.
   - Chairman can:
      - Add, update, and delete users within their organization.
      - Assign tasks.
   - Associate can:
      - Associate can view the tasks the assign to him.

### License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.