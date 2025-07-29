import streamlit as st

def capture_status():
    query_params = st.query_params if hasattr(st, "query_params") else st.experimental_get_query_params()
    status = query_params.get("state", None)  # Assuming 'state' is the parameter name

    # Store the status in session state if it exists
    if status and 'status' not in st.session_state:
        st.session_state.status = status[0] if isinstance(status, list) else status

    # Display the captured status
    if 'status' in st.session_state:
        st.success(f"問卷狀態：{st.session_state.status}")

        # Create a new URL with the status
        new_url = f"https://thebritishmuseumassignment.streamlit.app/case5?state={st.session_state.status}"
        st.write(f"新的網址：{new_url}")
    else:
        st.info("尚未收到問卷狀態")
