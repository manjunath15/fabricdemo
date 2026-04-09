workspace_id = "<workspace-id>"
capacity_id = "<capacity-id>"

assign_url = f"https://api.fabric.microsoft.com/v1/workspaces/{workspace_id}/assignToCapacity"

assign_payload = {
    "capacityId": capacity_id
}

assign_response = requests.post(
    assign_url,
    headers=headers,
    json=assign_payload
)

print(assign_response.status_code)
print(assign_response.text)