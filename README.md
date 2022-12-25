# UMNP
## Folder Structure
- `umnp/public/` assets folder: images and js configuration.
- `umnp/static_src/` tailwind and css configuration.
- `umnp/static_src/app/` urls, views, models, and admin configuration.
- `umnp/templates/` html configuration.

## Starting the Server
- Compile tailwind classes used in the html by the command below:
    ```
    python manage.py tailwind start
    ```
- In another terminal, run the command below to start the server:
    ```
    python manage.py runserver
    ```
- If the compiled classes hasn't been applied, try hard-refreshing the browser with `Ctrl + F5` or `Ctrl + Shift + R`

## Database Data
- Get Database Data by running the command below:
    ```
    python manage.py loaddata db.json
    ```
- Save Database Data by running the command below:
    ```
    python manage.py dumpdata > db.json
    ```