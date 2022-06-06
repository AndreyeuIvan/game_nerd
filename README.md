# Overview
Site for computer game lovers. Using third-party IPs, such as Twitter, Twitch. Used Django + Rest(Drf), some Js+Html, included Docker and runned on Heroku. Mainly on Bootstrap template. 

Using public API addresses, you can find a lot of interesting things on the net. This application is a synergy of several such addresses. Users get access to the world of games, with a detailed description and the latest reviews of the game.

There is a convenient system of registration and user authentication. There is the following filtering system by categories:

* platform (Xbox vs. PlayStation or PC)

* Age restriction

* genre

* the date of release

Each user can log into their personal account. Change the necessary data, such as email and personal data. Separately, there is a page with favorite games for the user, whose changes occur dynamically using Ajax requests. On the main page, the user sees a list of the first 20 games. If the user likes the game, he can press the “like” button. After that, all the games he has chosen are placed on a separate page, where he can view them separately.

The app also has its own public API address with data about games and reviews from Twitter.

The main advantage is the built-in data update capability by the administrator. He can update the game database once a day or once a week. This will keep your games and review data updated in real time.


## Table of Contents

* [Initial Django setup and first pages](./initial-setup-n-pages/readme.md)
* [Twitter and IGDB API](./twitter-igdb-api/readme.md)
* [Create Sing up, Login, User profile](./signup-n-user-profile/readme.md)
* [Create favorite games page](./favorite-games/readme.md)
* [Store games in Database, refresh periodically](./game-model-n-celery/readme.md)
* [Create REST API using DRF](./drf-rest-api/readme.md)
* [Application setup using Docker](./django-docker-setup/readme.md)

## Requirements

* Use latest Python version
* Use latest Django version
* Use virtualenv and virtualenvwrapper or any other tool for separation of working environment
* Follow PEP8 (flake8 package)
* Do not use any external libs for connecting to Twitter API or IGDB API.
* Use ES2015+ syntax for js
* Use [BEM](https://ru.bem.info/) methodology to create reusable and component-oriented CSS.
* Pay attention to keeping code clean and sticking to following principles: [separation of concerns](https://en.wikipedia.org/wiki/Separation_of_concerns), [SOLID](https://en.wikipedia.org/wiki/SOLID_(object-oriented_design)), [KISS](http://enterprisecraftsmanship.com/2015/06/15/kiss-revisited/), [YAGNI](http://enterprisecraftsmanship.com/2015/06/11/yagni-revisited/), [DRY](http://enterprisecraftsmanship.com/2015/09/11/dry-revisited/). The main goal of this exercise is to develop your skills in app architecture and code structuring.
* Styling for pages may vary, as the pictures are only mockups.
