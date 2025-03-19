# PizManager

PizManager is a simple, streamlined solution designed to help small businesses manage their operations efficiently. This web-based platform integrates customer management, sales tracking, and inventory management into a single application.

## Features

- **Customer Management**: Easily add, edit, and manage customer information, including contact details and purchase history.
- **Sales Tracking**: Record and monitor sales transactions, providing insights into revenue and sales performance.
- **Inventory Management**: Manage product stock levels, update inventory, and receive alerts for low-stock items.
- **Reporting**: Generate reports on business performance, including sales, inventory levels, and customer engagement.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: React (JavaScript)
- **Database**: PostgreSQL
- **Version Control**: GitHub
- **Testing**: Pytest, Django Test Framework

## Getting Started

### Prerequisites

- Python 3.x
- Node.js and npm
- PostgreSQL

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/PizManager.git
   cd PizManager
   ```

2. Set up the backend:
   - Navigate to the `backend` directory.
   - Install the required Python packages:
     ```
     pip install -r requirements.txt
     ```
   - Set up the PostgreSQL database and update the `settings.py` file with your database credentials.
   - Run migrations:
     ```
     python manage.py migrate
     ```

3. Set up the frontend:
   - Navigate to the `frontend` directory.
   - Install the required npm packages:
     ```
     npm install
     ```

4. Run the applications:
   - Start the backend server:
     ```
     python manage.py runserver
     ```
   - Start the frontend development server:
     ```
     npm start
     ```

## Usage

Once both the backend and frontend servers are running, you can access the application in your web browser at `http://localhost:3000`. Use the interface to manage customers, sales, and inventory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.