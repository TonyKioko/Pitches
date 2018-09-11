# One Minute Pitch
#### One MInute Pitch app created as an Independent Project on 07/09/2018
#### Author: **Tony Kioko**
## Description
One minute pitch is a web application that allows users to view various pitches posted by others.
The application helps users to:
* Submit a pitch in any category.
* See the pitches other people have posted.
* To vote on the pitch they liked and give it a downvote or upvote.
* To comment on the different pitches and leave feedback.
* Receive a welcoming email once signed up.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Create user account | **Click Sign Up button** | Form to capture user details|
| Welcome email | **On sign Up** | sends welcome email to new user|
| Display pitches | **On the Home page** | Pitches posted by users displayed per category |
| Post Pitch | **Login, Select category then Pitch** | Pitch created |
| Comment on Pitch | **Click comment on Pitch**  | Comment created for that specific pitch |
| Upvote or downvote | **click upvote/downvote**  | Pitch upvotes or downvotes increases  |


## Setup/Installation Requirements.
* Git clone https://github.com/TonyKioko/Pitches or download and unzip the repository from github.
* Have python3.6 installed in your machine
* Navigate into cloned file using the termianl.
* Run python3.6 -m venv --without-pip virtual to create a virtual environment.
* Run source virtual/bin/activate to activate the above created virtual environment.
* To run the app, type ./start.sh from your virtual environment on the terminal. In your favorite browser, open the link provided by the local host.

### Live Link ###

## Technologies used ##

* Python 3.6
* Flask
* Bootstrap

## Test Driven Development
* Testing was done using python inbuild test tool called unittest


## Known Bugs 
There are no known bugs.

<!-- ## Future additional features to be considered

* Store user credentials in a database.
* Use encryption algorithims to hash saved passwords. -->
 
### License
This project is licensed under the MIT Open Source license,Copyright (c) 2018 [Tony Kioko](https://github.com/tonykioko/)