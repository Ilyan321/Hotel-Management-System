# LuxeStay Hotel Management System

A streamlit-based hotel management system designed to streamline hotel operations including guest check-in/check-out, room tracking, and guest search.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-red)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

- **Check-In Management** — Register guests with name, email, phone, room type (Single/Double/Suite), and check-in/check-out dates.
- **Check-Out Management** — Check out guests by name, updating their status in the system.
- **View All Data** — Display all guest records in a tabular format.
- **Guest Search** — Search guests by name, email, or phone number.
- **Additional Services Overview** — Kitchen, Laundry, Gym, and Pool management sections.

## Tech Stack

- **Python 3**
- **Streamlit** — Web UI framework
- **Pandas** — Data handling and CSV operations

## Getting Started

### Prerequisites

- Python 3.x installed
- pip package manager

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ilyan321/Hotel-Management-System.git
   cd Hotel-Management-System
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install streamlit pandas os
   ```

### Running the App

```bash
streamlit run main.py
```

The app will open in your browser. A `Rooms.csv` file is automatically created on first run to store guest data.

## Project Structure

```
Hotel-Management-System/
├── main.py        # Main Streamlit application
├── Rooms.csv      # Guest data storage (auto-generated)
├── LICENSE         # MIT License
└── README.md       # Project documentation
```

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Author

**Ilyan Khan**