import streamlit as st

def capture_and_modify_state():
    query_params = st.query_params if hasattr(st, "query_params") else st.experimental_get_query_params()
    state = query_params.get("state", None)  # Assuming 'state' is the parameter name

    # Store the state in session state if it exists
    if state and 'state' not in st.session_state:
        st.session_state.state = state[0] if isinstance(state, list) else state

    # Display the captured state
    if 'state' in st.session_state:
        st.success(f"問卷狀態：{st.session_state.state}")

        # Create a new URL with the state
        new_url = f"https://thebritishmuseumassignment.streamlit.app/case5?state={st.session_state.state}"
        st.write(f"新的網址：{new_url}")
    else:
        st.info("尚未收到問卷狀態")
