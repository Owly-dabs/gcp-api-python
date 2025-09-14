import streamlit as st
import requests
import json

st.title("API Testing Tool")
st.write("Test your API endpoints with GET and POST requests")

# Input for API base URL
base_url = st.text_input(
    "Enter your API base URL:",
    value="https://your-service.a.run.app",
    help="The base URL of your API service"
)

# Select HTTP method
method = st.selectbox("Select HTTP Method:", ["GET", "POST"])

# Input for endpoint path
endpoint = st.text_input("Enter endpoint path:", value="", help="e.g., /users, /message")

# Input for request body (for POST requests)
if method == "POST":
    body = st.text_area("Enter JSON request body (optional):",
                       value='{\n  "name": "World"\n}',
                       help="Enter valid JSON for the request body")
    
    # Validate JSON
    try:
        json.loads(body) if body.strip() else None
        json_valid = True
    except json.JSONDecodeError:
        json_valid = False
        st.error("Invalid JSON in request body")

# Button to send request
if st.button("Send Request"):
    if base_url:
        # Construct full URL
        url = base_url.rstrip('/') + '/' + endpoint.lstrip('/') if endpoint else base_url
        
        try:
            if method == "GET":
                response = requests.get(url)
            else:  # POST
                # Check if JSON is valid before sending request
                if not json_valid:
                    st.error("Please fix the JSON errors before sending the request")
                    st.stop()
                
                headers = {'Content-Type': 'application/json'}
                json_data = json.loads(body) if body.strip() else None
                response = requests.post(url, json=json_data, headers=headers)
            
            # Display the response
            st.write(f"**URL:** {url}")
            st.write(f"**Method:** {method}")
            st.write(f"**Status Code:** {response.status_code}")
            
            if response.status_code < 400:
                st.success("✅ Request successful!")
            else:
                st.error("❌ Request failed")
                
            # Try to display JSON response
            try:
                st.json(response.json())
            except json.JSONDecodeError:
                st.text(response.text)
                
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Failed to send request: {str(e)}")
    else:
        st.warning("Please enter a base URL")