import uvicorn
import os
import subprocess
from setup import init_firebase


if __name__ == "__main__":
    # setup firebase credentials for authorizing service account
    # subprocess.run(f'. {os.getcwd()}/server/setup_credentials.sh', shell=True)
    init_firebase()
    uvicorn.run(f"app:app", host="127.0.0.1", port=5000, log_level="info", reload=True)