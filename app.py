import streamlit as st
from src.core.duct import duct_main
from src.core.trench import trench_main
from src.core.concrete_trench import concrete_trench_main
from src.core.cable_tray import cable_tray_main
import streamlit_antd_components as sac
    
# Config the whole app
st.set_page_config(
    page_title="INSTRUMENTATION CALCULATION",
    page_icon="🧊",
    initial_sidebar_state="collapsed",

)

def main():

    with st.sidebar:
        sac.menu([
            sac.MenuItem('Menu', icon='house-fill',children=[
                sac.MenuItem('Home'),
                sac.MenuItem('Duct Bank Calulation'),
                sac.MenuItem('Trench Calulation'),
                sac.MenuItem("Concrete Trench Calulation"),
                sac.MenuItem("Cable Tray size calulation")
            ]),
            sac.MenuItem(type='divider'),
            sac.MenuItem('link', type='group'),
        ], open_all=True, key='menu')
    
    if st.session_state['menu'] == 'Duct Bank Calulation':
        duct_main()
    elif st.session_state['menu'] == 'Trench Calulation':
        trench_main()
    elif st.session_state['menu'] == 'Concrete Trench Calulation':
        concrete_trench_main()
    elif st.session_state['menu'] == 'Cable Tray size calulation':
        cable_tray_main()
    else:
        st.header("Home")
        st.write("Please explore the option from the side bar")
        st.image("src/assets/3-2.jpg")
        st.image("src/assets/Duct-Bank-1.jpg")
        st.image("src/assets/1542025918734.png")
        pass

main()