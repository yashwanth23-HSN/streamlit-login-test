import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Welcome Portal",
    page_icon="👋",
    layout="centered"
)


# ============================================================
# USER DETAILS
# ============================================================
# Temporary users for testing
USERS = {
    "admin": {
        "password": "admin123",
        "name": "Administrator"
    },
    "yashwanth": {
        "password": "1234",
        "name": "Yashwanth"
    }
}


# ============================================================
# INITIALIZE SESSION STATE
# ============================================================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "name" not in st.session_state:
    st.session_state.name = ""


# ============================================================
# LOGIN FUNCTION
# ============================================================
def login_page():

    st.title("🔐 Portal Sign In")

    st.write("Please enter your username and password.")

    st.divider()

    with st.form("login_form"):

        username = st.text_input(
            "Username",
            placeholder="Enter your username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password"
        )

        login_button = st.form_submit_button(
            "Login",
            use_container_width=True
        )

    # --------------------------------------------------------
    # CHECK LOGIN
    # --------------------------------------------------------
    if login_button:

        username = username.strip().lower()

        # Empty username
        if username == "":
            st.warning("Please enter username.")
            return

        # Empty password
        if password == "":
            st.warning("Please enter password.")
            return

        # Username not found
        if username not in USERS:
            st.error("❌ Invalid username.")
            return

        # Password incorrect
        if password != USERS[username]["password"]:
            st.error("❌ Incorrect password.")
            return

        # ----------------------------------------------------
        # LOGIN SUCCESSFUL
        # ----------------------------------------------------
        st.session_state.authenticated = True
        st.session_state.username = username
        st.session_state.name = USERS[username]["name"]

        st.rerun()


# ============================================================
# WELCOME PAGE FUNCTION
# ============================================================
def welcome_page():

    st.success("✅ Login Successful")

    st.title(f"👋 Welcome, {st.session_state.name}!")

    st.subheader("Good to see you again.")

    st.write(
        "You have successfully logged into the portal."
    )

    st.divider()

    st.info(
        f"Logged in as: **{st.session_state.username}**"
    )

    st.write("### Welcome to the Dashboard")

    st.write(
        """
        This is your home page.

        You can add your dashboard functions,
        reports, forms, or other Streamlit pages here.
        """
    )

    st.divider()

    # --------------------------------------------------------
    # LOGOUT
    # --------------------------------------------------------
    if st.button(
        "🚪 Logout",
        use_container_width=True
    ):

        st.session_state.authenticated = False
        st.session_state.username = ""
        st.session_state.name = ""

        st.rerun()


# ============================================================
# MAIN FUNCTION
# ===========================================================
def main():

    if st.session_state.authenticated:
        welcome_page()
    else:
        login_page()


# ============================================================
# START APPLICATION
# ============================================================
if __name__ == "__main__":
    main()