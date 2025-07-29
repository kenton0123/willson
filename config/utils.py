import streamlit as st

def capture_and_modify_state(display=True):
    # Use modern query_params if available
    if hasattr(st, "query_params"):
        query_params = st.query_params
        state = query_params.get("state")
    else:
        query_params = st.experimental_get_query_params()
        state = query_params.get("state", [None])[0]

    # Store state in session_state if exists
    if state and 'state' not in st.session_state:
        st.session_state.state = state

    # Display status if requested
    if display:
        if 'state' in st.session_state:
            st.success(f"問卷狀態：{st.session_state.state}")
        else:
            st.info("尚未收到問卷狀態")
