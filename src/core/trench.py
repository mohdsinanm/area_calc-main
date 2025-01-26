import streamlit as st

def calculate_cable_dist(number_of_cables, diameter, cable_to_cale_dist):
    return (number_of_cables * diameter) + (cable_to_cale_dist * (number_of_cables - 1))


def calculate_width(inputs):
    
    total_cable_dist_IS = calculate_cable_dist(inputs['no_cables_IS'] , inputs['diameter_of_IS'], inputs['cable_to_cable'])

    total_cable_dist_nonIS = calculate_cable_dist(inputs['no_cables_nonIS'] , inputs['diameter_of_nonIS'], inputs['cable_to_cable'])

    total_cable_dist_tele =  calculate_cable_dist(inputs['no_cables_tele'] , inputs['diameter_of_tele'], inputs['cable_to_cable'])

    return ((inputs['edge_to_cable_distance'] * 2) + total_cable_dist_IS + inputs['distance_between_IS_non_Is'] + total_cable_dist_nonIS + inputs['distance_between_inst_tele'] + total_cable_dist_tele) / inputs['layers']

def calulate_height(inputs):
    cable_dia = sorted([inputs['diameter_of_IS'], inputs['diameter_of_nonIS'], inputs['diameter_of_tele']])[-1]
    return inputs['grade_to_tiles'] + inputs['tile_tickness'] + inputs['tiles_to_cable'] + (inputs['layers'] * cable_dia) + ((inputs['layers'] - 1) * inputs['layer_to_layer']) + inputs['edge_to_cable_distance']


def trench_calc(inputs):

    return {"width" : calculate_width(inputs),
            'height' : calulate_height(inputs)}


def ternch_UI():
    no_cables_IS = st.number_input("Number of cables : Instrumnet (IS)",step= 1)
    diameter_of_IS =  st.number_input("Diameter of (IS) cables")

    no_cables_nonIS = st.number_input("Number of cables : Instrumnet (Non-IS)",step= 1)
    diameter_of_nonIS =  st.number_input("Diameter of (Non-IS) cables")

    no_cables_tele = st.number_input("Number of cables : Telecom",step= 1) 
    diameter_of_tele =  st.number_input("Diameter of Telecom cables")

    distance_between_IS_non_Is = st.number_input("Distance between IS cables and Non-IS cables", value=50)

    cable_to_cable =  st.number_input("Distance between cables to cables", value=5)

    edge_to_cable_distance = st.number_input("Distance between edge and cables", value=50,help = 'Will be considered in every sides')

    distance_between_inst_tele = st.number_input("Distance between Telecom cables to  Instrument cables", value=300)

    layers = st.number_input("Number of layers", value= 1, step=1)

    grade_to_tiles = st.number_input("Grade to cable tiles distance", value=600)

    tile_tickness = st.number_input("Tile tickness", value=50)

    tiles_to_cable = st.number_input("Tile to cable distance", value=200)

    layer_to_layer = st.number_input("Layer to layer distnace", value= 50)

    st.image("src/assets/buried.jpg")
    return {
        "no_cables_IS" : no_cables_IS,
        "diameter_of_IS" : diameter_of_IS,
        "no_cables_nonIS": no_cables_nonIS,
        "diameter_of_nonIS" : diameter_of_nonIS,
        "no_cables_tele" : no_cables_tele,
        "diameter_of_tele" : diameter_of_tele,
        "distance_between_IS_non_Is" : distance_between_IS_non_Is,
        "cable_to_cable" : cable_to_cable,
        "edge_to_cable_distance" : edge_to_cable_distance,
        "distance_between_inst_tele" : distance_between_inst_tele,
        "layers" : layers,
        "grade_to_tiles": grade_to_tiles,
        "tile_tickness" : tile_tickness,
        "tiles_to_cable" : tiles_to_cable,
        "layer_to_layer" : layer_to_layer


    }

def trench_main():
    st.header("TRENCH CALCUALATION")
    inputs = ternch_UI()
    if st.button("Calculate"):
        result = trench_calc(inputs)
        st.write(f"**WIDTH** : {result['width']}")
        st.write(f"**HEIGHT** : {result['height']}")