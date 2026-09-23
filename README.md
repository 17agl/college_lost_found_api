# College Lost & Found API

A FastAPI-based REST API for managing lost and found items on a college campus. The project uses **SQLite** for data storage and **SQLModel** for database operations.

## Technologies Used

* Python
* FastAPI
* SQLModel
* SQLite
* Uvicorn

## Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd lost_found_api
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 3. Install Required Dependencies

Install the required packages using:

```bash
pip install "fastapi[standard]" sqlmodel
```

Alternatively, if a `requirements.txt` file is provided:

```bash
pip install -r requirements.txt
```

## Running the Project

Start the FastAPI development server using:

```bash
fastapi dev main.py
```

Alternatively, you can run:

```bash
python -m uvicorn main:app --reload
```

After successfully starting the server, it will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive API documentation.

Open Swagger UI in your browser:

```text
http://127.0.0.1:8000/docs
```

You can use Swagger UI to test all available API endpoints.

## Database

The project uses **SQLite** as the database.

The database file `database.db` is automatically created when the application starts. SQLModel creates the required `Item` table automatically.

No separate database server or configuration is required.

## Available API Endpoints

| Method | Endpoint                     | Description                  |
| ------ | ---------------------------- | ---------------------------- |
| POST   | `/items`                     | Create a new lost/found item |
| GET    | `/items`                     | Get all reported items       |
| GET    | `/items/{item_id}`           | Get a specific item          |
| PUT    | `/items/{item_id}`           | Update an item               |
| DELETE | `/items/{item_id}`           | Delete an item               |
| GET    | `/items/status/{status}`     | Filter items by status       |
| GET    | `/items/category/{category}` | Filter items by category     |

## Supported Status Values

The API accepts only:

* `Lost`
* `Found`
* `Returned`

## Validation and Error Handling

The API validates required fields and prevents empty titles, meaningless descriptions, and invalid status values.

If an item ID does not exist, the API returns:

```text
404 Not Found
```

Invalid input values return an appropriate HTTP error response.

## Project Structure

```text
lost_found_api/
│
├── main.py
├── requirements.txt
├── database.db
├── README.md
│
└── screenshots/
    ├── post-item.png
    ├── get-items.png
    ├── get-item-by-id.png
    ├── update-item.png
    ├── delete-item.png
    ├── status-filter.png
    └── category-filter.png
```

## Proof of Work

All screenshots demonstrating the successful execution and testing of the API endpoints are provided in the attached **Word document**.

The document includes screenshots for:

* POST `/items` – Create a new item
* GET `/items` – Retrieve all items
* GET `/items/{item_id}` – Retrieve an item by ID
* PUT `/items/{item_id}` – Update an existing item
* DELETE `/items/{item_id}` – Delete an item
* GET `/items/status/{status}` – Filter items by status
* GET `/items/category/{category}` – Filter items by category

The screenshots provide evidence of successful API execution through the FastAPI Swagger UI.

