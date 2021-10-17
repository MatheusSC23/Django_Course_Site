# Django Meetup Page

> Status: Developing


### This repository is dedicated to the study of the Django framework, it was used the idea to build a web applications where it's possible to list the meetups that a person has and see its description.

## The models of the project are:
+ Meetup
+ Location
+ Participant

## The main model of this project is Meetup and its fields are:
+ title
+ slug 
+ organizer_email
+ date
+ description
+ image
+ location
+ participants 

## The Locations model has the following fields:
+ name
+ address

## The Participant model has the following field:
+ email

## Completed features:
+ In the admin page it is possible to create meetups. 
+ It's possible to vizualise the image upload in each meetup.
+ It was created a database to store, Meetups, Participants and Locations.
+ It's possible to view more details abou a meetup, see the organizer's email and subscribe a new participant at the meetup by passing the participant's email.

## Features in developing:
+ Make a CRUD to the meetups.


## Technologies used:
<table>
  <tr>
    <td>Django</td>
    <td>Python</td>
  </tr>
  
  <tr>
    <td>3.2.8</td>
    <td>3.9.7</td>
  </tr>
</table>




