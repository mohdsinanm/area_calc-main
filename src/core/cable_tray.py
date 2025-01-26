import streamlit as st
from src.utils.utils import calculate_cable_dist


def calculate_height(inputs):

    cable_dia = sorted([inputs['diameter_of_IS'], inputs['diameter_of_nonIS']])[-1]

    return  inputs['layers'] * cable_dia + ((inputs['layers']- 1) * inputs['cable_to_cable']) + (inputs['edge_to_cable_distance'] * 2)


def calculatet_width(inputs):
    total_cable_dist_IS = calculate_cable_dist(inputs['no_cables_IS'] , inputs['diameter_of_IS'], inputs['cable_to_cable'])

    total_cable_dist_nonIS = calculate_cable_dist(inputs['no_cables_nonIS'] , inputs['diameter_of_nonIS'], inputs['cable_to_cable'])

    return ((inputs['edge_to_cable_distance'] * 2) + total_cable_dist_IS + total_cable_dist_nonIS + inputs['distance_between_IS_non_Is']) / inputs['layers']

def tray_size_calculate(inputs):

    return {"width" : calculatet_width(inputs),
            "height" : calculate_height(inputs)}


def cable_tray_UI():
    no_cables_IS = st.number_input("Number of cables : Instrumnet (IS)",step= 1)
    diameter_of_IS =  st.number_input("Diameter of (IS) cables")

    no_cables_nonIS = st.number_input("Number of cables : Instrumnet (Non-IS)",step= 1)
    diameter_of_nonIS =  st.number_input("Diameter of (Non-IS) cables")

    distance_between_IS_non_Is = st.number_input("Distance between IS cables and Non-IS cables", value=50)

    cable_to_cable =  st.number_input("Distance between cables to cables", value=5)

    edge_to_cable_distance = st.number_input("Distance between edge and cables", value=10,help = 'Will be considered in every sides')

    layer_to_layer = st.number_input("Layer to layer distnace", value= 10)

    layers = st.number_input("Number of layers", value= 1, step=1)

    return {
        "no_cables_IS" : no_cables_IS,
        "diameter_of_IS" : diameter_of_IS,
        "no_cables_nonIS": no_cables_nonIS,
        "diameter_of_nonIS" : diameter_of_nonIS,
        "distance_between_IS_non_Is" : distance_between_IS_non_Is,
        "cable_to_cable" : cable_to_cable,
        "edge_to_cable_distance" : edge_to_cable_distance,
        "layer_to_layer" : layer_to_layer,
        "layers" : layers


    }

def cable_tray_main():
    st.header("CABLE TRAY SIZE CALCULATION")
    inputs = cable_tray_UI()
    if st.button("Calculate"):
        result = tray_size_calculate(inputs)
        st.write(f"**WIDTH** : {result['width']}")
        st.write(f"**HEIGHT** : {result['height']}")