# Mine Base APP WS

This is a Flask application that includes API documentation using OpenAPI 3 and Swagger UI. The project also includes configurations for code formatting, linting, and testing.

## Required Tools

- Python 3
- Postgres DB

## Run on Local

1. **Create a virtual environment**:

   ```sh
   python3 -m venv .venv
   ```

2. **Activate the virtual environment**:

   - On macOS and Linux:
     ```sh
     source .venv/bin/activate
     ```
   - On Windows:
     ```sh
     .venv\Scripts\activate
     ```

3. **Install Dependencies**:

   Make sure you have Python and pip installed. Then, install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

4. **Create local Docker DB**:

   ```sh
   cd docker-local-bd
   docker compose up -d
   ```

5. **Define the enviroment variable to run flask app**:

   ```sh
   export FLASK_APP=run.py
   export FLASK_ENV=development
   ```

6. **Required Environment Variables**:

    Make sure to set the following environment variables:

    ```sh
    export POSTGRES_USER=your_postgres_user
    export POSTGRES_PASSWORD=your_postgres_password
    export POSTGRES_HOST=your_postgres_host
    export POSTGRES_PORT=your_postgres_port
    export POSTGRES_DB=your_postgres_db
    ```

    Replace `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT`, and `POSTGRES_DB` with your actual values.

7. **Run the database migration scripts**:

   ```sh
   flask db upgrade
   ```

8. **Run the Flask application**:

   ```sh
   flask run
   ```

   The application will be available at `http://localhost:5000`.

## Code Formatting

To format the code, use `black` with a line length of 78 characters:

```sh
black --line-length 78 .
```

## Linting

To remove all unused imports, use `autoflake`:

```sh
autoflake --remove-all-unused-imports -r --in-place .
```

To sort imports, use `isort`:

```sh
isort .
```

To check for code style issues, use `flake8`:

- For api

  ```sh
  flake8 api/
  ```

- For test
  ```sh
  flake8 test/
  ```

## API Documentation

The API documentation is generated using `OpenAPI 3` and served using `Swagger UI`. You can access the Swagger UI at:

<http://localhost:5000/api/doc>

## Running Tests

### Unit Tests

To run unit tests, use:

```sh
python -m pytest -s -m "unit"
```

### Integration Tests

```sh
python -m pytest -s -m "integration"
```

## Docker

### Building the Docker Image

To build the Docker image for the application, use:

```sh
docker build -t mine-base-app-ws:latest .
```

### Running the Docker Container

To run the Docker container, use:

```sh
docker run \
-e POSTGRES_USER='your_postgres_user' \
-e POSTGRES_PASSWORD='your_postgres_password' \
-e POSTGRES_HOST='your_postgres_host' \
-e POSTGRES_PORT='your_postgres_port' \
-e POSTGRES_DB='your_postgres_db' \
--name mine-base-app-ws-local -p 5000:5000 mine-base-app-ws:latest 
```

The application will be available at
<http://localhost:5000.>

## Testing Locally

To test the application locally, follow these steps:

1. Start the Flask application:

   ```sh
   export FLASK_APP=run.py
   export FLASK_ENV=development
   flask run
   ```

2. Access the application: Open your browser and navigate to <http://localhost:5000>.

3. Run tests

   ```sh
   python -m pytest -s -m "unit"
   python -m pytest -s -m "integration"
   ```

## Error Handling

The application includes custom error handlers for validation errors, not found errors, and generic errors. These handlers log the errors and return appropriate JSON responses.

## Logging

Global logging is configured to log errors and stack traces. The logs are printed to the console with timestamps, log levels, and messages.

## License

This project is licensed under the MIT License.

### Explanation

1. **Required Tools**: Lists the tools required to run the application.
2. **Run on Local**: Steps to create and activate a virtual environment, install dependencies, and run the Flask application locally.
3. **Code Formatting**: Instructions for formatting code using `black`.
4. **Linting**: Instructions for removing unused imports using `autoflake` and checking code style issues using `flake8`.
5. **API Documentation**: Information about accessing the Swagger UI for API documentation.
6. **Running Tests**: Instructions for running unit and integration tests using `pytest`.
7. **Docker**: Instructions for building and running the Docker image.
8. **Testing Locally**: Steps to test the application locally.
9. **Error Handling**: Brief description of custom error handlers.
10. **Logging**: Brief description of global logging configuration.
11. **License**: Placeholder for the license information.
