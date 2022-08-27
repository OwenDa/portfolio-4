# Opera Ireland  
*Opera Ireland* is a portfolio site with social networking features for performers, service providers and other professionals working in the operatic field on the island of Ireland.
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661344463/static/images/readme/responsive-profile_1_kjw3kj.png" alt="Opera Ireland users can personalise their profiles to display their professional academic achievements, alongside links to other platforms and their latest posts" width="75%" height="auto">

## Contents
1. [Problem Statement](#problem-statement)  
2. [User Stories](#user-stories)
3. [Tech Stack](#tech-stack)  
4. [Design Statement](#design-statement)
5. [Features](#features)
    + [Future Features](#future-features)
6. [Testing](#testing)
7. [Deployment](#deployment)  
8. [Known Bugs](#known-bugs)
9. [Acknowledgements](#acknowledgements)  
  
## Problem Statement  
A niche industry, the operatic community in Ireland currently has no dedicated portfolio display site or central social network.

Opera Ireland provides the user with a unique profile page and url to display a timeline of their professional and academic achievements, as well sharing links to their online presence elsewhere, such a professional website, Youtube channel, social media profiles and so on. In addition, the site has many features associated with social networking, such as the ability to view posts from other users in one feed, displaying the latest posts first.

While many future features may yet be implemented, the general design could also be implemented to serve other niche communities with only minor adaptations.
   
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661303645/static/images/readme/about-image_1_vqj6mp.jpg" alt="Opera Ireland users can create and view posts, personalise their profiles and display their professional academic achievements" width="75%" height="auto">
   
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

These functions should also be available to users employing a screen reader. See [Accessibility Testing](#accessibility-testing).


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

User Stories and EPICs can be viewed in more detail on [the project's GitHub Project Board](https://github.com/OwenDa/portfolio-4/issues/).
  
## Tech Stack  
1. Languages
  + HTML
  + CSS
  + Javascript
  + Python
  + Django's Template Language (similar to Jinja2)
  + DBML (used only for [database model diagram below]())

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
  
Wireframe sketches were drawn up in Balsamiq. These reflect basic layout considerations rather than aesthetics.

*Profile Page Wireframe*
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661369932/static/images/readme/New_Wireframe_1_copy_2_w8lxso.png" alt="Colourful wireframe demonstrating the intended layout of the Profile page." width="75%" height="auto">

*Post Feed Wireframe*
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661369932/static/images/readme/New_Wireframe_1_copy_k286tk.png" alt="Colourful wireframe demonstrating the intended layout of the Profile page." width="75%" height="auto">

*Settings Page Wireframe*
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661369932/static/images/readme/New_Wireframe_1_copy_3_nyv3mw.png" alt="Colourful wireframe demonstrating the intended layout of the Profile page." width="75%" height="auto">

*Sign Up & Sign In Pages Wireframe*
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661369932/static/images/readme/New_Wireframe_1_cjf6yn.png" alt="Colourful wireframe demonstrating the intended layout of the Profile page." width="75%" height="auto">

### Database Structure
The diagram below demonstrates the relationships between the project's models (database tables). This was written in DBML (Database Markup Language) with the aid of [dbdiagram.io](https://dbdiagram.io/docs) which provides some useful animations that lend additional context to the diagram. Click the image below to view the animated version in a new tab:

<a href="https://dbdiagram.io/d/6307eb52f1a9b01b0fe647c5" target=_blank aria-label="Click to open Entity Relationship Diagram in more detail"><img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661468780/static/images/readme/opera-ireland-erd_hp5zzl.png" alt="Entity Relationship Diagram for the Opera Ireland site as of August 2022." width="100%" height="auto"></a>

<details><summary>Click to view as DBML code</summary>

```
  //// -- ERD for Opera Ireland
  //// -- opera-ireland.herokuapp.com

  //// -- This is a learning project created by:
  //// -- https://github.com/OwenDa/portfolio-4


  Table django_contrib_auth_models.User {
    username varchar
    // One-to-one relationship with Profile.user
    password hash
    is_staff boolean
    is_active boolean
    is_superuse boolean
    last_login datetime
    date_joined datetime
      Indexes {
      (username) [pk]
      }
  }


  Table models.Profile {
      user varchar
      // One-to-one relationship with django's User.username
      // One-to-many relationships with SocialLink, HistoryItem and Post.
      first_name varchar
      last_name varchar
      id_user int
      bio text
      location varchar
      avatar image
      role varchar
  }

      
  Table models.SocialLink {
      user varchar
      // Many-to-one from this view point.
      link url
      site_name varchar
  }


  Table models.HistoryItem {
      user varchar
      // Many-to-one from this viewpoint.
      history_heading varchar
      history_details varchar
      history_role varchar
      year int
  }


  Table models.Post {
      id UUID [pk]
      user varchar
      // Many-to-one from this viewpoint.
      post_image image
      post_text text
      created_at datetime
      no_of_applause int
  }


  Table models.PostApplause {
      post_id varchar
      username varchar
  }


  Ref: django_contrib_auth_models.User.username - models.Profile.user
  Ref: models.Profile.user < models.SocialLink.user
  Ref: models.Profile.user < models.HistoryItem.user
  Ref: models.Profile.user < models.Post.user
  Ref: models.PostApplause.post_id - models.Post.id
  ```

</details>

    
## Features  

### Responsive Design

Opera Ireland is fully responsive and can be enjoyed on a wide range of devices. The site and its content will adapt to create the best user experience.

<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661344463/static/images/readme/responsive-profile_1_kjw3kj.png" alt="Fully responsive profile page shown on screen emulators of varying sizes" width="75%" height="auto">

### Sign In & Sign Up

<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661348018/static/images/readme/signup-responsive_1_qwogw1.png" alt="Fully responsive sign up page shown on screen emulators of varying sizes" width="75%" height="auto">  

Users can sign up to create an individual profile and access full site features. When signing up, the user is asked to create a username and informed that this will form part of their unique profile url.

After signing up for the first time, the user is directed to their settings page, allowing them to customise their profile. After this initial log-in, all future log-ins will direct the user to the index page which houses the main post feed.

<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661344459/static/images/readme/responsive-signin_1_szsqvt.png" alt="Fully responsive sign in page shown on screen emulators of varying sizes" width="75%" height="auto">  

### Post Feed

<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661343875/static/images/readme/screencapture-opera-ireland-herokuapp-2022-08-24-13_20_28-min_dqur7x.png" alt="Screenshot displaying the post feed populated with example posts from multiple example users." width="75%" height="auto">  

This feed is not curated and the site does not implement a "Follow" feature. This is an intentional omission and the feature is not likely to be added in the future. A niche community on a small island, the developer decided to take forum-like approach to the post feed, rather than the conventional curated approach used in most social networks. In the realm of social networks, this is similar to [Mastadon](https://joinmastodon.org/), for example, in which users of a particular instance can view feed which includes _all_ posts within that instance. [Mastadon](https://joinmastodon.org/) instances are, however, designed for those who already share an interest of some sort and can therefore be considered pre-curated, in a manner. This is the approach taken by Opera Ireland and for the very same reasons. An added benefit of this approach is that is encourages users to see and interact with posts from those whose work they may not already know or be familiar with.

While individual profiles can be viewed without logging in (allowing the user to harness their profile link as a promotional tool), the post feed and other site features require the user to have created an account and be logged in. This is intended is intended to strike a balance between promotion and keeping the site's features and content limited to its registered users.

### Profile

<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661341218/static/images/readme/screencapture-opera-ireland-herokuapp-profile-user4-2022-08-24-01_38_54_1_cgidxm.png" alt="Opera Ireland users can personalise their profiles to display their professional academic achievements, alongside links to other platforms and their latest posts" width="75%" height="auto">
  
The profile contains user-specific information which can be customised from the user's settings page, as well as the option to add a timeline of professional and academic achievements.

#### Example Profiles:
-	[User1](https://opera-ireland.herokuapp.com/profile/user1)
-	[User2](https://opera-ireland.herokuapp.com/profile/user2)
-	[User3](https://opera-ireland.herokuapp.com/profile/user3) 
-	[User4](https://opera-ireland.herokuapp.com/profile/user4)
-	[User5](https://opera-ireland.herokuapp.com/profile/user5) 

As can be seen from these example users, profile features include displaying basic user information, user posts, professional history timeline and links to other sites such as social media 

Profiles are rendered differently according to whether the viewer is the profile-owner or not. For example, only profile owners can see controls to add/edit history items. Similarly, prior to profile customisation, the profile owner will see prompts to complete their profile, while other users see only empty or blank fields.

<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661345428/static/images/readme/user3-differing-views_1_stv5s2.png" alt="Comparison of profile-owner versus profile-viewer renderings of an incomplete profile" width="100%" height="auto">  
  
### Settings
  
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661346664/static/images/readme/profile-settingsview_1_b2oicf.png" alt="Profile settings page completed and incomplete." width="100%" height="auto">  
  
The user can customise their profile from their Settings page. Login is required for this feature as each settings page is related to its owners profile.

Two forms are included, one for basic profile details such as first and last name, avatar, bio, location and so on. This form also features a reminder to the user of their personal url (/profile/username). The second form allows the user to add or remove external links.

### Applause (Like Post)
   
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661347224/static/images/readme/like-post_1_jossed.png" alt="Example post with 1 applause." width="75%" height="auto">  
  
Emulating the popular "Like" feature found in many such sites, Opera Ireland users can show appreciation for posts with the "applause" feature. Should the user change their mind, clicking or tapping the applause icon again will "unlike" the post.

### Create Post
  
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661347000/static/images/readme/newpost_1_v2q7lb.png" alt="Create new post modal form" width="75%" height="auto">  
  
A logged-in user can create a new post from any page on the site, using the "New Post" option on the navigation bar. Posts can feature text (required) and one image (optional). Should the user change their mind, this dialog can simply be closed.

Once published, posts feature the post content, the author's avatar, full name if saved to their profile and username, all of which link to the author's profile. In addition, an "applause" icon and "applause" counter are shown. Where the viewer is the logged in user, posts also feature a Delete Post option.

### Additional Features
In addition, the site uses custom 404 and 500 handlers to present the user with a UI in keeping with the rest of the site (avoiding causing undue alarm or disorientation) and a link to return 'Home'. This is a link leads the logged-user to the post feed (index) and the logged-out user to the sign-in page.  
  
To reduce resource-wasting and potentially harmful bot traffic, the site's admin url has been customised.
  
### Future Features  
In future, it would be ideal to add a search function which allows logged-in users to search for others by username or by role-type. It is with this latter function in mind that "role" must be chosen from a list rather than allowing user's to type freely; the aim is to generate more accurate results when the user searches for all profiles with the role-type "Soprano" for instance.

Comments could be added to posts, allowing for a more social and conversational interaction.

An additional account type, that of "Venue" could be added, allowing operatic venues to promote related events on the site.

Significant improvements might be made by allowing users to add ALT text to their own images, and some aspects of styling warrant further revision at a later stage.
  
## Testing  
### Manual Testing  
In large part, testing was carried out manually through the development process, checking that each function worked as expected and checking whether various user behaviours or choices were appropriately handled.  

`python3 manage.py check --deploy` was also run.
  
Click to expand and view latest test case results per module:  
  
<details><summary>
URLs
</summary></br>  
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661351122/static/images/readme/test-cases/test-urls-min_ivio42.jpg" alt="Test case table or tables." width="75%" height="auto"> 
</details>
  
<details><summary>
Sign in screen
</summary></br>  
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661351122/static/images/readme/test-cases/test-sign-in-min_v0zpuj.jpg" alt="Test case table or tables." width="75%" height="auto"> 
</details>
  
<details><summary>
Sign up screen
</summary></br>  
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661351122/static/images/readme/test-cases/test-sign-up-min_c3wyxt.jpg" alt="Test case table or tables." width="75%" height="auto">
</details>
  
<details><summary>
Navigation
</summary></br>
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661351122/static/images/readme/test-cases/test-navigation-min_zstzti.jpg" alt="Test case table or tables." width="75%" height="auto">
</details>
  
<details><summary>
New Post modal
</summary></br>
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661351122/static/images/readme/test-cases/test-new-post-modal-min_nnpkqv.jpg" alt="Test case table or tables." width="75%" height="auto"> 
</details>
  
<details><summary>
Post Feed
</summary></br>
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661351122/static/images/readme/test-cases/test-post-feed-min_sza7a9.jpg" alt="Test case table or tables." width="75%" height="auto"> 
</details>
  
<details><summary>
Posts
</summary></br>
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661351122/static/images/readme/test-cases/test-posts-min_rbw5k8.jpg" alt="Test case table or tables." width="75%" height="auto"> 
</details>
  
<details><summary>
Settings screen
</summary></br>
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661351122/static/images/readme/test-cases/test-settings-screen-min_qrmmgv.jpg" alt="Test case table or tables." width="75%" height="auto"> 
</details>
  
<details><summary>
Profile screen
</summary></br>
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661351122/static/images/readme/test-cases/test-profile-screen-min_kpfuie.jpg" alt="Test case table or tables." width="75%" height="auto"> 
</details>
  
<details><summary>
Other
</summary></br>
<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661351122/static/images/readme/test-cases/test-other-min_f5pihr.jpg" alt="Test case table or tables." width="75%" height="auto"> 
</details> 
  
  
### Accessibility Testing
For testing the contrast level of the various background and font colours used, [Coolers.co](https://coolors.co/contrast-checker) was employed. The primary accent colour was found to possess good contrast at all sizes, while the secondary accent colour was found unsuitable for small text and better suited to larger text. This colour is used to highlight links throughout the site, most of which are large headings. 

The developer manually tested to ensure that all features can be navigated via keyboard.

NVDA, a freely available screen reader, was used to test for the screen reader functions. The following User Story formed the basis of these tests. As can be seen, one sub-task remains unfulfilled and led to the addition of user-created ALT text as a [Future Feature](#future-features).

> As a **user employing a screenreader such as NVDA**, I can **successfully navigate the site** in order to **enjoy and make use of its content**.
>
> Acceptance Criteria: Functional navigation and/or use of:
> 
> - [x] Sign in page content, links, inputs and alerts
> - [x] Sign up page content, links, inputs and alerts
> - [x] Index page (Post Feed) content, links, inputs and alerts
>  + [ ] User-uploaded images (see future features)
> - [x] New Post modal inputs, prompts and functions
> - [x] Settings content, links, inputs, alerts and functions
> - [x] Profile page content, links, alerts and functions
> - [x] Navigation, as checked in previous tests
  
  
### Validators & Tools 

JavaScript code was run through [jsvalidator.com](https://jsvalidator.com/) with no errors or warnings.  
  
Both CSS and HTML were validated through the W3C's official validators. There were no errors in the CSS and the only warnings present were identifying vendor extensions added via [Autoprefixer](https://css-tricks.com/autoprefixer/) to improve browser compatibility, along with a reminder that CSS variables are not currently checked by the service.  

<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS icon provided by the CSS Validator" />
    </a>
</p>  
  
HTML was largely found valid; however, the use of Django's template language within the HTML markup language does cause some issues in validation. In the case of the base.html file, the initial template tags which precede DOCTYPE must first be removed as these cause an error which will prevent a full and complete check of the document. Similarly, template tag symbols such as `{` and `}`cause Bad Value errors; however, these are essentially not HTML and cannot be assessed as such. These errors can therefore be ignored.

The developer also reviewed any warnings concerning accessibility issues (namely, regarding decorative images) and judged the code to be acceptable as it stands.
   
[Google's Lighthouse tool](https://developers.google.com/web/tools/lighthouse) in Chrome's Dev tools was used to generate scores on Performance, Accessibility, Best Practices and SEO.

Some aspects of the site hinder this score, such as non-unique aria-ids on posts; however, this is caused by multiple posts being rendered from a single template. Similarly, decorative images have empty alt tags but do make use of aria-label and aria-labelledby where logical.

<img src="https://res.cloudinary.com/cloud9wastaken/image/upload/v1661351122/static/images/readme/mobile-signin-lighthouse_tddzoy.png"
 alt="Google's Lighthouse scores  for mobile view of signing page: Performance 69, Accessibility 97, Best Practice 92, SEO 91." width="50%" height="auto">  
  
Significant improvements might be made by allowing users to add ALT text to their own images, and certain heading-levels should be revised.
  
## Deployment  
<details><summary>
Click to Expand: Deployment Procedure
</summary></br>  
  
### Heroku  
The site was deployed to Heroku using the following procedure. Before beginning, ensure that requirements.txt is up to date.  
  
Similarly, ensure that ``DEBUG = False` in settings.py, and the developer also suggests running `$ python3 manage.py check --deploy` before deployment.
  
1. An account must first be created on [Heroku.com](https://www.heroku.com/)  
2. Once logged in, select "Create new app".  
3. The app must then be given a unique name and the developer's region must be selected from a list of options.  
4. From the Settings tab of the next screen, select "Reveal config vars".  
5. A Cloudinary url, database url, port and secret key are required config vars which can be added in the Heroku project settings.
6. Within the deploy section, select GitHub as the deployment method and authorise.
7. Input the name of the GitHub repository and click "Search", followed by "Connect".  
8. Choose either "Automatic deploys" or "Manual deploy". In this case, the developer opted for manual deploy for the initial deployment and, having verified that deployment was successful, enabled automatic deploys thereafter.  
9. Select the appropriate branch from which to deploy (in this case, the project had only the Main branch at the time of deployment).


### Forking & Cloning Repositories  
Forking a repository allows one to make a copy with which to experiment without affecting or jeopardising the original. This does not require any special permissions from or direct contact with the original developer provided the repository in question is public rather than private. You may wish to do this either to experiment with and learn from another party's code or aid in improving an open-source project by offering changes (note that forking is distinct from [branching](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)). To do this, one must have a GitHub account and be logged in. Then, simply visit the main page of the repository in question, and select the "Fork" option located in the upper-right corner (desktop) as shown in the image below. [Learn more about forks from GitHub Docs](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository).  

Forking a repository does not create locally-stored copies of its files on your computer. To achieve this, you will also need to Clone the repository. For example, you may wish to do this if you wish to have a functioning copy of another party's code in under to compile and execute it locally. Cloning options are found under the "Code" drop-down button of a repository's main page, as shown in the image below. [Learn more about cloning from GitHub Docs](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository).  
</details>  

## Known Bugs
1. New Post File Upload:  
The text content of new posts containing inappropriate file types (e.g. PDF) is published; the invalid file is not published; however, there is no specific feedback to the user concerning this issue. Video files may cause Error 500. The field is clearly marked for images; however, appropriate feedback would be useful.  
  
2. Exceedingly long file names can cause an error.

## Acknowledgements 
1. Screenshot images were compressed with [TinyPNG.com](https://tinypng.com/)
2. Large credit is due to [this tutorial](https://youtu.be/xSUm6iMtREA), however much the end-result of the project may differ from the examples shown.
3. Equally, [Code Institute](https://codeinstitute.net)'s Django tutorials are owed significant credit.
4. [Coolers.co](https://coolors.co) was used as described in the [Design Statement](#design-statement).
6. [Stack Overflow](https://stackoverflow.com/) was consulted several times in troubleshooting, but special thanks is owed to user [SamSparkx](https://stackoverflow.com/users/18799377/samsparx) for assistance given in answer to [this question](https://stackoverflow.com/questions/73439361/how-do-i-access-objects-user-info-across-django-models-foreign-key-beginner/73440194#73440194).
7. As indicated by the automatically generated credit preserved in the CSS file, the CSS code was prefixed by Autoprefixer.
 8. Bootstrap's excellent documentation was consulted, for example in the construction of an [alert dismiss button](https://getbootstrap.com/docs/4.0/components/alerts/#dismissing "https://getbootstrap.com/docs/4.0/components/alerts/#dismissing").
 9. [i.dev/amiresponsive](https://i.dev/amiresponsive) was used for screenshots to demonstrate responsiveness (note that an extension such as "Ignore X-Frame headers" is required to view this project in its current deployment).
 10. Most images were drawn from [Pexels.com](https://www.pexels.com/).
 11. [dbdiagram.io](https://dbdiagram.io/docs) was used to create the [ERD above](#database-structure).
 12. Credit to [Stackoverflow thread](https://stackoverflow.com/questions/17662928/
    django-creating-a-custom-500-404-error-page) for insight on the creation of 404 and 500 handler functions.
 
### Image Credits:
1. ["Áine Murphy" profile avatar (user1)](https://www.pexels.com/photo/smiling-woman-wearing-earrings-and-black-collared-top-1197132/ "https://www.pexels.com/photo/smiling-woman-wearing-earrings-and-black-collared-top-1197132/"): Photo by Anderson Guerra:  
2. ["John Lansbury" profile avatar (user2)](https://www.pexels.com/photo/a-man-singing-emotionally-8043761/ "https://www.pexels.com/photo/a-man-singing-emotionally-8043761/"). Photo by ANTONI SHKRABA.
3. [Microphone user2 post photo](https://www.pexels.com/photo/tilt-shift-photograph-of-gray-and-black-microphone-164879/ "https://www.pexels.com/photo/tilt-shift-photograph-of-gray-and-black-microphone-164879/"). Photo by Pixabay.
4.  [Microphone image as user4 avatar](https://www.pexels.com/photo/hand-metal-music-musician-33779/). Photo by Pixabay.
5.  ['Warm up' post image](https://www.pexels.com/photo/football-speedladder-warmup-13204962). Photo by Chris K.
6.  ['As One' post image (user1)](https://www.flickr.com/photos/americanoperaprojects/43971649681).
7.  [User5's avatar](https://www.pinterest.com/pin/171840542002547471) as listed under Creative Commons licence with attribution already printed within the image itself and [additional link to source here](http://aroundtheworldwithirina.blogspot.com).
8.  [User5 post (most expensive dress)](https://www.npg.org.uk/collections/search/use-this-image/?mkey=mw257493):  Adelina Patti as Violetta in 'La Traviata'; as Lucia in 'Lucia de Lammermoor'; as herself; as Martha in 'Martha'; as Zerlina in 'Don Juan'
by Ashford Brothers & Co, after Camille Silvy albumen carte-de-visite, circa 1861 3 7/8 in. x 2 1/2 in. (98 mm x 63 mm) overall Given by Terence Pepper, 2014.
Licence obtained from Rights and Images Department National Portrait Gallery, London.
9.  [Shouting man image (user2 post)](https://www.flickr.com/photos/ter-burg/8127283172).
10. [Woman with loudspeak image (user1 post)](https://www.pexels.com/photo/young-woman-with-a-megaphone-3851253/). Photo by Pressmaster.

