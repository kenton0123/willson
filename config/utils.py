import streamlit as st

def capture_and_modify_state(display=True):
    query_params = st.query_params if hasattr(st, "query_params") else st.experimental_get_query_params()
    state = query_params.get("state", None)

    # Store state in session_state if exists
    if state is not None and 'state' not in st.session_state:
        if isinstance(state, list):
            st.session_state.state = state[0]
        else:
            st.session_state.state = state

    # Display only if required
    if display and 'state' in st.session_state:
        st.success(f"問卷狀態：{st.session_state.state}")
        # Use current app URL instead of hardcoding
        current_url = st.experimental_get_query_params().get('url', [''])[0]
        if not current_url:
            current_url = st.server_util.get_current_url()
        new_url = f"{current_url}?state={st.session_state.state}"
        st.write(f"新的網址：{new_url}")
    elif display:
        st.info("尚未收到問卷狀態")

