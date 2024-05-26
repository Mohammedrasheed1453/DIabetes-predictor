import pickle
import streamlit as st
from streamlit_option_menu import option_menu
disease=pickle.load(open("diabetesmodel.sav","rb"))
with st.sidebar:
    selected=option_menu("DIABETES PREDICTOR",["diabetes prediction"],icons=["activity"])
if selected=="diabetes prediction":
    st.title("DIABETES PREDICTOR")
    col1,col2,col3=st.columns(3)
    with col1:
        pregnancies=st.text_input("enter number of pregnancies")
    with col2:
        glucose=st.text_input("enter the glucose level")
    with col3:
        bp=st.text_input("enter the bp")
    with col1:
        skinthick=st.text_input("enter the skin-thickness")
    with col2:
        insulin=st.text_input("enter the insulin level")
    with col3:
        bmi=st.text_input("enter the bodymassindex")
    with col1:
        diabetespedigree=st.text_input("enter the diabtes-pedigree")
    with col2:
        age=st.text_input("enter the age")
    diagnosis=""
    if st.button("diabetes-predictor"):
        diapre=disease.predict([[pregnancies,glucose,bp,skinthick,insulin,bmi,diabetespedigree,age]])
        if diapre[0]==1:
            diagnosis="the person is diabetic"
        else:
            diagnosis="the person is not diabetic"
        st.success(diagnosis)
