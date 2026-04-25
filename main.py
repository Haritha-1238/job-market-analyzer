# main.py
from src.cleaner   import clean_jobs
from src.analyser  import run_analysis
from src.dashboard import build_dashboard

if __name__ == "__main__":
    print("--- Step 1: Cleaning ---")
    clean_jobs()

    print("--- Step 2: Analysis ---")
    run_analysis()

    print("--- Step 3: Dashboard ---")
    build_dashboard()