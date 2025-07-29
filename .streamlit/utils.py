import streamlit as st

def capture_status():
    # Capture URL parameters
    query_params = st.query_params if hasattr(st, "query_params") else st.experimental_get_query_params()
    status = query_params.get("status", None)

    # Store the status in session state if it exists
    if status and 'status' not in st.session_state:
        st.session_state.status = status[0] if isinstance(status, list) else status

    # Display the captured status
    if 'status' in st.session_state:
        st.success(f"問卷狀態：{st.session_state.status}")
    else:
        st.info("尚未收到問卷狀態")
