#Farmers Market Review TESTING.md

## Table of Contents
- [Manual Testing](#manual-testing)
 - [Navigation](#navigation)
 - [User Stories Testing](#user-stories-testing)
 - [Search Function](#search)
 - [CRUD Functionality](#crud-functionality)
 - [Account/Authentication](#account-authentication)
 - [Social Links](#social-links)
- [Lighthouse Testing](#lighthouse-testing)
 - [Mobile](#mobile)
 - [Laptop PC](#Laptop-PC)
- [Code Validation](#code-validation)
 - [HTML](#html)
 - [CSS](#css)
 - [Python](#python)
 - [JavaScript](#javascript)
- [Browser Compatibility](#browser-compatibility)

## Manual Testing
### Navigation

| **Feature** | **Expected Outcome** | **Result** |
| ----------- | -------------------- | ---------- |
| Home link | To be redirected to home page | Pass |
| Register link | To be directed to regitration user page | Pass |
| Login link | To be directed to user log in page | Pass |
| Contact link | To be directed to site contact page | Pass |
| Logout link | To be directed to the user log out page | Pass |
| News link | To be directed to the news page | Pass |
| Market link | To be directed to a particular market page | Pass |
| Facebook link | To be directed to the facebook website | Pass |
| X link | To be directed to the X website | Pass |
| Instagram link | To be directed to the Instagram website | Pass |
| YouTube link | To be directed to the YouTube website | Pass |

### User Story Testing

| **User Story** | **Expected Outcome** | **Result** |
|----------------|----------------------|------------|
| As a site user I can click on a post so that I can read the full text. | When a post is clicked, a detailed view is displayed. | Pass |
| As a site user I can view reviews so that I can decide whether to visit this market or not | The site user can scroll down through the user reviews underneath the market post. | Pass|
| As a Site User I can register an account so that I can leave a review |The site user can register, log in and subsequently submit a review. | Pass |
| As a Site User I can modify or delete my reviews so that the information I provide is accurate. | Once logged in a site use can modify and/or delete their review(s) | Pass |
| As a Site User I can click on the Contact link so that I can contact the site owner. | When the Contact link is clicked the contact form is displayed providing a means of contact for the user. | Pass |
| As a Site Admin I can create, read, update and delete posts so that I can manage my site content | Once logged in to the admin console the site admin can create, read, update and delete market posts. | Pass |
| As a Site Admin I can create draft posts so that I can finish writing the content at a later time | Once logged in to the admin console the site admin can save posts as draft to submit later. | Pass |
| As a Site Admin I can approve or disprove comments so that I can filter out objectionable content | Once logged in to the admin console the site admin can approve or delete comments before they are posted to the site. | Pass |
| As a Site Admin I can create or update the contact page content so that is it available to site users | Once logged in to the admin console, the site admin can update the contact details and text. | Pass |
| As a Site Administrator I can upload market pictures so that I can support the written content | Once logged in to the admin console, the site admin can upload market pictures. | Pass |

### Search Function

| **Feature**| **Expected Outcome** |  **Testing Perfomed** | **Outcome** | **Result** | 
| -----------| -------------------- | --------------------- | ----------- | ---------- |
| Search for market by name | Single result to be returned or 'No Markets found' message | Search for 'dingle' | One market 'Dingle' returned | Pass | 
| Search for market by part name | One or more results containing serach query in Market name or location are returned in paginated form or 'No Markets found' message | Searched for 'inc' | One market 'Inch' returned | Pass |
| Search for market by location | One or more results containing serach query in Market name or location are returned in paginated form or 'No Markets found' message| Search for 'brandon' | One market 'Tralee' returned | Pass |
| Search for market by part location | One or more results containing serach query in Market name or location are returned in paginated form or 'No Markets found' message | Search for 'ken' | One market 'Kenmare' returned | Pass | 
| Search for market by location area | One or more results containing serach query in Market name or location are returned in paginated form or 'No Markets found' message | Search for 'Kerry' | 8 markets are returned in paginated form | Pass |
| Search for market not in the database | 'No Markets found' message returned | Search for 'cork' | 'No Markets found' returned | Pass |
| Search empty query | 'No Markets found' message returned | Search for '' |  Pass | 
| **Feature** | **Expected Outcome** | **Testing Performed** | **Result** | **Pass/Fail** |

### CRUD Functionality

 **Create**                                                  

| **Feature** | **Action** | **Expected Result** | **Result** |
| ----------- | ---------- | ------------------- | ---------- |
| User account creation | Complete and submit the registration form | User can login using username and password. Username is displayed on logged in status bar | Pass |
| Submit a review | A registered user logs in and navigates to the market detail page. Here they fill in the review form and submit | Form is submitted successfully message is displayed and the review awaits admin approval. Once approved by admin it is committed to the database. | Pass | 

 **Read** 

| **Feature** | **Action** | **Expected Result** | **Result** |
| ----------- | ---------- | ------------------- | ---------- |
| Market grid display | When a user lands on the homepage markets are displayed in a grid style | Markets with a status of 'Published' are displayed on the grid | Pass |
| News Page | When a user lands on the news page news items are displayed | News articles with a staus of newsletter = True are displayed | Pass |      
| Market details | When a user navigates to the markets details page further details associated with that market are displayed | Market description, location, times, ratings, map and pictures are returned | Pass |

**Update**

| **Feature** | **Action** | **Expected Result** | **Result** |
| ----------- | ---------- | ------------------- | ---------- |
| Edit user review | A logged in user can edit a review on the markets detail page | Reviews belonging to a logged on user are displayed with an edit button. The review is loaded in the form, the user edits accordingly and submits. A submit successful message is displayed and the change awaits admin approval | Pass |

 **Delete** 

| **Feature** | **Action** | **Expected Result** | **Result** |
| ----------- | ---------- | ------------------- | ---------- |
| Delete user review | A logged in user can delete a review from the markets detail page | Reviews belonging to a logged on user are displayed with a delete button. The review is loaded in the form, the user deletes. A confirmation modal is displayed, the user confirms and the delete is committed | Pass |


### Authentication 

**Acount Registration** 

| **Test** | **Expected Outcome** | **Result** |
| -------- | -------------------- | ---------- |
| Register new User with valid username, email and password | Account created and registration sucessful message displayed | Pass |
| Register new User with valid username and password, no email | Account created and registration sucessful message displayed | Pass |
| Register new User with valid username, no password and no email | Account not created with password validation error message displayed | Pass |
| Register new User with valid password, no username and no email | Account not created with username validation error message displayed | Pass |
| Register new User with valid username, invalid password and no email | Account not created with password validation error message displayed | Pass |

**Account Login**
| **Test** | **Expected Outcome** | **Result** |
| -------- | -------------------- | ---------- |
| Login with a valid username and password | Account login sucessful message displayed, logged in as 'username' appears in logged in bar | Pass |
| Login with a valid username and no password | Account login fail, 'please fill out this field' prompt displayed in password input | Pass |
| Login with a valid username and incorrect password | Account login fail, 'The username and/or password you specified are not correct' message displayed. | Pass |
| Login with a no username and no password | Account login fail, 'please fill out this field' prompt displayed in username input | Pass |
| Login with a no username and a password | Account login fail, 'please fill out this field' prompt displayed in username input | Pass |

**Account Logout**
| **Test** | **Expected Outcome** | **Result** |
| Logout using 'Log Out' button on Logout page | Account logout successfull, 'You have signed out' message appears and logged in as status changes to 'You are not logged in' | Pass |


### Social Links
    - Social media links tested on both mobile and desktop. 
    - Social links tested in multiple browsers successfully.
    - All open in a separate browser window.


### Lighthouse Testing
Lighthouse testing was carried out on both desktop and mobile devices using chrome developer tools.

#### Mobile
[Mobile Lighhouse Test](/static/docs/images/lighthousemob.PNG)

#### Laptop/PC
[Desktop Lighthouse Test](/static/docs/images/lighthousedesk.PNG)


## Code Validaton

### HTML Validation [W3C validator](https://validator.w3.org/)
As this project contains Django tags and Jinja templating language the source code of each page was pasted into the validator directly as opposed to using the websites url.

**Home page**
Document checking completed. No errors or warnings to show.

**Market detail page**
Error reported in realtion to parameter value passed to google maps url. There are spaces in the location name.
![Market details validation error](/static/docs/images/markedetailvalidation.PNG)
![Error highlight in code](/static/docs/images/mapserror.PNG)

**Search results page.html**
Document checking completed. No errors or warnings to show.

**Register page**
Errors reported in the all auth signup template. It looks like they have ul and li tags inside a span which is invalid.  
![Register validation error](/static/docs/images/registervalidation.PNG)
![Error highlight in code](/static/docs/images/registrationerror.PNG)

**Login page**
Document checking completed. No errors or warnings to show.

**Logout page**
Document checking completed. No errors or warnings to show.

**Contact page**
Document checking completed. No errors or warnings to show.

**News page**
Document checking completed. No errors or warnings to show.


### CSS Validation [Jigsaw](https://jigsaw.w3.org/css-validator/)
No errors reported 
![css validation](/static/docs/images/cssvalidation.PNG)

### Javascript Validation [JSHint](https://jshint.com/)
One error returned regarding an undefined variable.
![javascript validation](/static/docs/images/jshint.PNG)

No action required as this is a custom bootstrap variable and did not need to be defined inside the script.

### Python Validation
I installed and used the pycodestyle tool to validate the projects python code. 
I ran the pycodestyle tool command for each app, contact, markets_review, my_project and news.
I corrected errors returned and wrote the results of the last pycodestyle tests to the following text file [pycodestyle](/static/docs/pycodestyle.txt)
The remaining errors are found within the migration files which cannot be corrected.

## Browser Compatibility
This site was tested on the browsers below for functionality, consistency and responsiveness:
 - Google Chrome - *Pass*
 - Microsoft Edge - *Pass*
 - Mozilla Firefox - *Pass*
