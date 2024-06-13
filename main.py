from PIL import Image
import pandas as pd
import numpy as np
import streamlit as st
import joblib
from tensorflow.keras.models import load_model # type: ignore
import pyodbc
import requests
import json

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def home():
    load_css('styles.css')

    st.title('AI-Powered Farmer Assistant')
    st.markdown('<div class="home-content">',unsafe_allow_html=True) 
    st.markdown('## Welcome to the AI-Powered Farmer Assistant!')
    st.write("""
    Leveraging the power of AI, our platform provides farmers with intelligent recommendations to enhance crop productivity and manage resources efficiently.
    Explore our features to get started on your journey towards smarter farming!
    """)
    
    st.write("""
        ### Features:
        """)
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
            st.image('img/crop_recommendation_img.jpg', width=80)
            st.write("""
            **Crop Recommendation**
            Get personalized crop recommendations based on soil and climate conditions.
            """)

    with col2:
            st.image('img/fertilizer_recomendation_img.png', width=80)
            st.write("""
            **Fertilizer Recommendation**
            Receive optimized fertilizer suggestions tailored to your crops and soil type.
            """)

    with col3:
            st.image('img/plant_disease_detecting.jpg', width=80)
            st.write("""
            **Plant Disease Detection**
            Detect and diagnose plant diseases early using AI-powered image recognition.
            """)

    with col4:
            st.image('img/crop_yield_recommendation_img.png', width=80)
            st.write("""
            **Crop Yield Prediction**
            Predict crop yields based on various factors such as soil and weather conditions.
            """)

    st.markdown('## About')
    st.markdown('<div class="home-content">', unsafe_allow_html=True)
    st.markdown('### Empowering Farmers with AI Technology')
    st.write("""
    The AI-Powered Farmer Assistant is a comprehensive platform designed to assist farmers in making informed decisions 
    about their crops and farming practices. Leveraging advanced AI algorithms, the platform provides recommendations and 
    insights to enhance crop productivity, optimize resource usage, and ensure sustainable farming practices.
    """)
    st.markdown('### Our Mission')
    st.write("""
    Our mission is to empower farmers with cutting-edge technology, enabling them to achieve better yields, reduce costs, 
    and promote sustainable agriculture. By integrating AI with traditional farming practices, we aim to create a smarter, 
    more efficient agricultural ecosystem.
    """)
    st.markdown('### Our Team')
    st.write("""
    The AI-Powered Farmer Assistant is developed by a dedicated team of agricultural experts, data scientists, and 
    software engineers. Our team combines expertise in AI and farming to create a platform that addresses the unique 
    challenges faced by modern farmers.
    """)
    
def crop_recommendation():
    st.header('Crop Recommendation')
    model = joblib.load('crop reccommendetion\crop_recommendation_model.pkl')

    N = st.slider('**Nitrogen (N)**', min_value=0.0, value=0.0)
    P = st.slider('**Phosphorus (P)**', min_value=0.0, value=0.0)
    K = st.slider('**Potassium (K)**', min_value=0.0, value=0.0)
    temperature = st.slider('**Temperature (°C)**', min_value=0.0, value=25.0)
    humidity = st.slider('**Humidity (%)**', min_value=0.0, max_value=100.0, value=50.0)
    ph = st.slider('**Soil pH**', min_value=0.0, max_value=14.0, value=7.0)
    rainfall = st.slider('**Rainfall (mm)**', min_value=0.0, value=100.0)

    features = pd.DataFrame([[N, P, K, temperature, humidity,ph, rainfall]], 
                            columns=['N', 'P', 'K', 'temperature', 'ph', 'humidity', 'rainfall'])
    if st.button('Recommend Crop'):
        crop_prediction = model.predict(features)
        st.write(f'Recommended Crop: **{crop_prediction[0]}**')
    


def fertilizer_recommendation():

    model_path = r'fertilizer reccomendetion\fertilizer_recommendation_model.pkl'
    fertilizer_model = joblib.load( model_path)
    data = pd.read_csv('fertilizer reccomendetion\Fertilizer Prediction.csv')

    st.header('Fertilizer Recommendation')
    nitrogen = st.slider('**Nitrogen (N)**', min_value=0.0, value=0.0)
    phosphorus = st.slider('**Phosphorus (P)**', min_value=0.0, value=0.0)
    potassium = st.slider('**Potassium (K)**', min_value=0.0, value=0.0)
    temperature = st.slider('**Temperature**', min_value=0.0, value=25.0)
    humidity = st.slider('**Humidity**', min_value=0.0, max_value=100.0, value=50.0)
    soil_type = st.selectbox('**Select Soil Type**', options=data['Soil Type'].unique())
    crop_type = st.selectbox('**Select Crop Type**',options= data["Crop Type"].unique())

    input_data = pd.DataFrame({
        'Nitrogen': [nitrogen],
        'Phosphorus': [phosphorus],
        'Potassium': [potassium],
        'Temperature': [temperature],
        'Humidity': [humidity],
        'Soil Type': [soil_type],
        'Crop Type': [crop_type]
    })

    if st.button('Recommend Fertilizer'):
        fertilizer_prediction = fertilizer_model.predict(input_data)
        st.write(f'Recommended Fertilizer: **{fertilizer_prediction[0]}**')


