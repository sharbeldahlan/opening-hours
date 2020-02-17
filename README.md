# opening-hours
An API that takes JSON-formatted opening hours of a restaurant as an input and outputs hours in a more human readable format.

* [Needed components](#needed-components)
* [To-do list](#to-do-list)

## Needed components
Here is a preliminary high-level plan.

### Input
* The input is in the format of a JSON file.
* Input runs through a validator. Validity of the input to be communicated through the interface.
* API view to pass the cleaned input to the service for processing.

### Processing
* Service to receive the cleaned data and apply conversion logic.
* Converted logic to be returned to the API view.

### Output
* Converted data returned to API view.
* Converted data further formatted in some template. 
 

## To-do list

- [x] Write preliminary plan 
- [x] Prepare project dependencies.
- [x] Create Django project.
- [x] Create application within the project and give it the url.
- [x] Install Django REST Framework.
- [ ] Write unit tests for API Validators
- [ ] Write the API endpoints with validators.
- [ ] Write unit tests for main logic service.
- [ ] Iterate on tests and add integration tests.
- [ ] Write main logic service.
- [ ] Run tests and iterate. Make sure everything is in check.
- [ ] Update README with "How To Run" section.
- [ ] Update README with architecture decisions and pros and cons.