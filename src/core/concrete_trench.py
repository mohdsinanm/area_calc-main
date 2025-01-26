import streamlit as st

def calculate_cable_dist(number_of_cables, diameter, cable_to_cale_dist):
    return (number_of_cables * diameter) + (cable_to_cale_dist * (number_of_cables - 1))


def calculate_width(inputs):
    
    total_cable_dist_IS = calculate_cable_dist(inputs['no_cables_IS'] , inputs['diameter_of_IS'], inputs['cable_to_cable'])

    total_cable_dist_nonIS = calculate_cable_dist(inputs['no_cables_nonIS'] , inputs['diameter_of_nonIS'], inputs['cable_to_cable'])

    total_cable_dist_tele =  calculate_cable_dist(inputs['no_cables_tele'] , inputs['diameter_of_tele'], inputs['cable_to_cable'])

    return ((inputs['edge_to_cable_distance'] * 2) + total_cable_dist_IS + inputs['distance_between_IS_non_Is'] + total_cable_dist_nonIS + inputs['distance_between_inst_tele'] + total_cable_dist_tele) / inputs['layers'] + (inputs["wall_thickness"] * 2)

def calculate_height(inputs):
    cable_dia = sorted([inputs['diameter_of_IS'], inputs['diameter_of_nonIS'], inputs['diameter_of_tele']])[-1]

    return inputs['grade_to_cables'] +  (inputs['layers'] * cable_dia) + ((inputs['layers'] - 1) * inputs['layer_to_layer']) + inputs['cover_slab_thickness'] + inputs['bottom_thickness']+ inputs['edge_to_cable_distance']

def concrete_trench_calc(inputs):

    return {"width" : calculate_width(inputs),
            'height' : calculate_height(inputs) }


def concrete_ternch_UI():
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

    wall_thickness = st.number_input("Wall thickness", value=150, help='Considered in both sided')

    cover_slab_thickness = st.number_input("Thickness of cover slab", value=150)

    grade_to_cables = st.number_input("Grade to cable distance", value=200)

    bottom_thickness = st.number_input("Bottom concrete thickness", value=300)

    layers = st.number_input("Number of layers", value= 1, step=1)

    layer_to_layer = st.number_input("Layer to layer distnace", value= 50)

    st.image("src/assets/concrete.jpg")
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
        "wall_thickness": wall_thickness,
        "cover_slab_thickness" : cover_slab_thickness,
        "bottom_thickness" : bottom_thickness,
        "grade_to_cables" : grade_to_cables,
        "layer_to_layer" :layer_to_layer

    }

def concrete_trench_main():
    st.header("CONCRETE TRENCH CALCUALATION")
    inputs = concrete_ternch_UI()
    if st.button("Calculate"):
        result = concrete_trench_calc(inputs)
        st.write(f"**WIDTH** : {result['width']}")
        st.write(f"**HEIGHT** : {result['height']}")