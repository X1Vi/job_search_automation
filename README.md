# Step 1: Create a virtual environment named "venv"
python -m venv venv

# Step 2: Activate the virtual environment
# On Linux/macOS/WSL:
source venv/bin/activate

# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# On Windows (Command Prompt):
venv\Scripts\activate.bat

# Step 3: Install dependencies from requirements.txt
pip install -r requirements.txt

#Step 4: Run the Scripts
python3 scriptName.py
