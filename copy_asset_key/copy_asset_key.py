import json
import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()

JIRA_PAT = os.getenv("JIRA_PAT")
JIRA_URL = os.getenv("JIRA_URL")


s = requests.Session()

s.headers = {"Authorization": f"Bearer {JIRA_PAT}", "Content-Type": "application/json"}

issues = s.get(f"{JIRA_URL}/rest/api/3/issue/")

print(issues.content)
