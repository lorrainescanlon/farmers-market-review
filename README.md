# Farmers Market Review

## Code Institute - Portfolio Project 4 - Django 

Farmers Market Review is a review website which features full CRUD frunctionality to provide users with up to date information 
about markets. This platform allows users to share their experiences and rate markets they have visited so as to inform others,
currently it focuses on farners markets in and around County Kerry.

## Demo
![How the website looks on different devices](/static/docs/images/amIresponsive3.PNG)

### A live demo of the site can be found [here](https://farmers-market-review-55ade4f51551.herokuapp.com/)



## Tabe of Contents
- [Demo](#demo)
  - [A live demo of the site can be found here](#a-live-demo-of-the-site-can-be-found-here)
- [Site Goals](#site-goals)
- [UI/UX](#ui-ux)
  - [Agile](#agile)
  - [Wireframes](#wireframes)
  - [Design](#design)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Database Model](#database-model)
  - [CRUD](#crud)
  - [Market Model](#market-model)
  - [Review Model](#review-model)
  - [Ratings Model](#ratings-model)
  - [Picture Model](#picture-model)
  - [Contact Model](#contact-model)
- [Technologies Used](#technologies-used)
  - [Development Environment and Hosting](#development-environment-and-hosting)
  - [Libraries](#libraries)
    - [BOOTSTRAP](#bootstrap)
    - [All Auth](#all-auth)
    - [Crispy Forms](#crispy-forms)
  - [PostgresSQL](#postgres-sql)
  - [Cloudinary](#cloudinary)
- [Testing](#testing)
  - [Testing file](#testing-file)
  - [Bugs](#bugs)
    - [Bugs Fixed](#bugs-fixed)
    - [Bugs Remaining](#bugs-remaining)
- [Deployment](#deployment)
  - [Heroku Deployment](#heroku-deployment)
  - [Forking and Cloning](#forking-and-cloning)
- [Credits](#credits)
  - [Media](#media)
  - [Code](#code)
  - [Acknowledgements](#acknowledgements)


## Site Goals
- To provide a platfrom where market goers can get useful information about their local markets.
- To engage with users and enable them to review and rate their market expereince.
- To encourage would be visitors to visit the market by sharing reviews and ratings.
- Negative reviews might prompt market organisers and vendors to improve their service.
- To provide a means for feedback for site users to encourage the sharing of information.


## UI/UX
This website is aimed at people who have an interest in famers markets. It aims to encourage users to visit their local markets and help them to grow.

- **Strategy**: 
The goal is to create a space where markets goers can get information about local markets and share reviews with others.

- **Scope**: 
To include features that enhance the user experience and provide value to the user. Features like maps and market ratings help to achieve this.

- **Structure**: 
The user is presented with a landing page which lists the markets in paginated form. From here the user can browse to more detailed market information or follow the navigation links for different funtions of the page.  

  **_Website Sections:_**
  - **_Home / Landing Page:_** A list of markets in paginated form.
  - **_Header:_** A header containg navigation links to other pages of the website.
  - **_Market Detail:_** A page containing detailed market information and reviews.
  - **_Register:_** A page to register for a user account.
  - **_Login:_** A page where users to log in.
  - **_Logout:_** A page where users log out.
  - **_Contact:_** A page with a contact form.
  - **_News:_** A page with news articles.
  - **_Footer:_** A footer containing social media links.

- **Skeleton**:
The website is desinged with a simple hierarchical structure which the user can navigate through with ease.


- **Surface**:
A uniform design has been used throught with consistent colour schemes and font to provide a seamless user experience.
Colourful images of markets and produce are add interest used to enhance the user experience.
Pseudo classes such as hover, active and focus are used to add styling to elements when they change states.
Font used is Roboto. 

### Agile
This project was designed and built using the agile approach. I created a [GitHub project](https://github.com/users/lorrainescanlon/projects/3) and utilised the provided Kanban board method to split project elements into user stories and tasks. These tasks were updated as the project moved along until all tasks were completed.

![Kanban](/static/docs/images/kanban.PNG)

| **User Stories** |
| --- |
| As a site user I can click on a post so that I can read the full text. |
| As a site user I can view reviews so that I can decide whether to visit this market or not. |
| As a Site User I can register an account so that I can leave a review. |
| As a Site User I can modify or delete my reviews so that the information I provide is accurate. |
| As a Site User I can click on the Contact link so that I can contact the site owner. |
| As a Site Admin I can create, read, update and delete posts so that I can manage my site content |
| As a Site Admin I can create draft posts so that I can finish writing the content at a later time |
| As a Site Admin I can approve or disprove comments so that I can filter out objectionable content |
| As a Site Admin I can create or update the contact page content so that is it available to site users |
| As a Site Administrator I can upload market pictures so that I can support the written content |

### Wireframes
Wireframes were created using software. Frames were drafted for mobile and desktop design. Initial/ designs included met basic/early requirements and designs have evolved since. View the wireframe designs here ![Wireframes](/static/docs/wireframesmarketreview.pdf)

![Wireframe1](/static/docs/images/wire1.PNG)

![Wireframe2](/static/docs/images/wire2.PNG)


### Design
Colour Scheme
Font
Images, Map, Icons, Favicon, border style, border radius, shadow

## Features

### Existing Features

#### Navigation Bar
 - Navbar with seedling icon and page navigation links.
 - If user is authenticated/logged in the are presented with different navigation links.
 - Active link is highlighted in bold black text.
 - Collapsible burger menu with drop-down list on small to medium sized screens.

![Nav Bar](/static/docs/images/navbar.PNG)

![Nav Burger](/static/docs/images/navburger.PNG)

#### Search Box
 - The search box is located to the right of the navigation bar.
 - It searches market names and location fields to see if they contain the search query. 

![Search Box](/static/docs/images/searchbox.PNG)


#### Logged in display
 - Located under the navigation bar is tells the user wether they are logged in or not.
 - If they are logged in their username is displayed here.

![Logged In](/static/docs/images/loggedinas.PNG)

#### Footer
- The footer contains links to social media sites: Facebook, X, Instagram and YouTube.

![Footer](/static/docs/images/footer2.PNG)

#### Hero Image
 - A hero image is displayed on the home and seacrh results pages.
 - It depicts a market scene with a tradres stall full of colourful vegetables.
 - An overlay section with text describes the website.

![Hero](/static/docs/images/heroimage.PNG)

#### Market List
 - Markets are displayed as card items in a grid structure and paginated to display 6 per page. 

![Market Grid](/static/docs/images/marketgrid3.PNG)

#### Market Description
 - This section gives some detail of the market traders, location and operating times.
 - It also provides an average star rating and visit again score based on approved user reviews.

![Market Details](/static/docs/images/marketdetails2.PNG)

#### Map
 - The map tab displays the location of the market.

#### Image Carousel
 - The pictures tab shows an image carousel which displays images of the market and surrounding areas.

#### Review List
 - A list of approved reviews are displayed in order of date created
 - If the user is logged in an edit and delete button will be displayed on reviews belonging to that user.

#### Review Form
 - The review form allows logged in users to submit a review.
 - The form contains a textarea, a drop down menu to select a star rating and a radio button to indicate whether or not you would visit again.

#### Register
 - Registration form to become a site user.
 - Username and Password fields are required and validated.

#### Login
 - Login form to authenticate user.

#### Logout
 - Log out button to log user out.

#### Contact form
 - Contact form to enable users to provide feedback and/or contact the site administrator.

#### News
 - The news page is intended for future development.
 - Currently it displays a news article rendered from the News model. 
 - A newletter will appear here as a future add on as described below..

 ![News]()



### Future Features
Newsletter section with calendar of events taking place that month.
workshops coming up, popup markets, seasonal markets, fairs, festivals, food festivals, summer show, ploughing championships, bloom
Interview with producer/crafter of the month.
Seasonal grower gardener tips, recipies and craft ideas
New articles updated monthly. 
Users can subscribe to the newsletter once they have an account. 

Ability for user to upload images of their own along with their reviews.


#### Newsletter


## Database Model
The database model diagram was created using [Lucidchart](https://lucidchart.com)

![DBModel](/static/docs/images/dbmodels.png)

### Market Model
 - The market model stores data for featured farmers markets. 

### Review Model
 - The review model records reviews that are submitted for the markets stored in the market model.

### Pictures Model
 - The pictures model contains image urls for market pictures. These pictures are displayed on the image carousel on the markets detail page.

### Contact Model
 - Records contact messages sent via the form on the contact.html page.

### News Model
 - The news model contains news articles that can be pulled together to create a newslette on the news.html page.

### CRUD

The CRUD principle was at the center of the design process for this project. 

**Create:**
 - A user can create an account which is written to the database User model.
 - An authenticated user can create and submit a review that is written to the Review model.

**Read:**
 - A user can read detailed market information and review data returned from the Market and Review database models.
 - A user can search for markets by name and location details returned from the Market model.

**Update:**
 - An authenticated user can update or edit their own reviews recorded on the Review model.

**Delete:**
 - An authenticated user can delete their own review records from the Review model in the database.



## Technologies Used

### Development Enviornment and Hosting
 - [Figma](https://figma.com) - Wireframes.
 - [Lucid](https://lucid.app/) - Database ERD.
 - [GitHub](https://github.com/) - Version control.
 - [GitPod](https://gitpod.io) - IDE - used at the begining of the project then migrated to VS Code.
 - [Visual Studio Code](https://code.visualstudio.com) - IDE.
 - [Heroku](https://heroku.com) - Website hosting platform.
 - [Cloudinary](https://cloudinary.com/) - Image hosting platform.

### Libraries
#### Python
 - [Gunicorn](https://gunicorn.org/) - Python Http server for WSGI applications.
 - [pyscopg2](https://pypi.org/project/psycopg2/) - Python PostgresSQL Database adapter.

#### Django
 - [Django-allauth](https://docs.allauth.org/en/latest/) - An integrated set of Django applications used for user authentication and account management.
 - [Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Used for styled and responsive forms with validation.

#### Bootstrap
 - [Bootstrap5](https://getbootstrap.com/) - Front-end framework used to simplify html, css and responsive design features.

#### Whitenoise
 - [Whitenoise](https://whitenoise.readthedocs.io/en/stable/index.html) - Middleware used by Django to handle serving of the static files.

#### Summernote
 - [Summernote](https://summernote.org/) - WYSIWYG editor used by the site admin in the admin panel.

### PostgresSql
 - [PostgresSQL](https://www.postgresql.org/) - An object-relational database management system (ORDMBS) is used as the backend for this project.

### Google Maps API
 - [Google Maps](https://developers.google.com/maps) - Platform used to render maps on the website.

### Cloudinary

