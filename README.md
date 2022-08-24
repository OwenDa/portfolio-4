# Opera Ireland  
*Opera Ireland* is a portfolio site with social networking features for performers, service providers and other professionals working in the operatic field on the island of Ireland.
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661344459/static/images/responsive-profile_1_kjw3kj.png" alt="Opera Ireland users can personalise their profiles to display their professional academic achievements, alongside links to other platforms and their latest posts" width="75%" height="auto">

## Contents
1. [Problem Statement](#problem-statement)  
2. [User Stories](#user-stories)
3. [Tech Stack](#tech-stack)  
4. [Design Statement](#design-statement)
5. [Features](#features)
    + [Future Features](#future-features)
6. [Testing](#testing)
7. [Deployment](#deployment)  
8. [Acknowledgements](#acknowledgements)  
  
## Problem Statement  
A niche industry, the operatic community in Ireland currently has no dedicated portfolio display site or central social network.

Opera Ireland provides the user with a unique profile page and url to display a timeline of their professional and academic achievements, as well sharing links to their online presence elsewhere, such a professional website, Youtube channel, social media profiles and so on. In addition, the site has many features associated with social networking, such as the ability to view posts from other users in one feed, displaying the latest posts first.

While many future features may yet be implemented, the general design could also be implemented to serve other niche communities with only minor adaptations.
  
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661303645/static/images/about-image_1_vqj6mp.jpg" alt="Opera Ireland users can create and view posts, personalise their profiles and display their professional academic achievements" width="75%" height="auto">
  
## User Stories  
  **Types of User** 
  + Vocal Performers 
  + Non-vocal performers
  + Non-performing theatrical professionals such as directors
  + Non-performing service providers such as vocal coaches
   
   While each user may differ in their work, their interaction with the site is not dissimilar in terms of basic functionality:
   
  **As a site user, I can...** 
  + register an account in order to create a profile and use the site's functions.
  + log in in order to access the full site and my own account.
  + log out in order to access prevent others using my account without permission.
  + edit details within my profile so that it can function as an accurate, up-to-date CV or portfolio for others to see (see [Epic](#epic-user-profile)).
  + add a new post in order to promote myself or others, and add to the site content.
  + view another user’s profile in order to get an overview of their portfolio to-date.
  + 

### Epic: User Profile
**Primary Features:**  
_Acceptance Criteria:_
Within my own unique profile, I can...
-   Add my name
-   Edit my name
-   Add a 'Bio' to display a brief introductory text about myself
-   Edit Bio to keep it up to date
-   Add Avatar so that people more readily recognise me and my content.
-   Change Avatar as I please

**Secondary Features:**  

-   Add voice type (vocal performers) or other role type (non-vocal performers and non-performers) from a list in order to display it on my profile.
-   Add external links to promote their other online profiles and sites
-   Edit/Delete external links for accuracy

Tertiary features exist to be considered in later development under their own user stories and/or EPICs.
  
## Tech Stack  
1. Languages
  + HTML
  + CSS
  + Javascript
  + Python
  + Django's Template Language (similar to Jinja2)

2. Libraries & Frameworks
  + Django 3.2
  + Bootstrap 4
  + jQuery
  + Popper JS
  + FontAwesome Icons
 
2. Additional Tools
  + Balsamiq

 4. Dependencies
  + asgiref==3.5.2
  + cloudinary==1.29.0
  + dj-database-url==0.5.0
  + dj3-cloudinary-storage==0.0.6
  + Django==3.2.13
  + django-simple-pagination==1.3
  + gunicorn==20.1.0
  + oauthlib==3.2.0
  + Pillow==9.2.0
  + psycopg2==2.9.3
  + PyJWT==2.4.0
  + python3-openid==3.2.0
  + pytz==2022.1
  + requests-oauthlib==1.3.1
  + sqlparse==0.4.2
  
## Design Statement     
The site employs a simple UI, with many standard UI components already familiar to the user and little to distract from the content itself.

Bootstrap 4 was chosen, over Bootstrap 5, for use with jQuery and support IE 10 and 11.
  
Wireframe sketches were drawn up in Balsamiq.
    
## Features  

After signing up for the first time, the user is directed to their settings page, allowing them to customise their profile. After this initial log-in, all future log-ins will direct the user to the index page which houses the main post feed.

### Post Feed

<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661343875/static/images/screencapture-opera-ireland-herokuapp-2022-08-24-13_20_28-min_dqur7x.png" alt="Screenshot displaying the post feed populated with example posts from multiple example users." width="75%" height="auto">  

This feed is not curated and the site does not implement a "Follow" feature. This is an intentional omission and the feature is not likely to be added in the future. A niche community on a small island, the developer decided to take forum-like approach to the post feed, rather than the conventional curated approach used in most social networks. In the realm of social networks, this is similar to [Mastadon](https://joinmastodon.org/), for example, in which users of a particular instance can view feed which includes _all_ posts within that instance. [Mastadon](https://joinmastodon.org/) instances are, however, designed for those who already share an interest of some sort and can therefore be considered pre-curated, in a manner. This is the approach taken by Opera Ireland and for the very same reasons. An added benefit of this approach is that is encourages users to see and interact with posts from those whose work they may not already know or be familiar with.

While individual profiles can be viewed without logging in (allowing the user to harness their profile link as a promotional tool), the post feed and other site features require the user to have created an account and be logged in. This is intended is intended to strike a balance between promotion and keeping the site's features and content limited to its registered users.

### Profile

<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661341218/static/images/screencapture-opera-ireland-herokuapp-profile-user4-2022-08-24-01_38_54_1_cgidxm.png" alt="Opera Ireland users can personalise their profiles to display their professional academic achievements, alongside links to other platforms and their latest posts" width="75%" height="auto">
  
The profile contains user-specific information which can be customised from the user's settings page, as well as the option to add a timeline of professional and academic achievements.

#### Example Profiles:
-	[User1](https://opera-ireland.herokuapp.com/profile/user1)
-	[User2](https://opera-ireland.herokuapp.com/profile/user2)
-	[User3](https://opera-ireland.herokuapp.com/profile/user3) 
-	[User4](https://opera-ireland.herokuapp.com/profile/user4)
-	[User5](https://opera-ireland.herokuapp.com/profile/user5) 

Profiles are rendered differently according to whether the viewer is the profile-owner or not. For example, only profile owners can see controls to add/edit history items. Similarly, prior to profile customisation, the profile owner will see prompts to complete their profile, while other users see only empty or blank fields.

<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661345428/static/images/user3-differing-views_1_stv5s2.png" alt="Comparison of profile-owner versus profile-viewer renderings of an incomplete profile" width="75%" height="auto">  

1. https://groups.google.com/g/django-users/c/al95x1TXFV4/m/7mCCWQE3jtAJ
Year choices code (history items)

2. https://www.geeksforgeeks.org/difference-between-bootstrap-4-and-bootstrap-5/
Bootstrap 4 vs 5

3. Bootstrap Docs, for example, alert dismiss button: https://getbootstrap.com/docs/4.0/components/alerts/#dismissing

4. Special thanks to https://stackoverflow.com/users/18799377/samsparx

5. django-simple-pagination docs: https://django-simple-pagination.readthedocs.io/en/latest/index.html and pypi link: https://pypi.org/project/django-simple-pagination/


Images:
1. Photo by Anderson Guerra: https://www.pexels.com/photo/smiling-woman-wearing-earrings-and-black-collared-top-1197132/
"Áine Murphy" profile avatar (user1)
2. Photo by ANTONI SHKRABA production: https://www.pexels.com/photo/a-man-singing-emotionally-8043761/
"John Lansbury" profile avatar (user2)
3. Photo by Pixabay: https://www.pexels.com/photo/tilt-shift-photograph-of-gray-and-black-microphone-164879/
Microphone user2 post photo
4. microphone image as user4 avatar: Photo by Pixabay from Pexels: https://www.pexels.com/photo/hand-metal-music-musician-33779/
5. warm up post image Photo by Chris K: https://www.pexels.com/photo/football-speedladder-warmup-13204962/
6. As one post image (user1) from https://www.flickr.com/photos/americanoperaprojects/43971649681
7. User5's avatar is from https://www.pinterest.com/pin/171840542002547471/ listed under Creative Commons licence with attribution already printed within the image itself (link: http://aroundtheworldwithirina.blogspot.com/)
8. User5 post (most expensive dress): licence obtained from Rights and Images Department
National Portrait Gallery, London as per https://www.npg.org.uk/collections/search/use-this-image/?mkey=mw257493: Adelina Patti as Violetta in 'La Traviata'; as Lucia in 'Lucia de Lammermoor'; as herself; as Martha in 'Martha'; as Zerlina in 'Don Juan'

by Ashford Brothers & Co, after Camille Silvy
albumen carte-de-visite, circa 1861
3 7/8 in. x 2 1/2 in. (98 mm x 63 mm) overall
Given by Terence Pepper, 2014

9. Shouting man image (user2 post) from: https://www.flickr.com/photos/ter-burg/8127283172 

Notes:
Ignore X-Frame headers required to view on emulator sites like https://i.dev/amiresponsive 