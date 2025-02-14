## Requirements

- Python 3.x
- [Optional] Conda (for Conda setup)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/ZakariaBaqasse/csc_ai_apps_and_agents_workshops.git
cd csc_ai_apps_and_agents_workshops
```

### 2. Setting up the Virtual Environment

#### Option 1: Using `venv` (Recommended)

##### On Windows:

1. Open Command Prompt and navigate to the project directory.
2. Run the following command to create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   ```bash
   venv\Scripts\activate
   ```

##### On Linux/macOS:

1. Open Terminal and navigate to the project directory.
2. Run the following command to create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

#### Option 2: Using `conda`

##### On Windows/Linux/macOS:

1. Create a new conda environment with the required Python version:

   ```bash
   conda create --name myenv python=3.x
   ```

2. Activate the conda environment:

   ```bash
   conda activate myenv
   ```

### 3. Install Dependencies

Once the virtual environment is activated, install the necessary dependencies by running:

```bash
pip install -r requirements.txt
```

### 4. Running the Project

Each file can be run individually:

```bash
python workshop-[workshop-number].py
```
