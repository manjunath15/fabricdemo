import requests
import msal

# ========= CONFIGURATION =========

TENANT_ID = "xx"
CLIENT_ID = "xx"
CLIENT_SECRET = "xx"

WORKSPACE_NAME = "fabric-api-created-ws"

AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

SCOPE = ["https://api.fabric.microsoft.com/.default"]

FABRIC_WORKSPACE_API = "https://api.fabric.microsoft.com/v1/workspaces"

# ========= TOKEN GENERATION =========

app = msal.ConfidentialClientApplication(
    CLIENT_ID,
    authority=AUTHORITY,
    client_credential=CLIENT_SECRET
)

token_response = app.acquire_token_for_client(scopes=SCOPE)

if "access_token" not in token_response:
    raise Exception("Token generation failed: " + str(token_response))

access_token = token_response["access_token"]

print("✅ Token acquired")

# ========= CREATE WORKSPACE =========

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

workspace_payload = {
    "displayName": WORKSPACE_NAME
}

response = requests.post(
    FABRIC_WORKSPACE_API,
    headers=headers,
    json=workspace_payload
)

print("Status Code:", response.status_code)
print("Response:", response.text)

if response.status_code == 201:
    print("✅ Workspace Created Successfully")
else:
    print("❌ Workspace Creation Failed")