model = load_model('New Plant Diseases Dataset(Augmented)/plant_disease_model.h5')

class_names = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy',
'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot',
'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)',
'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch',
'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'] 

def preprocess_image(image):
    image = image.resize((150, 150))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def plant_disease_detection():
    st.header('Plant Disease Detection') 
    uploaded_file = st.file_uploader('**Choose an image...**', type='jpg')

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        if st.button('Detect Disease'):
            processed_image = preprocess_image(image)
            prediction = model.predict(processed_image)
            predicted_class = class_names[np.argmax(prediction)]
            st.write(f'The plant is predicted to have: **{predicted_class}**')

def crop_yield_prediction():
    data = pd.read_csv('crop yield predictor\crop_yield.csv')

    numerical_features = ["Crop_Year","Area","Production","Annual_Rainfall","Fertilizer","Pesticide"]  
    categorical_features = ['Season','Crop',"State"]
    
    yield_model = joblib.load('crop yield predictor\crop_yield_model.pkl')
    
    st.header('Crop Yield Prediction') 
    Crop_Year = st.slider('**enter the year**', min_value=1900, max_value=2100, value=2023)
    Area = st.slider('**enter the Area**', min_value=0.0, value=1.0)
    Production =st.slider('**enter production**',min_value=0.0, value=1000.0)
    Annual_Rainfall = st.slider('**Rainfall (mm)**', min_value=0.0, max_value=500.0, value=100.0)
    Fertilizer = st.slider('**enter the Fertilizer**',min_value=0.0, value=50.0)
    Pesticide = st.slider('**enter the Pesticide**',min_value=0.0, value=10.0) 
    Crop = st.selectbox('**Crop**', options=data['Crop'].unique()) 
    Season = st.selectbox('**Season**', options=data['Season'].unique()) 
    State = st.selectbox('**State**', options=data['State'].unique())   
    features = pd.DataFrame([[Crop_Year,Area,Production,Annual_Rainfall,Fertilizer,Pesticide,Crop,Season,State]], 
                            columns=numerical_features + categorical_features)
    
    if st.button('Predict Yield'):
        predicted_yield = yield_model.predict(features)
        st.write(f'Predicted Crop Yield: **{predicted_yield[0]:.2f}**')

def store_contact_info(name, contact_number, email, query):
    server = 'contactinfoserver.database.windows.net'
    database = 'contact_info'
    username = 'nikhil'
    password = 'SQL@1234'
    driver= '{ODBC Driver 17 for SQL Server}'

    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Contacts (Name, ContactNumber, Email, Query) VALUES (?, ?, ?, ?)", (name, contact_number, email, query))
    conn.commit()
    conn.close()



def contact_us ():
    st.markdown("## AI Chat BOT")
    st.markdown("Ask me any question related to farming!")
    st.markdown("""
    <iframe src='https://webchat.botframework.com/embed/farmerbot-bot?s=C8KRN6CUcMU.qQsvHkz4NJRXiIfbzh0P4rU9VMKhmM3wLKWfJw9PffE'  style='min-width: 250px; width: 100%; min-height: 359px;'></iframe>
""", unsafe_allow_html=True)
    
    st.markdown("## Contact Us")
    st.markdown('<div class="home-content">',unsafe_allow_html=True)
    st.write("Please fill out the form below with your query or question.")
    name = st.text_input("Name")
    contact_number = st.text_input("Contact Number")
    email = st.text_input("Email ID")
    query = st.text_area("Query/Question")

    if st.button("Submit"):
        store_contact_info(name, contact_number, email, query)
        st.success("Your query has been submitted successfully!")






def main():
         
    st.sidebar.title("Navigator Tab")
    selection = st.sidebar.radio("**Features**",["**Home**", "**Crop Recommendation**", "**Fertilizer Recommendation**", "**Plant Disease Detection**", "**Crop Yield Prediction**","**contact us**"],index=0)
    
    if selection == "**Home**":
        home()
    elif selection == "**Crop Recommendation**":
        crop_recommendation()
    elif selection == "**Fertilizer Recommendation**":
        fertilizer_recommendation()
    elif selection == "**Plant Disease Detection**":
        plant_disease_detection()
    elif selection == "**Crop Yield Prediction**":
        crop_yield_prediction()
    elif selection == "**contact us**":
         contact_us()
         

if __name__ == '__main__':
    main()