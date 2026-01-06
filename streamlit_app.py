import streamlit as st

# Page Configuration
st.set_page_config(page_title="Beckett", layout="wide")

# App Pages
home = st.Page("pages/home.py", title="Home", icon="⚾")
functional_patterns = st.Page("pages/functional_patterns.py", title="Functional Patterns", icon="🛠")
hitting_done_right = st.Page("pages/hitting_done_right.py", title="Hitting Done Right", icon="💣")
parisi = st.Page("pages/parisi.py", title="Parisi Speed School", icon="🏃")
pro_velocity = st.Page("pages/pro_velocity.py", title="Pro Velocity Bat", icon="💫")
the_turf = st.Page("pages/the_turf.py", title="The Turf", icon="❇️")

# Create the navigation menu
pg = st.navigation([home, functional_patterns, hitting_done_right, parisi, pro_velocity, the_turf])


# Run the selected page
pg.run()
