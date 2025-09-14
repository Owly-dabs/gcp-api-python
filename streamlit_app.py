import streamlit as st
import requests

st.title("API Health Check")
st.write("Ping your FastAPI endpoint to check if it's working")

# Input for API URL
api_url = st.text_input(
    "Enter your FastAPI endpoint URL:",
    value="https://your-service.a.run.app",
    help="The URL of your deployed FastAPI service"
)

# Button to ping the API
if st.button("Ping API"):
    if api_url:
        try:
            # Send GET request to the API
            response = requests.get(api_url)
            
            # Display the response
            st.write(f"**Status Code:** {response.status_code}")
            
            if response.status_code == 200:
                st.success("✅ API is working!")
                st.json(response.json())
            else:
                st.error("❌ API returned an error")
                st.text(response.text)
                
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Failed to connect to API: {str(e)}")
    else:
        st.warning("Please enter an API URL")