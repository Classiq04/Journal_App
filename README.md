# Journal App 📔

A simple yet elegant journaling application built with a Python/Flask backend and an interactive frontend. This app allows you to write, save, and manage your daily journal entries with ease.

## Features ✨

- 📝 **Write Entries**: Easily create and save journal entries
- 📚 **View All Entries**: Display all saved journal entries in a clean list format
- 🐳 **Docker Support**: Run the entire application with Docker Compose
- 💾 **Persistent Storage**: Entries are saved and retrievable across sessions
- 🎨 **Clean UI**: Simple and intuitive user interface

## Tech Stack 🛠️

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, and JavaScript
- **Database**: Python-based backend storage
- **Containerization**: Docker & Docker Compose
- **Server**: Nginx (Frontend)

## Project Structure 📁

```
Journal_App/
├── backend/              # Flask backend application
│   ├── Dockerfile       # Backend Docker configuration
│   └── app.py          # Main Flask application
├── frontend/            # Frontend files
│   ├── index.html      # Main HTML page
│   ├── script.js       # JavaScript logic
│   └── styles.css      # Styling (optional)
├── docker-compose.yaml # Docker Compose configuration
└── README.md           # This file
```

## Prerequisites 📋

Before running the application, ensure you have:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

*Alternatively, for local development without Docker:*
- Python 3.7+
- Node.js/npm (optional, for frontend development)

## Quick Start 🚀

### Option 1: Using Docker Compose (Recommended)

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Classiq04/Journal_App.git
   cd Journal_App
   ```

2. **Start the Application**
   ```bash
   docker-compose up --build
   ```

3. **Access the Application**
   - Frontend: http://localhost:8000
   - Backend API: http://localhost:5000

4. **Stop the Application**
   ```bash
   docker-compose down
   ```

### Option 2: Running Locally (Without Docker)

#### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install flask
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```
   The backend will run on http://localhost:5000

#### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Start a simple HTTP server:
   ```bash
   python -m http.server 8000
   ```
   Or use:
   ```bash
   python3 -m http.server 8000
   ```

3. Open your browser and go to http://localhost:8000

## API Endpoints 🔌

### Get All Entries
- **Endpoint**: `GET /entries`
- **Response**: JSON array of all journal entries

### Add New Entry
- **Endpoint**: `POST /entries`
- **Request Body**:
  ```json
  {
    "content": "Your journal entry text here"
  }
  ```
- **Response**: Confirmation of entry creation

## Usage 📖

1. Open the application in your browser
2. Type your journal entry in the text area
3. Click the **"Add Entry"** button to save
4. Your entry will appear in the "All Entries" list below
5. All entries are automatically loaded when the page loads

## Docker Compose Configuration 🐳

The `docker-compose.yaml` file defines two services:

- **backend**: Flask API service running on port 5000
- **frontend**: Nginx web server serving the frontend on port 8000

Both services use volume mounts for live development and auto-restart on failure.

## Development 💻

### Making Changes to Backend
- Edit files in the `backend/` directory
- The Docker container will automatically reload due to volume mounting
- Restart the container if needed: `docker-compose restart backend`

### Making Changes to Frontend
- Edit files in the `frontend/` directory
- Changes reflect immediately in the browser (refresh the page)

## Troubleshooting 🔧

### Port Already in Use
If ports 5000 or 8000 are already in use, modify the `docker-compose.yaml`:
```yaml
ports:
  - "5001:5000"  # Change first number to an available port
```

### Container Won't Start
- Check Docker daemon is running
- View logs: `docker-compose logs -f`
- Rebuild containers: `docker-compose up --build`

### Frontend Can't Connect to Backend
- Verify both containers are running: `docker-compose ps`
- Check the API base URL in `frontend/script.js` matches your backend address
- Ensure the backend service is fully started (wait a few seconds)

## Future Enhancements 🌟

- [ ] User authentication and accounts
- [ ] Edit/delete existing entries
- [ ] Search and filter entries
- [ ] Export entries to PDF or file
- [ ] Dark mode theme
- [ ] Mobile-responsive design improvements
- [ ] Database integration (PostgreSQL/MongoDB)

## Contributing 🤝

Feel free to fork this project and submit pull requests with improvements!

## License 📄

This project is open source. Feel free to use and modify as needed.

## Author ✍️

Created by [Classiq04](https://github.com/Classiq04)

---

**Happy Journaling!** 📝✨

If you encounter any issues or have questions, feel free to open an issue on the [GitHub repository](https://github.com/Classiq04/Journal_App/issues).
