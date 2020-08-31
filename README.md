# **The Philanthropist**

![The Philanthropist Banner Logo](static/images/core_img/logo.png "The Philanthropist Banner Logo")

## **Introduction**

This is the repository for **The Philanthropist** website.

The deployed site can be visited by clicking [**here**](https://pq-the-philanthropist.herokuapp.com/).

The site code can be viewed in this [**GitHub Repository**](https://github.com/an-slua-sidhe/milestone-4).

My name is **Paul Quinn** and I designed and developed this site in its entirety as part of my [**Fullstack Web Development Diploma**](https://codeinstitut#e.net/courses) with the **Code Institute**, Ireland. For my Milestone 4 project, I designed a fully functional fullstack e-commerce site called 'The Philanthropist'. The inspiration for this came from my background as an archaeologist and a love for history and our cultural heritage. The concept is that site users can donate an amount of money to their selected site, monument, artefact or text. These donations would then nominally go to a fictional charity called **The World Heritage Foundation™**, which would distribute the funds proportionately to help preserve the antiquities the user had selected.

The site is built on a fullstack **Django** framework, is deployed live on **Heroku** and uses **AWS S3** to host media and static files. Locally, it uses the built-in **Django Db.sqlite3** database, whereas when deployed live it uses **Heroku's Postgres** database. Their is full authentication functionality on site using Django's Allauth: admin superusers can add and edit  items in the **Antiquities** and **Latest Options** apps, whereas normal users can register and login, gaining access to antiquity descriptions and their order history in the **Checkout** and **Profile** apps.

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

I wanted the user experience to be clean and clear, where the sites purpose and concept was quickly and intuitively conveyed. I wanted the antiquities and the images of them to be the main focus of the site. I used a combination of a Bootstrap Template called [**Amado**](https://startbootstrap.com/) and a selection of high quality photos of the antiquities to achieve this. The chosen template already had a smooth and elegant UI which I could incorporate into my code. I tried to include extra non-template features (such as the edit and delete buttons for superusers or the use of the template home page as the **Latest Options App**) into the existing flow to the site.

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

#### **Home App**

This the is main template for the site, which contains the Head and Footer and Navbar elements for every other page, route or view. There is also a **Subscription** section which appears just above the **Footer** on each page.

* **Navbar**  

   This Navbar is the fully responsive navigation element. It contains links to the following screens: **Home**, **Latest Options**, **All Antiquities**, **Cart**, links for **Login**, **Registration** and **Add Antiquity**. There is also a **Cart Total** icon, a **Search** icon and some **Social Media** links. I added my own logo to the top of the navbar to connect it with the overall site theme. This element collapses to a dropdown on smaller resolutions.

* **Subscription**
    This is a simple element where users can subscribe to the site via an **EmailJS** enabled form.

* **Footer**  

   The Footer is a basic element that contains a small **Copyright** text and the site logo. The links in the navbar also appear here, and become a dropdown on smaller devices.

#### **Main Page**

The games opening page, containing the main logo and some information about the site, along with the [**Landing Page Background**](static/images/misc/landing_page_bg.jpg) which is an image of the Parthenon in Athens at night. There is also a CTA button asking the user to 'Donate Now'.

#### **Latest Options App**

Here I amended the original **Amado** home page to create a new app for the latest antiquities to become available for donation. There is a separate 'latest_options' model and fixture which superusers can update from the admin panel, so the items can be refreshed when new ones become available for donation. Each option links through to the 'single_antiquity' view for that antiquity_id. I created an opaque background and styled the item's title information as it wasn't legible on the bright and detailed antiquity images (as opposed to the austere and white images used in the orginal template).

#### **All Antiquities App**

- All Antiquities View  
This app adds an extra column between the navbar to the left and the antiquities information to the right. This is where you can sort by category or period. The antiquities section contains the image, value, date and name of each item, along with a shopping cart icon so you can add one donation to your cart. If logged in as a superuser, there are edit and delete options for each item.

- Single Antiquity View
Here the user can see the antiquities information, including a 4-image carousel of photos, value, name, date and category. If the user is logged in, they also get a description. If not, there is a link instead to either login or register for the site. THere is a quantity input field so users can donate more than once for the same antiquity. The edit and delete options for superusers also appear here. 

#### **Bag App**

This page has two main sections: a Shopping Cart Detail section, with image, name, quantity and value of each item; a Cart Total section with a list of cultures supported, number of items and the total donation. Quantity can be changed for each item here, and the edit and delete options for supperusers appear again. The two sections appear side by side on larger resolutions, and with the cart detail above the cart total section on smaller resolutions.

#### **Checkout App**

Similar to the Bag App, this page has two main sections: Chosen Donations section, where the user's order is detailed once more (but without the update, edit or delete options); Checkout Information section, where the user inputs their billing info and credit card details before checking out. The credit card section is linked to and enabled by **Stripe**. The form needs to be fully validated before submission. As with the Bag App, the two sections appear side by side on larger resolutions, and above one another on smaller resolutions.

#### **Profiles App**

Once again this page has two main sections: Default Billing Information where the billing information the user has used for previous orders appears and can be updated; the Checkout information section, where each previous order appears with its order number, date, item name x quantity, and order total information visible. The user can click through via a link on the order number to the full details of the original order in the **Order History** view As with the last two apps above, the two sections appear side by side on larger resolutions, and above one another on smaller resolutions.

### **Future Features**

* **Pagination**  

    The **Amado** template comes with pagination elements builtin, so it would be easy to add pagination as a future feature on the **All Antiquities** page.

* **Sorting by Date through Age Field addition to 'antiquities.json'**  

    Users can already sort by alphabetical order ascending and descending, as well as value of item ascending and descending. However, date is stored as a string in the 'antiquities.json' fixture, as it needs to use the **AD** and **BC** suffixes. A possible futreu addition to site would be to calculate the real-time age of each feature from the current year, add a field in the model that gives each antiquity its own **Age** value, and then sort through this field both ascending and descending.

* **Full Subscription Service linked to Django ADmin backend**  

    The **Sunscription Link** that appears in the 'base.html' at the bottom of every page is currently enabled by **EmailJS**. In future, the emails could be linked to the Django backend, enabling the admin superusers to deal with them in the admin login.

* **Extra Information Wikipedia link available on Single Antiquities detail view upon login**  

    The item description on the **Single Antiquity** page is only viewable if you are a registered and logged in user of the site. A possible future feature would be to expand upon this, offering a longer description along with a link to the items **Wikipedia** page upon logging in.

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

[**AWS**](https://aws.amazon.com/) - The site was deployed live on **Amazon Web Services** was used to store the media and static files for the Heroku enabled live version of the site.

### **Other Technologies**
 
[**Django**](https://www.djangoproject.com/) - This is a fullstack site which uses the **Django** fullstack framework.

[**Postgres**](https://www.postgresql.org/) - This project's live relational database was ennabled by the open-source **Postgres** database.

[**VSCode**](https://code.visualstudio.com) - All code for this site (including this README file), and all **Github** versioning of this code, was done with **VSCode**.

[**Bootstrap**](https://getbootstrap.com) - The site was built using **Bootstrap's** grid system (**Bootstrap 4.5.0**).

[**Colorlib**](https://colorlib.com/) - I sourced my website template from this site.

### **Design**

[**Adobe XD**](https://www.adobe.com/ie/products/xd.html) - The wireframes for this site were designed in **Adobe XD**.

[**DBDiagram**](https://dbdiagram.io/) - The database schema for this site was designed with **DBDiagram**.

[**Photoshop**](httpshttps://en.wikipedia.org/wiki/Adobe_Photoshopwww.gimp.org/) - I used **Photoshop** to edit all images, the **Favicon** and the site **Logo**.

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

There are multiple **Media Query** resolution denominations in the templates css files, and I have several in my own [**CSS**](static/css/style.css) code also. Every imaginable variation, from the smallest phone to the largest 4K monitor, was used to test the responsivity of the site. There are multiple elements being targeted and styled within several **Media Queries**.

### **Validation**

* [**HTML Code Checker**](https://validator.w3.org) - I checked my HTML with the **W3C Markup Validation Service**. All errors were caused by the validator having difficulty with Django template code. It received the following messages:

  - Several "Error: Bad value for attribute href on element link: Illegal character in path segment: { is not allowed" warnings, for Django template language code across HTML documents in all Apps.

  - Several "Error: Text not allowed in element ul in this context" errors, once again due to Django template code.

  - The '{% load static %} code at the top of 'base.html' was the cause of these errors:
    - "Error: Element head is missing a required instance of child element title".
    - "Error: Stray doctype"
    - "Error: Stray start tag html"
    - "Fatal Error: Cannot recover after last error. Any further errors will be ignored."

  - A "Warning: Consider adding a lang attribute to the html start tag to declare the language of this document" for each template besides base.html.

  - An "Error: End of file seen without seeing a doctype first. Expected ! DOCTYPE html" for each template besides base.html.

  - An "Error: Element head is missing a required instance of child element title" for each template besides base.html.

  - Several "Error: Misplaced non-space characters inside a table" errors for Django 'if' loops.

  - Several "Error: Bad character = after <. Probable cause: Unescaped <. Try escaping it as &lt;" errors for template language loop counters.

  - Several "Error: Text not allowed in element ol in this context" messages for template language in ordered lists.
  
* [**CSS Code Checker**](https://jigsaw.w3.org/css-validator) - I checked my CSS with the **W3C CSS Validation Service**. It received the following messages for vendor prefixes unknown to the validator:

  - Core-style.css: Received several messages for vendor prefixes unknown to the validator, and for importing style sheets at the top of the CSS document.

  - Nice-select.css: Received several messages for vendor prefixes unknown to the validator.

  - Owl-carousel.css: Received several messages for vendor prefixes unknown to the validator.

  - style.css: Received a "Congratulations! No Error Found" message.

* [**CSS Auto-prefixer**](https://autoprefixer.github.io) - The **CSS Online Auto-prefixer** provided a **Vendor Prefix** check for my code. I added all suggestions to my CSS.

* [**Javascript Code Checker**](https://jshint.com/) - I checked my JavaScript **JS Hint**. It received the following messages:

  - Active.js: Two undefined variables (WOW and jQuery)

  - Map-active.js: One undefined variables (Google)

  - SendEmail.js: Two undefined variables (emailjs and swal)

* [**ARIA Checker**](http://wave.webaim.org/) - I used **Wave** (Web Accessibility Evaluation Tool) to check that my code was accessible to all users.  It received the following messages:

  - Several Errors referring to "Missing Empty Links", which are in fact Django template code links.

  - Several Contrast Errors (Mainly referring to the the gold Amado-btn or gold on white backgrounds)

  - Several Possible Heading Errors (Referring to the name of each antiquity in the All Antiquities view, which is not a heading.)

  - Several messages about redundant links regarding links which are legitimate.

  - Alerts for missing form labels.

### **User Scenarios**

#### **Unauthenticated user looking to browse antiquities**

1. Go to the **Main Page**.
2. Click on the **Navbar** link to **All Antiquities** to the left of the page.

#### **Unauthenticated user looking to make a donation**

1. Go to the **Main Page**.
2. Click on the **Navbar** link to **All Antiquities** to the left of the page.
3. Select some Antiquities to donate too, either by clicking the cart iocon on a particular item, or clicking to view the antiquity's details in the **Single Antiquity** view and choosing a quantity of donations.
4. Select either the **Cart** option or the cart icon in the navbar.
5. On the **Cart** page review the order and then select **Checkout**.
5. Enter billing and credit card information and select donate.

#### **Unauthenticated user trying to register for an account**

1. Go to the **Main Page**.
2. Click on the **Register** button to the left of the page.
3. Enter registration details and select **Sign Up**.
4. Find the confirmation email in your inbox.
5. Go to the link and select confirm email.

#### **Authenticated user trying to login**

1. Go to the **Main Page**.
2. Click on the **Login** button to the left of the page.
3. Enter login details and select **Sign In**.

#### **Authenticated user trying to view profile information**

1. Go to the **Main Page**.
2. Click on the **Login** button to the left of the page.
3. Enter login details and select the **My Profile** button to the left of page.

#### **Site administrator looking to view backend information**

1. Go to the **Main Page**.
2. Add '/admin' to the end of the url in the browser.
3. Enter admin login details.

#### **Site administrator trying to add an antiquity**

1. Go to the **Main Page**.
2. Click on the **Login** button to the left of the page and login as a superuser.
3. Select the **Add Antiquity** button to the left of page.
4. Add the items details and select **Save**.

#### **Site administrator trying to edit an antiquity**

1. Go to the **Main Page**.
2. Click on the **Login** button to the left of the page and login as a superuser.
3. Go to the **All Antiquities** page and select an item to edit, either by the links on the **All Antiquities** page or on the **Single Antiquity** details page.
4. Edit the items details and select **Save**.

### **Oustanding Bugs**

#### Original Template JQuery and Bootstrap JS Files

- The original JS effects that came with the template files used an earlier version of JQuery. This meant that Bootstraps Toasts did not work. I used a CDN link to get th latest version of JQuery and the Bootstrap js links. This meant that the older functions in the template JS did not work on the **Latest Options** page. Instead, I used Bootstrap responsive classes to style the page so it had the same effect, iterating through the latest options json and creating an element for each.

#### iPhone Scrolling Issue

- On iPhones there is an issue with scrolling on the **Cart** screen. The screen would only scroll down when the user started swiping below the Shopping Cart heading. This was not seen on any other device.

#### Stripe JS Browser Console Errors

- Upon load in of the site there are three Stripe JS errors each time; these are with regard to fonts that Stripe uses (message= "Refused to load the font 'https://js.stripe.com/fonts/ProximaNova-Regular.otf' because it violates the following Content Security Policy directive: "font-src 'none'".") This does not seem to effect performance or the functionality of the site in any way.

#### Failed bootstrap.min.css SourceMap Load

- Upon load of site this error appears in the browser console: "DevTools failed to load SourceMap: Could not load content for http://127.0.0.1:8000/static/css/bootstrap.min.css.map: HTTP error: status code 404, net::ERR_HTTP_RESPONSE_CODE_FAILURE". I supplied a CDN link to the Bootstrap CSS and this error does not seem to cause any issues with the site.

___

## **Deployment**

### **Local**

* This project is deployed live on [**Heroku**](https://pq-the-philanthropist.herokuapp.com/).

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

* **Amado Template**  

The template used to create the site.

- Source: https://colorlib.com/wp/template/amado/
- Preview Site: https://colorlib.com/preview/#amado

* **Boutique Ado**

I learned so much while creating the above Code Institute mini-project. The HTML and CSS in The Philanthropist are largely my own dissection of the Amado template code into the various Django apps, but for the python needed to get such a complex site up and running I had to lean heavily on what I had learning in the Fullstack Frameworks and Django Module. I would like to acknowledge that here and give credit where credit is due.

### **Images Used**

All rights for the images used lies with their respective owners. Images used here for illustrative purposes only in the context of this academic project. Any future professional deployment of the site will use only my own assets.

* Several images were sourced from [**Pinterest**](https://www.pinterest.ie/).
* Several images were sourced from the [**Museum of Ireland**](https://www.museum.ie/en-IE/home) website.
* Several images were sourced from the [**British Museum**](https://www.britishmuseum.org/) website.
* Several images were sourced from the [**BBC**](https://www.bbc.com/) website.

### **Acknowledgements**

* I would like to acknowledge all the archaeologists I have worked besides over the years, and all those who strive to keep our cultural and archaeological heritage safe and available for the next generation.