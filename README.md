Brief:
The objective of this project is to create a CRUD application, using supporting tools, methodologies and technologies 
learned in core modules so far, these include:
- Project Management
- Python Fundamentals
- Python Testing
- Git
- Basic Linux
- Python Web Development
- Continuous Integration
- Cloud Fundamentals
- Databases

Scope:
The following are the requirements for the project:
 - A Trello board (or equivalent Kanban board tech) with full expansion
on user stories, use cases and tasks needed to complete the project.
It could also provide a record of any issues or risks that you faced
creating your project.
 - A relational database used to store data persistently for the
project, this database needs to have at least 2 tables in it, to
demonstrate your understanding, you are also required to model a
relationship.
 - Clear Documentation from a design phase describing the architecture
you will use for you project as well as a detailed Risk Assessment.
A functional CRUD application created in Python, following best
practices and design principles, that meets the requirements set on
your Kanban Board
 - Fully designed test suites for the application you are creating, as
well as automated tests for validation of the application. You must
provide high test coverage in your backend and provide consistent
reports and evidence to support a TDD approach.
 - A functioning front-end website and integrated API's, using Flask.
 - Code fully integrated into a Version Control System using the
Feature-Branch model which will subsequently be built through a CI
server and deployed to a cloud-based virtual machine.

My Approach:
For my project, I decided to create an app to be used with Paintable Miniture Figurines. The app will allow the user to select
which model(s) they wish to paint, output which paints are needed for selected models and mark which paints they have and which
paints are needed.

To achieve this, I will start with creating a Jira board and researching which models need which paints and begin to create tables based on this information.

Jira Board:






![initial Jira](https://github.com/TSamson-QA/Fundamental_Project/blob/main/ERD.PNG)

Entity Relationship Diagram (ERD):






![table design](https://github.com/TSamson-QA/Fundamental_Project/blob/main/jira_1PNG.PNG)

I started by creating the list table, which is what i want the user to see when they have selected the required models. The list table has the List_ID as a primary key, as well as the foreign keys Model_ID and Paint-ID. Then the tables for Models and Paint were created, which both needed ID and names for each item. The Model table also contains which paint is needed for it.


