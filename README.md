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

Step 4: after the deployment completed go to the Azure AI Language studio and sign in with azure account > clicked on create new project > selected custom question answeing
![5](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/a1dad527-0bd5-4dff-97f7-21460e782e8a)

Step 5: filled necessary details like name and description > clicked on next to review and finish > clicked on create project
![6](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/28027d07-c37e-4dee-a85a-9598ea69c7d0)

Step 6: After creating project gone to the project > clicked on Edit knowledge base > clicked on add symbol to add new question answer pairs > filled question input field with question and answer field with answer > clicked on done
![7](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/2d966d46-568f-44a8-9c73-ec2950bf96df)

Followed step 7 to add 50 questions > clicked on save button

Step 8: after the saved knowledge base gone to deploy knowledge based tab > clicked on deploy to deploy knowledge base > clicked on create boat
![8](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/2b221080-86a2-43fc-a267-a5f035d6ad56)

#4)created web app for deploy AI chat bot:

Step1: after the clicked create chat boat we redirected to the azure portal > signed into the azure account > on Custom deployment > in basic tab filled the required detail like subscription, resource group, Bot handle, Pricing tier and creation type etc.. > clicked on next
![9](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/f435cbad-b390-48fc-8db1-3fd4074720b3)

>in web app tab filled necessary details like app name, sdk language selection, creation type, app service plan, language resource key and for the language resource key we needed to gone to the language chat bot that we created > management resource > keys and end point > copy key1and paste in input field of language resource key > review and create.
![10](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/963f3247-4c3a-4331-803f-ce882503b7c1)
![11](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/4cdca076-2259-48f5-9972-2b686b39404b)

#5)azure SQL server and database (to store farmer query/question with name, phone no. and email ID):

Step1: gone to the azure portal and login with account > searched for sql server > clicked on sql server > in sql server clicked on create > filled the naccesary detail like server name and location > authentication method = use sql authentication > create admin login with password > clicked on create
![12](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/778a735c-82a1-466f-b08c-da695d9feb48)

Step 2: searched for sql database > clicked on sql database > clicked on create >
filled the necessary detail like subscription, resource group, database name, server that we created > clicked on create button
![13](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/3bab0003-b3b4-4cb4-aad1-78f8a9929dc3)

go to the created sql database > clock on Query editor > authenticate with password > create table that store farmer query with personal detail like name, mobile no. and email id.

#Website Overview
#This is Our Home Page:
![Screenshot 2024-06-14 103313](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/343f220c-d92c-41de-b7b6-ecfd5b4bc468)
![Screenshot 2024-06-14 103343](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/763ebfe0-b7b0-424b-9842-fe0c7425ff71)

#Our Services
![Screenshot 2024-06-14 115640](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/0151a15c-4c55-4e5c-a7fd-ac8be1937736)

#Crop Recommendation
![Screenshot 2024-06-14 103559](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/093af84a-ae3e-4269-a9de-91f5d1f25144)

#Fertilizer Recommendation
![Screenshot 2024-06-14 103858](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/d1c55826-cbd0-47d2-aaf6-f7ce81f3c779)

#Plant Disease Detection
![Screenshot 2024-06-14 104331](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/160fa621-efc7-4d09-bf73-61ddf353dc89)

#Crop Yield Prediction
![Screenshot 2024-06-14 104429](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/12241326-e97b-4f23-bdff-5a708ef6e2c3)

#contact us
![Screenshot 2024-06-14 104559](https://github.com/Panu08/ai-farmer-assistant/assets/169903566/8d893578-8c0c-4527-80e1-27a27526d21b)

This is the AI-POWERED FARMER ASSISTANT Website Project created for internship purposes.

















