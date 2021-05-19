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






![initial Jira](https://github.com/TSamson-QA/Fundamental_Project/blob/main/jira_1PNG.PNG)


Entity Relationship Diagram (ERD):






![table design](https://github.com/TSamson-QA/Fundamental_Project/blob/main/ERD.PNG)

The Model table contains the Model_ID as the primary key, as well as Paint_ID as a foreign key. Model_name is also contained in the model table. The paint table contains Paint_ID and Paint_name, used to identify paint colour.

Risk Assessment:
Creating an application, however, does pose risks. Here, I will describe some of the risks that may be encountered and how I mitigated the risks as much as possible, as well as a Matrix.





![risk_matrix](https://github.com/TSamson-QA/Fundamental_Project/blob/main/Risk_Assess_Matrix.PNG)

1. Risk of Security Breaches: High Impact (4) Medium Probability (3).
   Creating an app nowadays will always come with security risks. The danger being the underestimation of the need of proper security. No application is guaranteed to be safe,
   so I will use the following to decrease the risk of a security breach where possible:
   - Use of Secret Keys: The use of a secret key will ensure that only the person using the application will be able to view the outcome of the application, by using encryption
     built in to Flask.
   - Use of a secure SQL server: Using a secure server will minimise the risk of security breaches.
   - Keeping security details secure: I will ensure that the Secret Key, as well as the details of the SQL server are not available to the public, this will mean that I cannot upload such details to GitHub.
2. Risk of creating an application that is not useful: High Impact (4) Low Probability (2).
   I wanted to create an application that will be useful to the end users, as it is very important to recognise what will be useful. I took the time to think about something
   that end users will find useful and designed the application around that.
3. Risk of Adding too many features: Medium Impact (3) Low Probabilty (2).
   Initially, I did want to create a bigger project than I needed to, which would take considerably more time and may even result in missing the set deadline for the project. I quickly realised that I needed to focus of the Minimum Viable Product.
   This was the result of planning to add too many features. Even though I did succumb to this way of thinking, I managed to scale the project down during the planning phase in
   order for it to be more achievable.
4. Risk of Technical Difficulties: Very High Impact (5) Low Probability (2).
   Due to this being the first major project, there will always be the risk of experiencing technical difficulties during development.      This can be mitigated by remembering to use available sources or asking instructors when needed.
5. Risk of Poor Management: Medium Risk (3) Medium Impact (3).
   The final product can be effected by self-management. If I am poorly managing my time and not following a set timetable to work at, the result of the final MVP could not meet expectations. To ensure a better quality of management, I am breaking down tasks completed, ones to be done, and the time frame in which to do it.
6. Risk of Poor Version Control: High Risk (4) Low Probability (2).
   To ensure that I am always working on version control, I have created a Dev branch within gitHub, which will store the version currently being worked on, with a functioning product being kept seperately within the Main branch of my repository. 

