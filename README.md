# opening-hours
An API that takes JSON-formatted opening hours of a restaurant as an input and outputs hours in a more human readable format.

![](demo.gif)

## Contents
* [How to run](#how-to-run)
* [How to run tests and other dev tools](#how-to-run-tests-and-other-dev-tools)
* [Thoughts and Reflections](#thoughts-and-reflections)
* [To-do list](#to-do-list)


## How to run
1. Clone this repository then go to the root directory `opening-hours/`.
1. Run `pipenv install` to get all the project's requirements from Pipfile. You need to have `pipenv` installed on your machine.
1. Run `pipenv shell` to activate your virtual environment.
1. Go to the `project/` directory and create a `.env` file to store environment variables: `touch .env`.
1. Obtain a secret key from [MiniWebTool](https://miniwebtool.com/django-secret-key-generator/).
1. Add the SECRET_KEY and the DEBUG environment variables with their values to the `.env` file as follows: 

     ```
     DEBUG=on
     SECRET_KEY='<secret_key_you_obtained_from_MiniWebTool>'
     ```

1. Go back to the root directory and run `python manage.py migrate`
1. Start the application by running `python manage.py runserver`.
1. Access the endpoint on `http://127.0.0.1:8000/api/`. You can get and post to the endpoint directly from the web browser.
1. Enjoy! 🎉

From now on, whenever you want to start the project again, all you need is steps 3, 8, and 9.

### Example payload:
You can post this JSON payload to the API endpoint.
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

## How to run tests and other dev tools
To run the tests and use other dev-packages for various purposes like test coverage or flake8 reports, you need to run `pipenv install --dev`.
* Tests: run command `pytest` in the project root.
* Test coverage report: run `pytest --cov=application application/tests` in the project root.
* Flake8 reports: run `flake8` in the project root.
* Mypy for type checking: run `mypy path/to/program.py` in the project root.

## Thoughts and Reflections
In general, this exercise provides a good software engineering practice and thinking. More understanding of the context in which such API is used would help me assess better how the structure of the payload could be improved.
Nonetheless, what comes my mind are three different ways of structuring the data:
* [Structuring the payload for easier serializing](#structuring-the-payload-for-easier-serializing)
* [Making the open and close events more contained](#making-the-open-and-close-events-more-contained)
* [The lazy approach](#the-lazy-approach)

### Structuring the payload for easier serializing
Perhaps if the input data was formatted in a slightly different manner, writing serializers would have been easier.
For example, instead of having the days as keys, we could have a "day" key and its value as the days. That way, the payload would look like this:
```json
{
  "data": [
    {
        "day": "monday",
        "events": [
          {
            "type": "open",
            "value": 36000
          },
        ]
    }
  ]
}
```
...and the serializers would then be as simple as:

```python
class EventOfADaySerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=EVENT_TYPE_CHOICES)
    value = serializers.IntegerField(validators=[is_integer])


class DayOfTheWeekSerializer(serializers.Serializer):
    day = serializers.ChoiceField(choices=DAYS_OF_THE_WEEK)
    events = EventOfADaySerializer(many=True)

```
Still, this change only tackles one aspect, and not really simplifying the way the hours of each day are handled.

### Making the open and close events more contained
Another option is that we could go a step further to simplify the payload, and replace the dicts containing `"type"` and `"value"`  with `"opening_time"` and `"closing_time"`, like this:

```json
{
  "monday": [
    {
      "opening_time": 32400,
      "closing_time": 3600,
      "next_day": true
    }
  ]
}
``` 
This way the open and close times are _contained_ in one dict rather than existing in different "packets", which could also simplify the logic of closing events over midnight. However, it might be tricky to assess if a smaller `"closing_time"` value means _over midnight_ closing or a mere error in the data. It might then be a good idea to look into an additional parameter `"next_day"` to ensure data validity.

### The lazy approach
Of course, one could ask for the input data to be almost like the human readable format, as follows:

```json
{
  "monday": [
    {
      "opening_time": "12 PM",
      "closing_time": "12:30 AM"
    }
  ]
}
```
which leaves not much room for code to be written, but don't they say "the best code is no code"? `¯\_(ツ)_/¯`. On a serious note, it's probably a bad idea to forgo the luxury of a 32-bit Unix timestamp at least for the next 18 years.

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
- [x] Update README with reflections.
