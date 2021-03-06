# Fundamental Project

## Table of Contents

 - [Brief](https://github.com/TSamson-QA/Fundamental_Project/blob/main/README.md#brief)
 - [Scope](https://github.com/TSamson-QA/Fundamental_Project#scope)
 - [My Approach](https://github.com/TSamson-QA/Fundamental_Project#my-approach)
 - [Entity Relationship Diagram](https://github.com/TSamson-QA/Fundamental_Project#entity-relationship-diagram-erd)
 - [Risk Assessment](https://github.com/TSamson-QA/Fundamental_Project#risk-assessment)
 - [First Working Build](https://github.com/TSamson-QA/Fundamental_Project/blob/main/README.md#first-working-build)
 - [Second Working Build](https://github.com/TSamson-QA/Fundamental_Project/blob/main/README.md#second-working-build)
 - [Third Working Build](https://github.com/TSamson-QA/Fundamental_Project/blob/main/README.md#third-working-build)
 - [Testing](https://github.com/TSamson-QA/Fundamental_Project#testing)
 - [Version Control](https://github.com/TSamson-QA/Fundamental_Project/blob/main/README.md#version-control)
 - [Application Security](https://github.com/TSamson-QA/Fundamental_Project/blob/main/README.md#application-security)
 - [Project Summary and Self Reflection](https://github.com/TSamson-QA/Fundamental_Project/blob/main/README.md#project-summary-and-self-reflection)


## Brief:

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

## Scope:

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

## My Approach:

For my project, I decided to create an app to be used with Paintable Miniture Figurines. The app will allow the user to select
which model(s) they wish to paint, output which paints are needed for selected models and mark which paints they have and which
paints are needed.

To achieve this, I will start with creating a Jira board and researching which models need which paints and begin to create tables based on this information.

## Jira Board:






![initial Jira](https://github.com/TSamson-QA/Fundamental_Project/blob/main/images/jira_1PNG.PNG)


## Entity Relationship Diagram (ERD):






![table design](https://github.com/TSamson-QA/Fundamental_Project/blob/main/images/ERD.PNG)

The Model table contains the Model_ID as the primary key, as well as Paint_ID as a foreign key. Model_name is also contained in the model table. The paint table contains Paint_ID and Paint_name, used to identify paint colour.

## Risk Assessment:

Creating an application, however, does pose risks. Here, I will describe some of the risks that may be encountered and how I mitigated the risks as much as possible, as well as a Matrix.





![risk_matrix](https://github.com/TSamson-QA/Fundamental_Project/blob/main/images/Risk_Assess_Matrix.PNG)
![risk_table](https://github.com/TSamson-QA/Fundamental_Project/blob/main/images/Risk_Assess_table.PNG)

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


## First Working Build:

![first_working_build](https://github.com/TSamson-QA/Fundamental_Project/blob/main/images/1ST_W_B.PNG)
![FWB add page](https://github.com/TSamson-QA/Fundamental_Project/blob/main/images/1ST_W_B_addpage.PNG)


After creating a set list of objects in both tables, and setting relationships between them, I was able to let the user select which model they wish to use, from a drop down menu. The user is then re-directed to the home page, where the selected models are displayed, as well as the paints needed for the selected models.

I am now planning to let the user remove selections, as well as add custom ones to the database.
I have updated the JIRA board as progress continues, adding more tasks as I go.



![jira2](https://github.com/TSamson-QA/Fundamental_Project/blob/main/images/jira_2.PNG)


## Second Working Build:

Following what was added to the JIRA board above, I implemented a delete function, which deletes a model entry and the paint associated with it. 



![2nd_W_B_delete](https://github.com/TSamson-QA/Fundamental_Project/blob/main/images/2nd_W_B_delete.png)

This delete function will also delete an entry if it has been added to the selected models list, allowing greater control for the user. I updated my JIRA board with my progress.



![jira3](https://github.com/TSamson-QA/Fundamental_Project/blob/main/images/jira_3.PNG)


## Third Working Build:

I was able to implement a new element in the application, which allows users to add entries to the database. 


![3_W_B_1](https://github.com/TSamson-QA/Fundamental_Project/blob/main/images/3rd_W_B_1.PNG)

If the user enters text in to the fields shown, they are added to the database and automatically added to the models list.

![3_W_B_2](https://github.com/TSamson-QA/Fundamental_Project/blob/main/images/3rd_W_B_3.PNG)

The user is able to manipulate this entry like they would be able to any other. The entry is also saved, and is available in the dynamic Select Field.

![3_W_B_3](https://github.com/TSamson-QA/Fundamental_Project/blob/main/images/3rd_W_B_4.PNG)


Now this is finally implemented, I have updated the Jira board as shown below, and plan to implement testing.

![JIRA_4](https://github.com/TSamson-QA/Fundamental_Project/blob/main/images/jira_4.PNG)

## Testing:

When the third working build was fully implemented, I started working on testing. I was able to successfully test with an 85% coverage. 

![Testing](https://github.com/TSamson-QA/Fundamental_Project/blob/main/images/testing.PNG)


## Version Control

![Version Control graph](https://github.com/TSamson-QA/Fundamental_Project/blob/main/images/version-control.PNG)

Through my project, I was able to maintain version control by only changing files directly on the dev branch. When features were fully working and implemented successfully, I merged the dev branch on to the Main branch. 

## Application Security

![Getenv Security](https://github.com/TSamson-QA/Fundamental_Project/blob/main/images/getenv_security.PNG)

In order to make the application more secure, I removed the server address and the secret key from the files. This will prevent information from being displayed publicly on GitHub.
To access the application, I need to set environment variables when hosting on a virtual machine, and accessing through Gunicorn. 


## Project Summary and Self Reflection:

In this section, I will do a self-evaluation and reflect on what could have been done more effectively and what I would add in the future.

### Self-Evaluation

I found that during my project, I initally did struggle with implementation of the dynamic drop down menu. I was able to get it to work perfectly fine, but did not know how to call values that had been selected. With help from my instructor, though, I was finally able to get this to work. Looking back on this, I should have asked sooner, rather than spend time attempting to fix it myself, this would have saved time and allowed me to better implement other features.

### Future Implementations

Upon looking at my completed project, I thought on what i would do differently, and what else i could implement of I were to continue the application in the future.
If i had more time to work on my project, I would have made a Many to Many relationship between the Models and the Paints tables. This would have allowed the user to have one model be associated with several different paints, more like what would actually be needed for painting a model. 
I would also like to implement Images into the application, displaying the model kit as well as the paints, and a finished product, when fully painted.

Overall, i feel the project went well and met the MVP, as was originally planned, I am pleased with this outcome, but would have liked to make some minor changes.
