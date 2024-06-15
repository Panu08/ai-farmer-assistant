# Ai-Powered-Farmer-Assistant
# Working Links for the Project
Web Application hosted on Azure -> http://172.206.206.95:8501

Github Repository -> https://github.com/Panu08/ai-farmer-assistant
# Project Aim
The AI-Powered Farmer Assistant web application is designed to support farmers in making data-driven decisions to enhance agricultural productivity and sustainability. 

This document provides an in-depth guide to the application’s features, architecture, deployment, and usage. Detailing the core functionalities of the application, including crop recommendation, fertilizer recommendation, plant disease detection, and crop yield prediction.


The primary purpose of the AI-Powered Farmer Assistant web app is to leverage advanced artificial intelligence and machine learning technologies to assist farmers in making informed decisions to enhance agricultural productivity and sustainability.
# Azure Services Used
1.Azure AI Service (An ai service(chatbot) integrated into the website)

2.Azure Webapp Service

3.Azure SQL Database Sevice (To Store the data into an SQL database)

4.Azure Virtual Network 

5.Azure Virtual Machine 
# Web Tecnologies Used
1.Python

2.CSS

3.Streamlit
# Resource Visualizer
![project](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/38545cf1-f569-4f9d-a9f4-4705b74c4eb8)

# Azure Resources overview
#1) Created virtual network (for resource group and virtual machine):

step 1: signed into azure portal > search for virtual network > gone to virtual network service and clicked on create > in basic tab filled the necessary details like subscription, resource group, virtual network name and region etc... > clicked on review and create.

![14](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/1e62eeb0-25b3-4a64-864e-ec0807379304)

#2) Created virtual machine (for deploy the project):

step 1: signed into azure portal > search for virtual machine > gone to virtual machine service and clicked on create > in basic tab filled the necessary details like subscription, resource group, virtual machine name, region and selected Availability options =No infrastructure redundancy required, image = window server 2022 > size Standard_E2s_v3 - 2 vcpus, 16 GiB memory and authenticate virtual machine with username and password > select public inbound port = Allow selected ports and select all port > go to the networking tab and check the created virtual network are assigned or not > clicked on review and create.

Step 2: to added streamlit server port like 8501 into inbound security rule > gone to the created virtual machine > in networking tab clicked on network setting and then clicked on network security group > in virtual machine nsg go to the setting and clicked on inbound security rule > add to Add inbound security rule and add the 8501 streamlit server port >
filled the necessary detail that shown in screen short > add
![14](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/3de51292-8211-4477-8c2e-734493c57c92)
![15](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/7065a4e1-3700-4683-a841-5d84681506a2)
![16](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/684065fe-c640-4147-91fa-df22e797e380)

#3)created chat bot using azure AI language service:

step 1: signed into azure portal > clicked on create resource > searched for language service > clicked on create > click on language service
![1](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/eb279dae-00d2-467d-adf5-09ffdca190ea)

Step 2: on select additional feature > selected Custom question answering > clicked on continue to create your resource
![2](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/bfef1569-2124-4452-8a97-9a96eca7088d)

Step 3: on Create Language here we filled the necessary details like subscription, resource group, name, Pricing tier and azure Search Pricing tier etc.. > clicked on review + create
![3](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/7babbce9-2cf5-474b-9263-3deda2db057b)








