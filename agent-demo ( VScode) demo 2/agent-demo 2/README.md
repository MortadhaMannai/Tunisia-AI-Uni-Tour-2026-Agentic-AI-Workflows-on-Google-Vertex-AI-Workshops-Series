# DevFest Agent Demo

This demo contains a simple local setup to present an agentic AI workflow during a live talk.
It includes:
- train_model.py: trains a small XGBoost model and saves vertex_model.pkl
- mock_api.py: a Flask endpoint that returns synthetic payloads
- agent_demo.py: fetches data, predicts, generates SHAP explanation, and executes a simulated action
- requirements.txt: dependencies

Steps to run locally:
1. Create a virtual environment
   python -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   .venv\Scripts\activate     # Windows PowerShell

2. Install dependencies
   pip install -r requirements.txt

3. Train the model
   python train_model.py

4. Start the mock API in a separate terminal
   python mock_api.py

5. Run the agent demo
   python agent_demo.py

Notes:
- If SHAP plotting fails, run the demo in a Jupyter notebook or save plots to files and open them
- You can change loop and pause parameters in agent_demo.py for presentation pacing
