# import streamlit as st;
# import pandas as pd;
# import joblib as jb;
# import numpy as np;



# #import the model
# model = jb.load("ml-model.pkl")


# st.title("ML Prediction App")

# st.write("Enter the customer details to predict the tip amount.")

# total_bill = st.number_input( "Total Bill ($)", min_value=0.0, value=20.0 ) 
# sex = st.selectbox( "Sex", ["Male", "Female"] ) 
# smoker = st.selectbox( "Smoker", ["Yes", "No"] ) 
# day = st.selectbox( "Day", ["Thur", "Fri", "Sat", "Sun"] ) 
# time = st.selectbox( "Time", ["Lunch", "Dinner"] ) 
# size = st.number_input( "Party Size", min_value=1, max_value=20, value=2 ) 
# # Prediction 
# if st.button("Predict Tip"): 
#     input_data = pd.DataFrame({ "total_bill": [total_bill], "sex": [sex], 
#                                "smoker": [smoker], "day": [day], "time": [time],
#                                  "size": [size] })
#     prediction = model.predict(input_data)
#     st.success(f"Predicted Tip: ${prediction[0]:.2f}")


import streamlit as st
import joblib
import pandas as pd

model = joblib.load("ml-model.pkl")

st.title("Tip Prediction App")
st.write("Enter the customer details to predict the tip amount.")

total_bill = st.number_input( "Total Bill ($)", min_value=0.0, value=20.0 ) 
sex = st.selectbox( "Sex", ["Male","Female"] ) 
smoker = st.selectbox( "Smoker", ["Yes","No"] ) 
day = st.selectbox( "Day", [ "Thur", "Fri", "Sat", "Sun" ] ) 
time = st.selectbox( "Time", ["Lunch", "Dinner"] ) 
size = st.number_input( "Party Size", min_value=1, max_value=20, value=2 ) 
# Prediction 
if st.button("Predict Tip"): 
    input_data = pd.DataFrame({ "total_bill": [total_bill],"size": [size], "sex_Female": [sex=="Female"], 
                               "smoker_No": [smoker=="No"], "day_Fri": [day=="Fri"],"day_Sat": [day=="Sat"],
                               "day_Sun": [day=="Sun"], "time_Dinner": [time=="Dinner"]})
    prediction = model.predict(input_data)
    st.success(f"Predicted Tip: ${prediction[0]:.2f}")