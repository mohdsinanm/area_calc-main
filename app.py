import streamlit as st
import polars as pl 
import math 

def calc_area_circle(diameter):
    return math.pi*pow((diameter/2),2)

def calc_width(total_number_of_duct,diametr_of_duct,distance_between_duct,bountary_dist):
    return (total_number_of_duct * diametr_of_duct) +  ((total_number_of_duct - 1) * distance_between_duct) + (2 * bountary_dist )

def cal_height(bountary_dist,no_of_total_rows,diametr_of_duct,distance_between_duct):
    return (2 * bountary_dist ) + (no_of_total_rows * diametr_of_duct) + ((no_of_total_rows - 1) * distance_between_duct )

def calc(total_wires,diameter_of_wire,no_of_duct_per_row, diametr_of_duct, distance_between_duct,bountary_dist,percentage_capacity):

    area_of_wire = round(calc_area_circle(diameter_of_wire),2)
    area_of_duct = round(calc_area_circle(diametr_of_duct),2)

    
    capacity_area = (area_of_duct*percentage_capacity)/100

    number_of_wire_per_duct = round(capacity_area/area_of_wire)

    total_number_of_duct = math.ceil(total_wires/number_of_wire_per_duct)

    
    no_of_total_rows =  math.ceil(total_number_of_duct/no_of_duct_per_row)
    if no_of_total_rows == 1:
        width = calc_width(total_number_of_duct,diametr_of_duct,distance_between_duct,bountary_dist)
        height =  cal_height(bountary_dist,no_of_total_rows,diametr_of_duct,distance_between_duct)
    else:
        width = calc_width(no_of_duct_per_row ,diametr_of_duct,distance_between_duct,bountary_dist)
        height =  cal_height(bountary_dist,no_of_total_rows,diametr_of_duct,distance_between_duct)

    results = {"Total number of ducts" : total_number_of_duct,
            "Width" : width,
            "Height" : height,
            "Area" : width * height,
            "Number of total rows" : no_of_total_rows,
            "Number of wires per duct" : number_of_wire_per_duct,
            "Area of wire" : area_of_wire,
            "Area of duct" : area_of_duct,
            }
    
    return results


def ui():
    
    total_wires = st.number_input("Enter total number of wire",step=1)
    diameter_of_wire = st.number_input("Diameter of wire")
    no_of_duct_per_row = st.number_input("Number of duct per row",value=3)
    diametr_of_duct = st.number_input("Diameter of duct",value=150)
    distance_between_duct = st.number_input("Distance between ducts",value=100)
    bountary_dist = st.number_input("Distance between duct and boundary",value=150)
    percentage_capacity = st.number_input("Percenatge filling",value=50)

    if st.button("Calculate"):
        if total_wires != 0 and diameter_of_wire != 0:
            st.session_state["results"] = calc(total_wires,diameter_of_wire,no_of_duct_per_row, diametr_of_duct, distance_between_duct,bountary_dist,percentage_capacity)
            with st.container(height=60,border=True):
                st.markdown(f"**Area = {st.session_state['results']['Area']}**")

            st.dataframe(pl.DataFrame(data= st.session_state["results"]).transpose(include_header=True).rename({"column":"Parameter","column_0":"Value"}),use_container_width=True)
        else:
            st.error("Please enter all the input values")
    
    

    
# Config the whole app
st.set_page_config(
    page_title="Calc app",
    page_icon="🧊",
    initial_sidebar_state="collapsed",
)

def main():
    st.header("DUCT BANK")
    ui()

main()
