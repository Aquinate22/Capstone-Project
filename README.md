
# Phase-5-**Capstone Project**

This is a collaborative project on:

# Disease Diagnosis and Prognosis (Breast Cancer)

Disease diagnosis and prognosis are important aspects of healthcare that involve determining the nature and severity of a patient's condition.
This project will mainly focus on the diagnosis of breast cancer using Machine Learning.


## Authors

- [@Ann Gitonga](https://github.com/anngitonga)

- [@Gloria Mutero](https://github.com/Wambui0001)

- [@Mitchelle Okubasu](https://github.com/Aquinate22)



## Project description: 
**Using Machine Learning and mammograms to detect breast cancer.**

The project aims to leverage the power of machine learning algorithms and mammograms to enhance the early detection of breast cancer. By developing a computer-aided diagnostic system, the project seeks to assist radiologists in accurately identifying and classifying abnormalities in mammograms, ultimately improving patient outcomes.


## Understanding Breast Cancer

![image](https://github.com/Aquinate22/Capstone-Project/assets/121969694/107bdda8-fc86-425f-a91d-79b294e90644)


 Breast cancer is a prevalent type of cancer that develops in the breast tissue, mainly in the ducts or lobules. It primarily affects women, but men can also develop breast cancer, although it is much rarer. Research shows that 1 in 8 women and 1 in 1000 men suffer from it. Breast cancer can vary widely in its behavior and response to treatment, which is why it is essential to detect and diagnose it at an early stage. Breast cancer can be classified as:

- Non-invasive (or in situ): When it stays localized to the area of the breast where it originated, without spreading through the surrounding breast tissue.
- Invasive: When the neoplasm is able to spread through the lymphatic system and blood.
Breast cancer is curable if detected early or in time. The treatment of breast cancer often consists of a combination of surgical removal, radiation therapy, and medication (such as hormonal therapy, chemotherapy, and targeted biological therapy) to treat the microscopic cancer that has spread from the breast tumor through the blood. Such treatment can prevent cancer growth and spread, thus saving lives. Generally, symptoms of breast cancer include:

- A breast lump
- Alteration in size, shape, or appearance of a breast
- Dimpling, redness, pitting, or other changes in the skin
- Changes in nipple appearance or alterations in the skin surrounding the nipple
- Abnormal nipple discharge.

A mammogram is an X-ray that checks for cancer in the breast tissue. Mammography images can reveal various features, such as:

 1. Calcifications: Tiny deposits of calcium in the breast tissue, which can be indicative of certain types of breast cancer.
 2. Masses or tumors: Abnormal growths or lumps in the breast tissue, which may be cancerous or non-cancerous.
 3. Architectural distortion: Distortions in the normal structure of breast tissue, which can be a sign of cancer.
 4. Microcalcifications: Small clusters of calcifications that may indicate early-stage breast cancer.
 5. Asymmetries: Differences in the appearance of breast tissue between the left and right breast, which may require further evaluation.

## Business Understanding
The development of our mammogram diagnosis and prognosis web app stems from an understanding of the challenges faced by healthcare professionals in interpreting mammograms and providing timely diagnoses for breast diseases.

By creating an app that harnesses the power of AI and machine learning, we aim to bridge this gap and hence provide a robust solution for healthcare professionals. Our app will leverage advanced algorithms and large datasets to enhance accuracy, consistency, and efficiency in mammogram interpretation.

The business value of our app lies in its ability to enable healthcare professionals with a reliable tool that expedites early detection and diagnosis of breast diseases. Medical professionals will be able to make quicker and more accurate decisions, facilitating early intervention, and potentially improving treatment success rates. Moreover, the app's real-time reporting and alerting capabilities will enable healthcare providers to prioritize urgent cases, ensuring timely intervention and reducing the risk of disease progression.

From a business perspective, our app has the potential to establish itself as an indispensable tool in the field of breast disease diagnosis. Its widespread adoption first in the Kenyan market could lead to increased efficiency in healthcare workflows, reduced healthcare costs associated with misdiagnosis and delayed treatment, and ultimately improved patient satisfaction and outcomes.

Overall, our app's business understanding revolves around addressing the existing challenges in mammogram interpretation, improving diagnostic accuracy, empowering healthcare professionals and ultimately contributing to the early detection and effective treatment of breast diseases.
## Goals/ Objectives:

- To develop a model that can assist in early detection of breast cancer.
- To improve the accuracy and precision of breast cancer diagnosis.
- Reducing the False Positive "recall" rates for mammograms.
## Data Understanding

In our project, we shall use mammogram images and their lables as our base of our web application. Mammograms are primarily used to identify any abnormalities or changes in breast tissue that may indicate the presence of a tumor or other abnormalities. The data set used can be downloaded from https://drive.google.com/file/d/12umDKmXJ8--ZmuiTrchSQRCs8SmRl12h/view?usp=sharing.

We extracted the zip file and got four files:

*  train - contains the images we will use to train our model.

*  Training_set.csv - this csv file has contains the labels for the training images

*  test - contains 1900+ images. We will use the images to test our model.

*  Testing_set.csv

*  sample_submission



Distribution of classes in the data

![image](https://github.com/Aquinate22/Capstone-Project/assets/121969694/d1905cae-d95c-47f5-a93f-12fda87eb0d5)

Combined classes into Benign and Malignant
Count of Class names

![image](https://github.com/Aquinate22/Capstone-Project/assets/121969694/3503a698-feb6-4827-bed2-16331df08b81)

**Benign Images**

![image](https://github.com/Aquinate22/Capstone-Project/assets/121969694/f0e67ad4-a3ee-4b9d-b0d0-2bc95903b524)

**Malignant Images**

![image](https://github.com/Aquinate22/Capstone-Project/assets/121969694/617be429-b10a-4dae-a454-e18802d90e55)



Next, advanced image processing techniques were employed to preprocess the mammogram images, extracting relevant features and reducing noise. This step helps in enhancing the quality and clarity of the images, enabling more accurate analysis.

# Modeling

**Convolutional Neural Networks**

Convolutional Neural Networks(CNNs) were then trained on the preprocessed mammogram dataset. These algorithms will learn patterns and features indicative of breast cancer from the images. By training the models on our dataset, they can generalize and detect subtle abnormalities in new, unseen mammograms.

**1. Base Model**

Architecture: 
* Four layers of Convolutional and MaxPooling followed by Flattenning and dense layers.

**2.  A more sophisticated Model**

*  Corrected class Imbalance
*  Set initial bias and class weights
*  Used the same number of Convolutional and MaxPooling layers and changes the number of neurons.

**3. Pretrained Model**
*  Used the VGG16 pre-trained model to train 


**Decision Tree**
* Trained the model using a Decision tree and improved the model by GridSearch.
  ![image](https://github.com/Aquinate22/Capstone-Project/assets/121969694/3fdccf13-4308-4bbf-9501-7115d1a71296)


## Evaluation

Once the models were trained, they were evaluated and validated using separate datasets to assess their performance. 

Evaluation metrics used:
*  Loss
*  Accuracy
*  Precision
*  Recall

  ![image](https://github.com/Aquinate22/Capstone-Project/assets/121969694/3a13f1b9-4598-49d6-81b6-08237d864016)
  ![image](https://github.com/Aquinate22/Capstone-Project/assets/121969694/deca547c-237a-4da3-b6f6-f54147a829ef) ![image](https://github.com/Aquinate22/Capstone-Project/assets/121969694/ef1234f7-7647-4c00-9349-7a2fe031e458)


  
# Deployment
Deployed our model on Streamlit.
 Developed a user-friendly interface that integrates the trained machine learning models into the existing workflow of radiologists. The interface will allow radiologists to upload mammograms and receive real-time predictions and risk assessments, aiding in their decision-making process.
