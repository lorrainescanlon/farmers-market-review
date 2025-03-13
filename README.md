# Farmers Market Review

## Code Institute - Portfolio Project 4 - Django 

Farmers Market Review is a review website which features full CRUD frunctionality to provide users with up to date information 
about markets. This platform allows users to share their experiences and rate markets they have visited so as to inform others,
currently it focuses on farmers markets in and around County Kerry.

## Demo
![How the website looks on different devices](/static/docs/images/mockup.PNG)

A live demo of the site can be found [here](https://farmers-market-review-55ade4f51551.herokuapp.com/)

## Tabe of Contents
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
    - [Python](#python)
    - [Django](#django)
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
- To engage with users and enable them to review and rate their market experience.
- To encourage would be visitors to visit the market by sharing reviews and ratings.
- Negative reviews might prompt market organisers and vendors to improve their service.
- To provide a means for feedback for site users to encourage the sharing of information.


## UI/UX
This website is aimed at people who have an interest in farmers markets. Its objective is to encourage users to visit their local markets and help them to grow.

- **Strategy**: 
The goal is to create a platform where markets goers can get information about local markets and share reviews with others.

- **Scope**: 
To include features that enhance the user experience and provide value to the user. Features like maps and market ratings help to achieve this.

- **Structure**: 
The user is presented with a landing page which lists the markets in paginated form. From here the user can browse to more detailed market information or follow the navigation links for different functions of the page.  

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
More on this is the design section below.


### Agile
This project was designed and built using the agile approach. The first step in this process was to create the user stories which address the expectations and needs of the site users.
Each user story had acceptance criteria defined and was managed through stages on a Kanban board

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


I created a [GitHub project](https://github.com/users/lorrainescanlon/projects/3) and utilised the provided Kanban board method to manage user stories and tasks. These tasks were updated as the project moved along and acceptance criteria was met, until all tasks were completed.

![Kanban](/static/docs/images/kanban.PNG)


### Wireframes
Wireframes were created using Figma software. The initial designs met basic early requirements that have evolved since. View the wireframe designs here ![Wireframes](/static/docs/wireframesmarketreview.pdf)

![Wireframe1](/static/docs/images/wire1.PNG)

![Wireframe2](/static/docs/images/wire2.PNG)


### Design
There is a consistent colour scheme used throughout the site as shown on the colour palette below. These colours are complimented by rich images of markets that add interest and enhance the user experience.
The font used was Roboto from Google fonts. Icons were used to highlight certain elements of the website, the seedling icon is used within the heading to give a logo effect.
Border styles and shadow are added to elements to add texture and interest. Pseudo classes such as hover, active and focus are used to add further styling and effects to elements when they change states.
 
![colour palate](/static/docs/images/colourpalette.PNG)


## Features

### Existing Features

#### Navigation Bar
 - Navbar with website name, seedling icon and page navigation links.
 - If user is authenticated/logged in they are presented with different navigation links.
 - An active link is highlighted in bold black text.
 - The search box is located to the right of the navigation bar.

 ![Nav Bar](/static/docs/images/navbar.PNG)

 - A logged in display tells the user whether they are logged in or not.

 ![Mobile nav](/static/docs/images/mobvanbar.jpg)

 - The navbar becomes a collapsible burger menu with drop-down list on small to medium sized screens.

 ![Nav burger](/static/docs/images/navburger.jpg)

#### Footer
 - The footer contains links to social media sites: Facebook, X, Instagram and YouTube.

 ![Footer](/static/docs/images/footer.PNG)

 - The quotes stack vertically on mobile screens.

 ![Mobile footer](/static/docs/images/mobfooter.jpg)

#### Hero Image
 - A hero image is displayed on the home and seacrh results pages.
 - It depicts a market scene with a traders stall full of colourful vegetables.
 
 ![Hero](/static/docs/images/heroimage.PNG)

 - An overlay section with text describes the website.

 ![Mobile hero](/static/docs/images/mobhero.jpg)

#### Market List
 - Markets are displayed as card items in a grid structure and paginated to display 6 per page. 

 ![Market grid](/static/docs/images/marketgrid.PNG)

 - Market cards stack vertically on mobile devices.

 ![Mobile grid](/static/docs/images/mobgrid.jpg)

#### Market Description
 - This section gives some detail of the market traders, location and operating times.

 ![Market details](/static/docs/images/marketdetails2.PNG)

 - It also provides an average star rating and visit again score based on approved user reviews.

 ![Mobile detail](/static/docs/images/mobdetails.jpg)

 - The map tab displays the location of the market.

 ![Mobile carousel](/static/docs/images/mobcarousel.jpg)

 - The pictures tab shows an image carousel which displays images of the market and surrounding areas.

 #### Reviews 
 - A list of approved reviews are displayed in order of date created.
 - If the user is logged in an edit and delete button will be displayed on reviews belonging to that user.

 ![Reviews](/static/docs/images/reviews.PNG)


#### Review Form
 - The review form allows logged in users to submit a review.
 - The form contains a textarea, a drop down menu to select a star rating and a radio button to indicate whether or not you would visit again.

 ![Review form](/static/docs/images/reviewform.PNG)


#### Register
 - Registration form to become a site user.
 - Username and Password fields are required and validated.

 ![Register](/static/docs/images/register.PNG)

#### Login
 - Login form to authenticate user.

 ![Login](/static/docs/images/loginpage.PNG)
  

#### Logout
 - Log out button to log user out.

  ![Logout](/static/docs/images/logout2.PNG)


#### Contact form
 - Contact form to enable users to provide feedback and/or contact the site administrator.

  ![Contact](/static/docs/images/contact.PNG)

#### News
 - The news page is intended for future development.
 - Currently it displays a news article rendered from the News model. 
 - A newletter will appear here as a future add on as described below.

 ![News](/static/docs/images/news.PNG)


### Future Features
 - Monthly Newsletter section with calendar of events taking place like workshops, popup markets, seasonal markets, fairs, festivals, food festivals, competitions.
 - Interview with producer/crafter of the month.
 - Users can subscribe and unsubscribe to the newsletter once they have registered an account. 
 - Have a review like button, for users to like if they found a review helpful.
 - Ability for registered user to upload images of their own along with their reviews.


## Database Model
The database model evolved from the needs of the user stories. Originally I had included a ratings model to store ratings data to calculate the stars ratings and visit again score. 
I eventually decided against including it as the data could be generated easily from the reviews model data. 
The diagram was created using [Lucidchart](https://lucidchart.com)

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
 - [Cloudinary](https://cloudinary.com) - Platform for hosting images and video.

## Testing

### Testing File
For detailed testing, validation and results please refer to the [Testing Document](TESTING.md)

### Bugs

#### Bugs Resolved
 - Google Maps. I ran into problems early on with locations not displaying correctly on the maps. I found that the coordinates being passed to render the maps center were not correct even though I had eneterd them correctly through the admin console. The latitude and longtitude fields were created as float point numbers, I changed this to Charfield and the issue resolved.

 - Market Detail Error. When I deployed the site to Heroku it started throwing error 500 server errors when I tried to access some market detail pages. On the ide with debug set to true an error "name 'visityes_percent' is not defined" was returned. This was happening to markets who had no reviews against them yet, so no value for 'visityes_percent' or 'visitno_percent' was being calculated. I added an if statement to the markets_review views.py to ensure that if no reviews were present that a value of 0 was returned for 'visityes_percent' and 'visitno_percent'.

        if review_count <= 0:
          visityes_percent = 0
          visitno_percent = 0
        else:
            visityes_percent = int((visityes_count/review_count)*100)
            visitno_percent = int((visitno_count/review_count)*100)

 - Pagination issue. When returning a search query that had more than one page of results the second page wouldnt load, it returned the following error. 
 
 "ValueError at /search/ Cannot use None as a query value object_list = Market.objects.filter(Q(name__icontains=query) | Q(location__icontains=query)).order_by('name')."

 I found a resolution on stackoverflow by doing a google search of the error https://stackoverflow.com/questions/57883376/error-cannot-use-none-as-a-query-value-when-trying-to-paginate-with-listview I updated my code from 

        {% if page_obj.has_previous %}
          <li><a href="?page={{ page_obj.previous_page_number }}" class="page-link link"> &laquo; PREV</a></li>
        {% endif %}
        {% if page_obj.has_next %}
          <li><a href="?page={{ page_obj.next_page_number }}" class="page-link link"> NEXT &raquo;</a></li>
        {% endif %} 

    To the following

        {% if page_obj.has_previous %}
          <li><a href="/search?page={{ page_obj.previous_page_number }}&q={{ query }}" class="page-link link"> &laquo; PREV</a></li>
        {% endif %}
        {% if page_obj.has_next %}
          <li><a href="/search?page={{ page_obj.next_page_number }}&q={{ query }}" class="page-link link"> NEXT &raquo;</a></li>
        {% endif %}

 - Review form not refreshing once submitted. During user testing I ran into an issue where the review form was not refreshing after a review had been submited, it was still populated with the review data. On investigation the line of code used to reset the form in the view had been indented incorrectly. I corrected the indentation and the form worked as expected.

 - Search feature returning all markets for empty search string. During user testing it was found that the search function returned all records from the markets model for an empty search string. I added an if statement to search_view to return None for an empty search.

        if query:
            object_list = Market.objects.filter(
                Q(name__icontains=query) | Q(location__icontains=query)
                ).order_by('name')
            paginator = Paginator(object_list, 6)
            page_number = request.GET.get("page")
            page_obj = paginator.get_page(page_number)

            context = {
                "query": query,
                "object_list": object_list,
                "page_obj": page_obj
              }
        else:
            object_list = None
            context = {
              "query": query,
              "object_list": object_list,
            }
  
#### Bugs Remaining
 - Validator error for google maps url. Bad Value error. The value for the location parameter is being passed with spaces, this isn't affecting the rendering of the maps however. Adding a function to the market_detail view to remove spaces before passing the value to the maps url may work. Or creating a new variable for the url value as the location variable is used elsewhere on the market_detail template.

 - Errors on all-auth signup template. Syntax rules as described in testing document which do not seem to affect the function of the form. 


## Deployment

### Pre-requisites
Ensure the following are installed and added to requirements.txt prior to deployment to Heroku.
- Gunicorn, required by Heroku to run Django.
- Pyscopg2, required to connect to PostgreSQL.
- Whitenoise, to enable the serving of static files in prodution environment.
- Cloudinary, to host images and video files.

### Heroku Deployment
- The site was deployed to Heroku, the steps used were as follows: 
  - Create and login to your heroku account. 
  - On your heroku dashboard, click the new button and 'create new app' from the dropdown menu.
  - Enter the name of the app 'farmers-market-review', select region as 'Europe' and click the 'Create app' button
  - On the app screen select the 'Settings' tab.
  - Find the 'Config Vars' section and populate the following Key : Value pairs
    - CLOUDINARY_URL *your key value*
    - DATABASE_URL *your key value* 
    - GMAPS_API_KEY *your key value*
    - SECRET_KEY *your key value*
  - Scroll back to the top of this page and find the Deploy tab. 
  - On this page find 'Deployment method' and select 'GitHub'.
  - In the 'Connect to Github' section enter the name of your repository and click 'Connect'.
  - On the deploy page select your preferred deployment type I choose 'Enable Automatic Deploys'.
  - The app will be built on your next push to github.
  - Once created the app appears on your heroku dashboard. 
  - Click on app and your dashboard and 'Open app' from the app page. 
  - The app opens in a console loaded in a browser window.

### Forking and Cloning
You can choose to fork or clone your project for development purposes. Forking creates a separate repository that shares code and visibility settings with the original repository. You can make changes to a forked repsotitory without affecting the original repository.
You can clone your repository to create a local copy on your computer and sync between the two locations. Changes made to a clone repository will affect the original repository.

To Fork
- Log in to GitHub.
- Find the repository for your project.
- Click the Fork button in the top right corner of the screen.

To Clone
- Log in to GitHub.
- Find the repository for this project.
- Click the Code button and select whether you would like to clone with HTTPS, SSH or GitHub CLI. Copy the link displayed.
- Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
- Type 'git clone' into the terminal and then paste the link you copied in the previous steps. 


## Credits

### Media
- Images were taken from pexel and unsplash
 - Hero image Photo by Wendy Wei [Pexels](https://www.pexels.com/photo/radish-and-carrots-1656663/)
 - Caherdaniel market card picture by Paréj Richárd [Unsplash](https://unsplash.com/photos/clear-glass-jars-on-brown-wooden-shelf-F20_xtNvis4?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash)
 - Dingle market card picture picture by Dave Takisaki [Unsplah](https://unsplash.com/photos/person-carrying-beige-tote-bag-in-front-of-food-stall-at-daytime-TFdkcrw-_4M?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
 - Inch market card picture by Michael Starkie [Unsplash](https://unsplash.com/photos/a-herd-of-cattle-standing-next-to-each-other-on-a-lush-green-field-BSCynDNMP2k?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash)
 - Kenmare market card picture no author [Pixabay](https://pixabay.com/photos/shellfish-meal-food-yummy-seafood-2114006/)
 - Listowel market card Clem Onojeghuo [Pexels](https://www.pexels.com/photo/man-standing-in-front-of-bowl-and-looking-towards-left-375889/)
 - Miltown market card picture by Dahlia E. Akhaine [Unsplash](https://unsplash.com/photos/a-bunch-of-cheeses-that-are-on-a-table-DH13R1yMtdE?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash)
 - Portmagee market card picture by tookapic [Pixabay](https://pixabay.com/photos/fish-fresh-market-food-seafood-933187/)
 - Tralee market card picture by Bree Anne [Unsplash](https://unsplash.com/photos/a-woman-talking-on-a-cell-phone-next-to-a-table-full-of-vegetables-dafqajrdhYI?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash)
 - Fonts were taken from [Fontawesome](https://fontawesome.com/)
 - Content was written by myself.

### Code
 - I used the walkthrough blog project as a basis for farmers market review. I followed the same basic structure and file layout. In particular the javascript code for edit and delete button functionality.
 - Django documentation on aggregation that I used as a reference for calculation in market details view https://docs.djangoproject.com/en/5.1/topics/db/aggregation/
 - Google Maps Platform documentation for implementing iframe https://developers.google.com/maps/documentation/embed/embedding-map
 - Stackoverflow resolution for pagination problem https://stackoverflow.com/questions/57883376/error-cannot-use-none-as-a-query-value-when-trying-to-paginate-with-listview
 - Django documentation on queries that I used https://docs.djangoproject.com/en/4.0/topics/db/queries/#complex-lookups-with-q-objects
 - Search form tutorial with code that I used when creating the search box https://learndjango.com/tutorials/django-search-tutorial#search-form
 - I used this fix to center list items on the registration form https://stackoverflow.com/questions/28977320/how-do-i-get-the-bullets-of-an-unordered-list-to-center-with-the-text
 - Bootstrap resource used for code for navbar and footer https://getbootstrap.com/docs/5.1/components/navs-tabs/
 - Bootstrap resource used for implementing carousel https://getbootstrap.com/docs/5.1/components/carousel/
 - Bootstrap progress bar code https://getbootstrap.com/docs/4.0/components/progress/


### Acknowledgements
- Thank you to my mentor Medale Oluwanfemi for his advice and guidance on this project.
- The tutoring team for their help at troubleshooting during the project.


