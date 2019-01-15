# DeliverIT2
DeliverIT-2 is a courier service that helps users deliver parcels to different destinations. DeliverIT2 provides courier quotes based on weight categories.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Git
* Python 3.6.5
* Virtualenv

### Quick Start

1. Clone the repository

```
$ cd into the created folder
```

2. Initialize and activate a virtualenv

```
$ virtualenv venv
$ source venv/bin/activate
```

3. Install the dependencies

```
$ pip install -r requirements.txt
```

4. Initialize environment variables

```
$ export SECRET_KEY=<SECRET KEY>
```

5. Run the development server

```
$ python app.py
```

6. Navigate to [http://localhost:5000](http://localhost:5000)

At the / endpoint you should see Welcome to DeliverIT-2 API displayed in your browser.

## Endpoints

Here is a list of all endpoints in the DeliverIT-2 API

Endpoint | Functionality
------------ | -------------
POST   /api/v1/auth/userregister | Register a user
POST   /api/v1/auth/adminregister | Register an admin
POST   /api/v1/auth/login | Log in user
POST   /api/v1/parcels | Create a parcel delivery order
GET   /api/v1/parcels/id | Fetch a specific parcel order
GET   /api/v1/parcels | Fetch all parcel delivery orders
GET   /api/v1/users/id/parcels | Fetch all parcel delivery orders by a specific user
PUT   /api/v1/parcels/id/cancel | Cancel a specific parcel

## Running the tests

To run the automated tests simply run

```
nosetests tests
```

### And coding style tests

Coding styles tests are tests that ensure conformity to coding style guides. In our case, they test conformity to
PEP 8 style guides

```
pylint app.py
```

## Deployment


Ensure you use Productionconfig settings which have DEBUG set to False

## Built With

* HTML5
* CSS3
* Python 3.6.5
* Flask - The web framework used

## GitHub pages

https://kelvinziroh.github.io/

## Heroku


## Versioning

Most recent version is version 1

## Authors

Kelvin Ziro.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration and encouragement
* etc
