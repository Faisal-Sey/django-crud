# Django CRUD Project

This is a Django project that implements CRUD (Create, Read, Update, Delete) operations. The project consists of an app called "crud" that handles the CRUD operations and a "helpers" folder that contains helper functions.

## Project Structure

The project follows the following structure:

- `_main`: Project files and settings
- `helpers`: Folder containing helper functions
- `crud`: App responsible for CRUD operations

## URLs

The URLs for the CRUD operations are defined in the `urls.py` file inside the `crud` app. Here are the URL patterns:

- `get-all-data/`: Retrieves all data records.
- `get-all-data/<int:page_number>/`: Retrieves all data records in a paginated manner based on the provided page number.
- `get-one-data/<slug:attr>/<slug:val>/<slug:value_type>/`: Retrieves a single data record based on the provided attribute, value, and value type.
- `add-data/`: Adds a new data record.
- `update-data/<int:data_id>/`: Updates an existing data record identified by the provided data ID.
- `delete-data/<int:data_id>/`: Deletes an existing data record identified by the provided data ID.
- `delete-many-data/`: Deletes multiple data records.

## Setting Up

To set up the Django CRUD project, follow these steps:

1. Install the project dependencies by running `pip install -r requirements.txt` in the project root directory.
2. Apply the database migrations by running `python manage.py makemigrations` and `python manage.py migrate` in the project root directory.
3. Start the development server by running `python manage.py runserver` in the project root directory.

The project should now be up and running, and you can access the CRUD operations through the defined URLs.

Please note that this is a basic setup guide, and you may need to customize it based on your specific environment and requirements.

Feel free to explore and modify the code to suit your needs. Happy coding!