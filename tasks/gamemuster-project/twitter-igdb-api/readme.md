# Twitter and IGDB API

## Short Description

Create wrappers for Twitter API and IGDB API and implement view logic.

## Estimation (h)

40

## Topics

* Python/Django
* HTML/CSS

## Requirements

### Source of Information

#### IGDB API

The main source of information is [IGDB API](https://api.igdb.com/). We will need the following feeds:

* Get game list
* Get single game

It&#39;s free RESTful API which provides JSON data.

There is a python client for this. Using this is prohibited as you&#39;ll need to build your own wrapper.

#### Twitter API

[Twitter API](https://dev.twitter.com/rest/public) will be used for retrieving tweets by game name hashtag. So the
Search API will be used. To authenticate in this API you&#39;ll need to use your own Twitter account. If you don&#39;t
have one, you&#39;ll need to create one.

Twitter has embedded timeline functionality. Using this is strongly prohibited. You&#39;ll need to fetch API data and
render it in some way.
