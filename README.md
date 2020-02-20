# opening-hours
An API that takes JSON-formatted opening hours of a restaurant as an input and outputs hours in a more human readable format.

![](demo.gif)

* [How to run](#how-to-run)
* [How to run tests](#how-to-run-tests)
* [To-do list](#to-do-list)


## How to run
1. Clone this repository then go to the project's root folder.
1. Run `pipenv install` to get all the project's requirements from Pipfile.
1. Run `pipenv shell` to activate your virtual environment.
1. Start the application by running `python manage.py runserver`.
1. Access the endpoint on `http://127.0.0.1:8000/api/`. You can get and post to the endpoint directly from the web browser.
7. Enjoy! 🎉

Example payload:
```json
{
    "monday": [],
    "tuesday": [
        {"type": "open", "value": 36000},
        {"type": "close", "value": 64800}
    ],
    "wednesday": [],
    "thursday": [
        {"type": "open", "value": 36000},
        {"type": "close", "value": 64800}
    ],
    "friday": [
        {"type": "open", "value": 36000}
    ],
    "saturday": [
        {"type": "close", "value": 3600},
        {"type": "open", "value": 36000}
    ],
    "sunday": [
        {"type": "close", "value": 3600},
        {"type": "open", "value": 43200},
        {"type": "close", "value": 75600}
    ]
}
```

## How to run tests
* Tests: run command `pytest` in the project root.
* Test coverage report: run `pytest --cov=application application/tests` in the project root.


## To-do list

- [x] Write preliminary plan.
- [x] Prepare project dependencies.
- [x] Create Django project.
- [x] Create application within the project and give it the url.
- [x] Install Django REST Framework.
- [x] Write unit tests for utils to format time.
- [x] Write utils that format the time.
- [x] Write unit tests for main logic service.
- [x] Write main logic service.
- [x] Write unit tests for API Validators.
- [x] Write the API serializers and validators.
- [x] Write tests for the API View
- [x] Write integration tests.
- [x] Write the API view.
- [x] Iterate on tests/logic if needed. Make sure everything is in check.
- [x] Update README with "How To Run" section.
- [ ] Update README with reflections.
