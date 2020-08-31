# **ORIGINAL FANTASY GAME&trade;**

![Original Fantasy Game Banner Logo](static/images/core_img/logo_main.png "Original Fantasy Game Banner Logo")

## **Introduction**

This is the repository for **The Philanthropist** website.

The deployed site can be visited by clicking [**here**](https://pq-the-philanthropist.herokuapp.com/).

The site code can be viewed in this [**GitHub Repository**](https://github.com/an-slua-sidhe/milestone-4).

My name is **Paul Quinn** and I designed and developed this site in its entirety as part of my [**Fullstack Web Development Diploma**](https://codeinstitut#e.net/courses) with the **Code Institute**, Ireland. For my Milestone 4 project, I designed a fully functional fullstack e-commerce site called 'The Philanthropist'. The inspiration for this came from my background as an archaeologist and a love for history and our cultural heritage. The concept is that site users can donate an amount of money to their selected site, monument, artefact or text. These donations would then nominally go to a fictional charity called **The World Heritage Foundation™**, which would distribute the funds proportionately to help preserve the antiquities the user had selected.

The site is built on a fullstack **Django** framework, is deployed live on **Heroku** and uses AWS S3 to host media and static files. Locally, it uses the built-in **Django Db.sqlite3** database, whereas when deployed live it uses **Heroku's Postgres** database. Their is full authentication functionality on site using Django's Allauth: admin superusers can add and edit  items in the **Antiquities** and **Latest Options** apps, whereas normal users can register and login, gaining access to antiquity descriptions and their order history in the **Checkout** and **Profile** apps.

There is a full overview of the design/development process below, along with an extensive outline of the testing process, future features, user stories, responsivity and deployment.

## **Table of Contents**

1. [User Experience](#user-experience)
    - [User Stories](#user-stories)
        * [The Unauthenticated Site User](#the-unauthenticated-site-user)
        * [The Authenticated Site User](#the-authenticated-site-user)
        * [The Site Administrator](#the-site-administrator)
    - [Design Documents](#design-documents)
        * [Wireframes](#wireframes)
        * [Mockups](#mockups)
        <!-- If there is time!! NB -->
        <!-- * [Database Schema](#database-schema) -->
    - [Design Choices](#design-choices)
        * [Images](#images)
        * [Colours](#colours)
        * [Fonts](#fonts)
        * [Icons](#icons)
    - [Design Changes](#design-changes)

2. [Features](#features)
    - [Existing Features](#existing-features)
        * [Home App](#base-html)
        * [Latest Options App](#main-page)
        * [All Antiquities App](#list-of-classes/races/characters)
        * [Bag App](#create/edit-classes/races)
        * [Checkout App](#new_character/edit_character)
        * [Profiles App](#new-game-page)
    - [Future Features](#future-features)

3. [Technologies Used](#technologies-used)

4. [Testing](#testing)
    - [Testing Devices](#testing-devices)
        * [Mobile Devices](#mobile-devices)
        * [Laptop Devices](#laptop-devices)
        * [Desktop Devices](#desktop-devices)
    - [Developer Tools](#developer-tools)
        * [Chrome](#chrome)
        * [Firefox](#firefox)
        * [Opera](#opera)
        * [Edge](#edge)
        * [Internet Explorer](#internet-explorer)
        * [Safari](#safari)
        * [Mobile Resolutions](#mobile-resolutions)
        * [Tablet Resolutions](#tablet-resolutions)
        * [Desktop Resolutions](#desktop-resolutions)
    - [Media Queries](#media-queries)
    - [BrowserStack](#browserStack)
    - [Validation](#validation)
        * [HTML](#html)
        * [CSS](#css)
        * [JavaScript](#javascript)
        * [Python](#python)
        * [ARIA](#aria)
    - [User Scenarios](#user-scenarios)
        * [Unauthenticated user looking to browse antiquities](#unauthenticated-user-looking-to-browse-antiquities)
        * [Unauthenticated user looking to make a donation](#unauthenticated-user-looking-to-make-a-donation)
        * [Unauthenticated user trying to register for an account](#unauthenticated-user-trying-to-register-for-an-account)
        * [Authenticated user trying to login](#authenticated-user-trying-to-login)
        * [Authenticated user trying to view profile information](#authenticated-user-trying-to-view-profile-information)
        * [Site administrator looking to view backend information](#site-administrator-looking-to-view-backend-information)
        * [Site administrator trying to add or edit an antiquity](#site-administrator-trying-to-add-or-edit-an-antiquity)
    - [Outstanding Bugs](#outstanding-bugs)

5. [Deployment](#deployment)
    - [Local](#local)
    - [Remote](#remote)
    - [Heroku](#heroku)
    - [AWS](#aws)

6. [Credits](#credits)
    - [Code Used](#code-used)
    - [Images Used](#images-used)
    - [Acknowledgements](#acknowledgements)

___

## **User Experience**

I wanted the user experience to be clean and clear, where the sites purpose and concept was quickly and intuitively conveyed. I wanted the antiquities and the images of them to be the main focus of the site. I used a combination of a Bootstrap Template called [**Amado ??**](https://startbootstrap.com/)and a selection of high quality photos of the antiquities to achieve this. The chosen template already had a smooth and elegant UI which I could incorporate into my code. I tried to include extra non-template features (such as the edit and delete buttons for superusers or the use of the template home page as the **Latest Options App**) into the existing flow to the site.

### **User Stories**

There are different types of user which may visit the site, each with different goals and motivations. I have listed their stories in three categories; The Unauthenticated Site User, The Authenticated Site User, The Site Administrator.

#### The Unauthenticated Site User

* As an Unauthenticated Site User, I can browse the latest antiquities open to donations on the **Latest Options** page.
* As an Unauthenticated Site User,  I can browse all antiquities and sort and filter by name, value, period and category on the **All Antiquities** page.
* As an Unauthenticated Site User, I can select my chosen antiquities to donate to on the **All Antiquities** page and then go to the **Cart Page** to review my order.
* As an Unauthenticated Site User, I can navigate from the **Cart Page** to the **Checkout Page** to enter my billing details and finalise my donation anonymously.

#### The Authenticated Site User

* As an Authenticated Site User, I can **Register** to create a **New Profile** from the navbar.
* As an Authenticated Site User, I can **Login** to my previously created profile from the navbar and gain access to antiquity descriptions on **Single Antiquity** pages.
* As an Authenticated Site User, I can **Login** and view my **User Profile**, along with my **Order History**, via the link in the navbar.


#### The Site Administrator

* As a Site Administrator, I can create a **Superuser Profile** through Django.
* As a Site Administrator, I can access my **Superuser Profile** by typing the '/admin' url into the browser.
* As a Site Administrator, I can access all orders, emails, users and app fixtures by viewing the Django admin backend.

### **Design Documents**

I used [**Adobe XD**](https://www.adobe.com/ie/products/xd.html) to design and create **Wireframes** for this site. For the database schema I used [**DBDiagram**](https://dbdiagram.io/). These documents can be found as PNGs (wireframes) and PDFs (schema) in the **Design Docs Folder**.

#### Wireframes

The basic **Wireframes** are available in 8 PNGs; one which shows the [**Home Page**](static/design_docs/wireframes/home_page.png), one for [**Selected Products**](static/design_docs/wireframes/selected_products.png), one for a [**Shop**](static/design_docs/wireframes/shop.png) screen, the [**Single Item**](static/design_docs/wireframes/single_item.png) screen, the [**Shopping Cart**](static/design_docs/wireframes/shopping_cart.png) screen, one for [**Checkout**](static/design_docs/wireframes/checkout.png), [**Registration**](static/design_docs/wireframes/registration.png) and [**Login**](static/design_docs/wireframes/login.png). Any colour used is for contrast only. Simple text headings were added to each element to denote its purpose. These overall [**Design Choices**](#design-choices) can be traced to the final deployed [**Website**](https://pq-original-fantasy-game.herokuapp.com/), with some changes (see [**Design Changes**](#design-changes)).

#### Mockups

As the templae came with its own colour scheme that complimented the assets I had for the project, there was no need for full colour design mockups of the project.

<!-- 
If there is Time!! NB
#### Database Schema

The database in this project was non-relational, and therefore the actual schema is very simple. It can be found [here](static/design_docs/database_schema.pdf) and it shows how the Race and Class creation routes feed into the character creation section. -->

### **Design Choices**

The template was amended and shaped to match the overall aesthetic, allowing the image's colours to really shine through. The template I used was called [Amado](https://colorlib.com/wp/template/amado/) (live site [here](https://colorlib.com/preview/theme/amado/)). It was created by [Colorlib](https://colorlib.com) and distributed by [Themewagon](https://themewagon.com/). The theme needs several of its own static files to work ([**CSS**](static/css/) and [**JavaScript**](static/js/)). I changed and added to the CSS with my own [**CSS**](static/css/style.css).

#### Images

I wanted a selection of high quality images for the site, which would accurately bring across the nature of the antiquities. Where these images would be used was already decided in the design **Wireframes** (see [above](#basic-wireframes)). I found the art I sought  in various places, including [Pinterest](https://www.pinterest.ie/), the [Museum of Ireland](https://www.museum.ie/en-IE/home) website, the [British Museum](https://www.britishmuseum.org/) website, the [BBC](https://www.bbc.com/) website and various museum and heritage website sources (see below for full [**Credits List**](#credits)). All images were re-sized and compressed in [Photoshop](https://www.photoshop.com/en) before use.

#### Fonts

The fonts I used were mostly from the [**Amado Theme**] and were mostly of the Helvetica Neue font family. I combined the [**Napoli Initialen**](https://www.1001fonts.com/napoli-initialen-font.htm) font (from typographer [**Mediengestaltung**](https://www.1001fonts.com/users/steffmann/)) with Times New Roman to create the different iterations of the **Logo**.

#### Icons

A [**Navicon**](static/images/misc/favicon.png) was created for the site using the original [**Psygnosis Games logo**](https://en.wikipedia.org/wiki/Psygnosis), which I edited in Photoshop  Social media link icons were supplied by [Font Awesome](https://fontawesome.com/).

### **Design Changes From Wireframes**

The main difference from the original design is the use of the navbar to the left of screen rather than along the top. The left sided nav was part of the **Amado** template design, and provides a robust wrapping element for the 'base.html' file, into which all block content could be inserted to the right. This made for easy insertion and application of the various views and pages throughout site. I also used the original home page of the template to make a **Latest Options** page on site, with a new **Landing Page** created to greet the user when they first visit the site.
___

## **Features**

This is a multi-page fullstack framework site, with 6 separate **Django** apps. The basic layout of the site was created using the [**Bootstrap 4**](https://getbootstrap.com) grid system (which is based on [Flexbox](https://www.w3schools.com/css/css3_flexbox.asp)), with alterations and additions. The core of this is the use of containers, rows and columns as classes for elements. All **anchor** links within text are fully navigable; they also change colour when hovered over.

### **Existing Features**

#### Base HTML

This the is main template for the site, which contains the Head and Footer and Navbar elements for every other page, route or view. There is also a **Subscription** section which appears just above the **Footer** on each page.

* **Navbar**  

   This Navbar is the fully responsive navigation element. It contains links to the following screens: **Home**, **Latest Options**, **All Antiquities**, **Cart**, links for **Login**, **Registration** and **Add Antiquity**. There is also a **Cart Total** icon, a **Search** icon and some **Social Media** links. I added my own logo to the top of the navbar to connect it with the overall site theme. This element collapses to a dropdown on smaller resolutions.

* **Subscription**
    This is a simple element where users can subscribe to the site via an **EmailJS** enabled form.

* **Footer**  

   The Footer is a basic element that contains a small **Copyright** text and the site logo. The links in the navbar also appear here, and become a dropdown on smaller devices.

#### Main Page

The games opening page, containing the main logo and some information about the site, along with the [**Landing Page Background**](static/images/misc/landing_page_bg.jpg) which is an image of the Parthenon in Athens at night. There is also a CTA button asking the user to 'Donate Now'.

#### List of Classes/Races/Characters

The **List** screens fulfill the same purpose for Races, Classes and Characters. Here the user can see a selection of Classes/Races/Characters that they have already created or create a new item. There is also a set of **Preset Classes/Races** at the bottom of the List of Classes/Races pages to get the player started. From here the player can also **Edit** or **Delete** a Class/Race/Character.

#### Create/Edit Classes/Races

The Create and Edit screens and app routes are similar for both Classes and Races. These screens use the **CRUD Background Image**, which is a portait that suits the **Create/Edit Form's** shape. Here the player can create or edit a Class or Race using several criteria: **Class Name** (text input), **Class Information** (text input), **Class Stat Modifier** (dropdown choice) and **Class Image** (image carousel and dropdown choice). All of this information is stored in a **MongoDB** database for future use. The Class/Race Name and Stat Modifier information feeds directly into the **Form Fields** in the **Character Creation** screen.

#### New Character/Edit Character

Similar to the Create/Edit Class/Race views, but with more field elements in the **Form**. These form elements are: Character Name, Character Information, Gender, Class, Race and Profile Image. The Class and Race information feeds into these fields from the database via JinJa template code (Class/Race Name + Class/Race Stat Modifier = Class/Race choice).

#### New Game Page

Similar aesthetically to the Main Page, here the player chooses to 'Pick a new character' or 'Select a saved character'. Accessible from either the Main Page CTA or the Navbar.

#### Start Game Page

This page follows the same layout as the Main Page and New Game Page, but with a different background. This is the [**Start Game Background**](static/images/locations/beginning_path.jpg), which is an image of a path leading off into the distance. Here the player is asked to choose to 'Start with a selected characert' or 'Choose a different character'. Only accessible once the player has selected a Character.

#### Game Location 1

What will be the opening location of the adventure, this screen uses one of the [**Game Locations Images**](static/images/locations/castle_in_distance.jpg) as a background. Here instead there is some text on an opaque background explaining that the game is under constuction. The player is can choose to 'Return to the main menu' or 'See the game location art'.

#### Game Art Page

This page uses the same background image as **Game Location 1**. It contains a **Game Location Art Carousel**, which is a collection of detailed fantasy landscapes. The user can return to the main screen from here using the button below the carousel.

### **Future Features**

* **Pagination**  

    A soundtrack for the game is currently being composed by [**Corr Mhóna**](https://corrmona.bandcamp.com/) guitarist Martin Farrow. This will be multi-instrumental, and will be classical and atmospheric in tone.

* **Sorting by Date through Age Field addition to antiquities.json**  

    A full adventure is planned for the site, with a series of linked pages where the player can progress through the game locations, via simple Button prompts (Forward, Back, Left, Right), with scrolling text telling them about their surroundings.

* **Full Subscription Service linked to Django ADmin backend**  

    A designated collection in **MongoDB** will take the information for the player-selected Character. This will feed into the game GUI HUD, and will include the Character profile and stats. The character will also be able to roll for **Stamina**, **Skill**, **Luck** and **Intelligence** in the **Character Creation** screen. These stats will effect the players journey through the game in encounters with npcs and during player choices.

* **Extra Information Wikipedia link available on Single Antiquities detail view upon login**  

    A modal will come in to effect whenever the player encounters an enemy who they wish or have to fight. This will display the players stats vs. his enemy's stats and will show the outcome of the battle.

___

## **Technologies Used**

All the technologies used to create this project are listed below, along with their usage. Simply click on the title for a link to the main site. When there were separate instances where a technology was used, I have listed each link below.

### **Languages**

[**HTML**](https://en.wikipedia.org/wiki/HTML5) - This project's structure is based on **HTML 5**.

[**CSS**](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - This project's style was created using **CSS 3**.

[**Javascript**](https://en.wikipedia.org/wiki/JavaScript) -   A number of elements on the site have **Javascript** functionality (**JS 1.8.5**).

[**Python 3**](https://www.python.org/download/releases/3.0/) - This project's app routing was created using **Python 3**.

### **Versioning and Deployment**

[**Git**](https://git-scm.com/) - I used **Git** to create this project's local repository and to maintain version control.

[**Github**](https://github.com) - A remote repository was done through **Github**.

[**Heroku**](https://www.heroku.com/) - The site was deployed live on **Heroku**.

### **Other Technologies**

[**Flask**](https://flask.palletsprojects.com/en/1.1.x/) - This project's template logic was created using **Flask**.

[**MongoDB**](https://www.mongodb.com/) - This project's non-relational database is hosted by **MongoDB**.

[**VSCode**](https://code.visualstudio.com) - All code for this site (including this README file), and all **Github** versioning of this code, was done with **VSCode**.

[**Bootstrap**](https://getbootstrap.com) - The site was built using **Bootstrap's** grid system (**Bootstrap 4.5.0**).

[**Start Bootstrap**](https://startbootstrap.com/) - I sourced my website template from this site.

### **Design**

[**Adobe XD**](https://www.adobe.com/ie/products/xd.html) - The wireframes for this site were designed in **Adobe XD**.

[**DBDiagram**](https://dbdiagram.io/) - The database schema for this site was designed with **DBDiagram**.

[**Photoshop**](httpshttps://en.wikipedia.org/wiki/Adobe_Photoshopwww.gimp.org/) - I used **Photoshop** to edit all art and the **Favicon**.

### **Validators**

[**HTML Code Checker**](https://validator.w3.org)

[**CSS Code Checker**](https://jigsaw.w3.org/css-validator)

[**CSS Auto-prefixer**](https://autoprefixer.github.io)

[**Javascript Code Checker**](https://jshint.com/)

[**ARIA Checker**](http://wave.webaim.org/)

[**BrowserStack**](https://www.browserstack.com/) - Multi-platform testing site.

___

## **Testing**

### **Testing Devices**

The site was tested on various devices, including on mobile, laptop and desktop platforms. I list these below:

#### **Mobile Devices**

* Galaxy A5 (Running Android Oreo 8.0.0)
* Fairphone 3 (Running Fairphone OS C20134228)
* iPhone XR (Running iOS 13)
* iPhone SE (Running iOS 13)
* iPhone 7 (Running iOS 13.4.1)
* iPhone 6 (Running iOS 12.4.4)

#### **Laptop Devices**

* HP Pavilion (Running Windows 10)
* Dell Latitude (Running Windows 10)
* MacBook Air (Running Mojave)

#### **Desktop Devices**

* Asus G20CB-UK032T Core i7-6700 (Running Windows 10)

### **Developer Tools**

I tested the site in **Developer Tools** on six internet browsers (**Chrome**, **Firefox**, **Opera**, **Edge**, **Internet Explorer** & **Safari**). Bugs and errors were tackled successfully in this way throughout the development process.

* [**Chrome**](https://www.google.com/chrome/?brand=CHBD&gclid=Cj0KCQjwkK_qBRD8ARIsAOteukDltqXTjp13--esZkC4d8eL6Ggma28pvUQiVvwnJwVA06i0YbiSIuwaArNOEALw_wcB&gclsrc=aw.ds) (Version 81.0.4044.138)

* [**Firefox**](https://www.mozilla.org/en-US/firefox/new/) (Version 76.0.1)

* [**Opera**](https://www.mozilla.org/en-US/firefox/new/) (Version 68.0.3618.104)

* [**Edge**](https://www.mozilla.org/en-US/firefox/new/) (Version 44.18362.449.0)

* [**Internet Explorer**](https://www.microsoft.com/en-ie/download/internet-explorer.aspx) (Version 11.836.18362.0)

* [**Safari**](https://www.apple.com/lae/safari/) (Version 13.1)

I used the full gamut of responsivity in **Developer Tools**, but I also tested on the specific resolutions shown below:

#### **Mobile Resolutions**

* iPhone 4 (320 x 480)
* Galaxy S5 (360 x 640)
* iPhone X (375 x 812)

#### **Tablet Resolutions**

* iPad (768 x 1024)
* iPad Pro (1024 x 1366)

#### **Desktop Resolutions**

* Laptop with MDPI Screen (1280 x 800)
* Laptop with HiDPI Screen (1440 x 900)
* Gaming Desktop (2560 x 1440)
* 4K Monitor (3840 x 2160)
* 4k Plus (4000 x 2200)

### **BrowserStack**

[**BrowserStack**](https://www.browserstack.com/) - Any platform that I couldn't test in developer tools or on my own devices, I tested here.

### **Media Queries**

There are 8 separate **Media Query** resolution denominations in the [**CSS**](static/css/style.css) code. Every imaginable variation, from the smallest phone to the largest 4K monitor, was used to test the responsivity of the site. There are multiple elements being targeted and styled within several **Media Queries**.

### **Validation**

* [**HTML Code Checker**](https://validator.w3.org) - I checked my HTML with the **W3C Markup Validation Service**. It received the following messages:

  - Several "Error: Bad value for attribute href on element link: Illegal character in path segment: { is not allowed" warnings, for Jinja template language code across all HTML documents.

  - A "Warning: Consider adding a lang attribute to the html start tag to declare the language of this document" for each template besides base.html.

  - An "Error: End of file seen without seeing a doctype first. Expected ! DOCTYPE html" for each template besides base.html.

  - An "Error: Element head is missing a required instance of child element title" for each template besides base.html.

  - A "Warning: The first occurrence of ID delete_class was here" for each html document that have jinja urls that match element ids.
  
* [**CSS Code Checker**](https://jigsaw.w3.org/css-validator) - I checked my CSS with the **W3C CSS Validation Service**. It received the following messages for vendor prefixes unknown to the validator:

  - Style.css:
    - Line 33: "moz-transition is an unknown vendor extension".

    - Line 34: "webkit-transition is an unknown vendor extension".

    - Line 35: "o-transition is an unknown vendor extension".

    - Line 121: "moz-transition is an unknown vendor extension".

    - Line 122: "webkit-transition is an unknown vendor extension".

    - Line 123: "o-transition is an unknown vendor extension".

  - Grayscale.css:
    - 34 Errors; Mostly parse errors, with 2 property and one value error.

    - 225 Warnings; For vendor prefixes unknown to the validator, for duplicate colour selection for one element, and for pseudo-elements unknown to the validator.

* [**CSS Auto-prefixer**](https://autoprefixer.github.io) - The **CSS Online Auto-prefixer** provided a **Vendor Prefix** check for my code. I added all suggestions to my CSS.

* [**Javascript Code Checker**](https://jshint.com/) - I checked the JavaScript in grayscale.js with **JS Hint**. It received the following messages:

  - Metrics:
    - "There are 4 functions in this file".

    - "Function with the largest signature take 1 arguments, while the median is 0".

    - "Largest function has 6 statements in it, while the median is 4.5".

    - "The most complex function has a cyclomatic complexity value of 5 while the median is 1.5".

  - One warning
    - "Line 18; Misleading line break before '?'; readers may interpret this as an expression boundary".

  - One undefined variable:
    - "Line 56; jQuery"

* [**ARIA Checker**](http://wave.webaim.org/) - I used **Wave** (Web Accessibility Evaluation Tool) to check that my code was accessible to all users.  It received the following messages:

  - 30 x Contrast Errors (Mostly reffering to the black background of the list pages and the main button colour on the landing page background)
  - 10 x Alerts for Redundant Links (All of which were legitimate links)
  - 15 x Suspicious Alternative Text (Referring to Fantasy names unknown to the validator)

### **User Scenarios**

#### **Unauthenticated user looking to browse antiquities**

* **Navbar Link**
    1. Go to the **Main Page**.
    2. Click on the **Navbar** on the top of the screen.
    3. Click on the link to **New Game**.
    4. On the **New Game Page**, either select to **'Create a new character'** or to **'Select a saved character'**.
    5. If **'Create a new character'** is selected, create a new Character and press **Save**, then continue to the **Start Game** screen.
    6. If **'Select a saved character'** is selected, choose a saved Character from the **List of Characters**, press **Save** and continue to the **Start Game** screen.
    7. On the **Start Game** screen, choose to **'Start with selected Character'**.

* **New Game Button**
    1. From the **Main Page**, press the CTA **'Start a new game!' button**.
    2. Follow steps 4-7 in **Navbar Link** above.

* **List of Characters**
    1. When browsing the **List of Characters** screen, choose one of the Characters by pressing the **Select Button** for that Character.
    2. Follow steps 4-7 in **Navbar Link** above.

#### **Unauthenticated user looking to make a donation**

#### **New Class/Race**

1. Go to the **Main Page**.
2. Click on the **Navbar** on the top of the screen.
3. Click on the links to either **List of Classes** or **List of Races**.
4. Select the **'Create a new class/race' button** at the top of the screen.
5. Create a new Class/Race by entering information into the form fields. Press **Save** to save it to the database and have it display on the **List of Classes/Races** page.

#### **Unauthenticated user trying to register for an account**

* **New Game Button**
    1. From the **Main Page**, press the CTA **'Start a new game!'** button.
    2. On the **New Game Page**, select the **'Create a new character' button**.
    3. Create a new Character by entering information into the form fields. Press **Save** to save it to the database and have it display on the **List of Characters** page.

* **List of Characters Link**
    1. When browsing the **List of Characters** screen, press the **'Create a new character' button** at the top of the screen.
    2. Create a new Character by entering information into the form fields. Press **Save** to save it to the database and have it display on the **List of Characters** page.

* **Navbar Options**
    1. Alternatively, from the **Main Page**, click on the **Navbar** on the top of the screen.
    2. Select either the **New Character**, **Saved Character** or **New Game** links.
    3. For **New Character**, create a new Character by entering information into the form fields, then press **Save**.
    4. For **Saved Characters** follow the steps in **List of Characters** above.
    5. For **New Game** follow the steps in **New Game Button** above.

#### **Authenticated user trying to login**

* **Navbar Link**
    1. Go to the **Landing Page** section.
    2. Click on the **Navbar** on the top of the screen.
    3. Click on the links to either **List of Classes**, **List of Races** or **Saved Characters**.
    4. For your the Class/Race/Character, press the **Edit Button** for that item.
    5. Edit the form fields on the **Edit** page, and press the **Save Button**.

* **On Screen UI Buttons**
    1. While browsing the **List of Classes**, **List of Races** or **Saved Characters** screens, follow steps 4-5 in the previous section.

#### **Authenticated user trying to view profile information**

1. On the Main Page, select **'Start New Game'**.
2. On the **New Game Page**, either select to **'Create a new character'** or to **'Select a saved character'**.
3. If **'Create a new character'** is selected, created a new Character and press **Save**, then continue to the **Start Game** screen.
4. If **'Select a saved character'** is selected, choose a saved Character from the **List of Characters**, press **Save** and continue to the **Start Game** screen.
5. On the **Start Game** screen, choose to **'Start with selected Character'**.
6. On **Game Location 1** screen, press the **'See game location art'** button.
7. Use the **Carousel** to browse the **Location Art**.

#### **Site administrator looking to view backend information**

1. Follow steps 1-6 in the previous section.
2. Read the current update on the game in the **Game Location 1** screen.
3. Come back later to review the actual game.

#### **Site administrator trying to add or edit an antiquity**

1. Follow steps 1-6 in the previous section.
2. Read the current update on the game in the **Game Location 1** screen.
3. Come back later to review the actual game.

___

## **Deployment**

### **Local**

* This project is deployed live on [**Heroku**](https://pq-original-fantasy-game.herokuapp.com/).

* You can run the code in your chosen local **Integrated Development Environment** (**IDE**, e.g. [**VS Code**](https://code.visualstudio.com), [**AWS CLoud9**](https://aws.amazon.com/cloud9)).
    1. Open the **Project Repository** in [**Github**](https://github.com/an-slua-sidhe/milestone-3).
    2. Look for the green *Coded* button at the top right of the repository.
    3. If using [**Github Desktop**](https://desktop.github.com), chose to *Open in Desktop*.
    4. If you want to **Clone** the files into a **Git** repository, chose to copy the URL from the same menu (# 2.). Open your chosen **Command Line Interface** (**CLI**, e.g. [**Gitbash**](https://git-scm.com/downloads)) and use the following command:


        ``` bash
        git clone https://github.com/an-slua-sidhe/milestone-3.git
        ```

    5. To set up the files manually in a local repository, chose to **Download ZIP** and remove the files from the ZIP folder. Place them into the chosen location. If desired, set up a **Git** repository in this folder in your **CLI** with the following command:

        

        ``` bash
        git init
        ```

    6. You can check the state of your repository after initialising it by using this command:

        

        ``` bash
        git status
        ```

### **Remote**

* To push the code to a remote repository, follow the steps below (I use **Github** as an example).

    1. After using the command 'git status' (see step 6 above) in the command line, check that the console reads:


        ``` bash
        Nothing to commit
        working tree clean
        ```

    2. Next, link your remote repository. For **Github**, open your Github account and select *Repositories*. At the top right of the screen select *New*.

    3. Give your repository a name. Keep it short and avoid underscores.

    4. You can now choose a few different ways to link the local and remote repositories. The one we want here is "…*or push an existing repository from the command line*". Copy the code this option gives you and paste it into your command line. It should look something like this:

        ``` bash
        git remote add origin https://github.com/an-slua-sidhe/milestone-2
        git push -u origin master
        ```

    5. Now you can push any changes from the command line with:

        ``` bash
        git push
        ```

    6. If you check the status of of your local repository now (using 'git status') it should give you something like this:

        ``` bash
        On branch master
        Your branch is up-to-date with 'origin/master'.
        nothing to commit, working tree clean
        ```

    7. Finally, to deploy the code live with **Github Pages**, open the repository in your **Github** account and select '*Settings*' at the top right of the page. Scroll down to the *Github Pages* section. Click on the '*None*' button. Select the correct branch from the menu. Now click on the URL link to visit the deployed site.

### **Heroku**

* To push the code to a Heroku and deploy it dynamically, follow the steps below.

    1. Following on from **Local** deployment step 6 above, type the command 'git status' in the command line and check that the console reads:

        ``` bash
        Nothing to commit
        working tree clean
        ```

    2. Next, create an App on Heroku. Log in to your previous Heroku account or set up a new one, select the *New* button on the top right of the screen, then select *Create New App*.

    3. Name your app (usinb only lowercase characters and dashes) and choose the regional server that best suits your location.

    4. Next, login to your Heroku account from your CLI using:

        ``` bash
        heroku login
        ```

        A browser window should open up where you can click to login to your account through your local IDE. If this does not open, select the link on the CLI with *ctrl + c* and open it manually.

    5. Link your existing Git repository to Heroku by adding Heroku as a remote repository:


        ``` bash
        heroku git:remote -a <project-name>
        ```

    6. From now on you can push your code from the CLI with:

        ``` bash
        git push heroku master
        ```

    7. Set the necessary *Environment Variables*. Select the *Settings* tab, and then select the *Config Vars* button. Enter the KEY - VALUE pairs for your config variables here (e.g. SECRET_KEY, IP, PORT etc.)

    8. Finally, select the *Open App* button the top right of the screen to see your deployed application.

___

## **Credits**

### **Code Used**

* **Grayscale Start Bootstrap Theme**  

    Source: https://startbootstrap.com/themes/grayscale/
    Live Site: https://startbootstrap.github.io/startbootstrap-grayscale/

### **Images Used**

Except where stated, all rights for the images used lies with their respective owners. Art is merely used here for illustrative purposes in the context of this academic project. Any future professional deployment of the site will use only my own assets.

* Several images were sourced from [**Pinterest**](https://www.pinterest.ie/).
* Several images were sourced from [**Deviant Art**](https://www.deviantart.com/)
* Two fighting Fantasu gamebook covers were used: [Forest of Doom](https://en.wikipedia.org/wiki/The_Forest_of_Doom) and [Deathtrap Dungeon](https://en.wikipedia.org/wiki/Deathtrap_Dungeon)
* The **Main Page Background** was created by [**Roger Dean**](https://www.rogerdean.com/)
* The Class image of the Thief comes from the game of the same name by [**Looking Glass Studios**](https://en.wikipedia.org/wiki/Thief:_The_Dark_Project)
* The Class image of the Warrior is by Simon Bisley, and comes from the 2000 A. D. comic [**Sláine**](https://en.wikipedia.org/wiki/Sl%C3%A1ine_(comics)) by Pat Mills.
* I have also used my own assets in this project (e.g. the *CRUD Screen* background).

### **Acknowledgements**

* I would like to acknowledge the wonderful books by Ian Livinsgtone and Peter Jackson that I spent many happy hours reading when I was younger.
* I would also like to acknowledge the contributions of [**Inkle Studios**](https://www.inklestudios.com/) and their computer game adaptions of the Sorcery! series of Fighting Fantasy books, which were an inspiration for this project.

![Original Fantasy Game Location Banner](static/images/misc/banner_2.jpg "Original Fantasy Game Location Banner")
