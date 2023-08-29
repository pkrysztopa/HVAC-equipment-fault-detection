# HVAC Equipment fault detection

# Project Overview

Typical fault detection in the building management systems (BMS) relies on hard-coded algorithms. The advantage of such a solutions is the simplicity of their implementation, the disadvantage that they usually detect faults when they are already advanced and costly to remove. The elements of effective preventive maintenance however should be an algorithms that can detect such defects early enough before the problem becomes serious. Such algorithms have to calculate more complex dependencies than typical algorithms. The use of machine learning tools can be effective to develop such algorithms and this project focuses on the development of such tools. The project tries out various methods that will be able to effectively detect a number of different faults.

In this project, the data mostly will be used to: 
<ul>
<li>test their usefulness in terms of detecting faults in the given building systems,</li>
<li>examining the methods of building algorithms for automatic fault detection,</li>
<li>consideration of practical application of this type of algorithms.</li>
</ul>

This data were collected according to this publication: https://www.nature.com/articles/s41597-020-0398-6.
Below is a description of the dataset from the above publication.
<details>
<summary>Click here to see a description of the dataset from the above publication.</summary>


  <b>Abstract</b>

It is estimated that approximately 4–5% of national energy consumption can be saved through corrections to existing commercial building controls infrastructure and resulting improvements to efficiency. Correspondingly, automated fault detection and diagnostics (FDD) algorithms are designed to identify the presence of operational faults and their root causes. A diversity of techniques is used for FDD spanning physical models, black box, and rule-based approaches. A persistent challenge has been the lack of common datasets and test methods to benchmark their performance accuracy. This article presents a first of its kind public dataset with ground-truth data on the presence and absence of building faults. This dataset spans a range of seasons and operational conditions and encompasses multiple building system types. It contains information on fault severity, as well as data points reflective of the measurements in building control systems that FDD algorithms typically have access to. The data were created using simulation models as well as experimental test facilities, and will be expanded over time.

  <b>Methods</b>

The dataset comprises of five air-handling units (AHUs) and roof top units heating ventilation and air conditioning (RTU HVAC) system types, created through simulation or physical experimental facilities. The simulated datasets were created from HVACSIM+ and a EnergyPlus-Modelica co-simulation. The experimental datasets were created from three experimental research facilities: Lawrence Berkeley National Laboratory in Berkeley, California, Oak Ridge National Laboratory in Oak Ridge Tennessee and Iowa Energy Center in Ames City, Iowa.
Data Records

The data is stored on figshmare and OpenEl. Each CSV file represents a single combination of system configuration and experimental or simulated data creation approach. The creation approach can be found under file details. The datasets are minute-frequency time series measurements of the system operational parameters that are most commonly available to automated fault detection and diagnostics (FDD) algorithms in typical commercial buildings. The first column of each file consists of time stamp, and is presented in the format m/d/yy h:mm. The last column of each file consists of a binary indicator of the ground truth information on whether or not a fault is present.

</details>

# Installation and Setup

In this section, provide detailed instructions on how to set up the project on a local machine. This includes any necessary dependencies, software requirements, and installation steps. Make sure to include clear and concise instructions so that others can easily replicate your setup.

I like to structure it as below - 

## Codes and Resources Used

- **Editor Used:**  Jupyter Notebook
- **Python Version:** 3.10

## Python Packages Used
- **General Purpose:** 'warnings, datetime, re'
- **Data Manipulation:** `pandas`
- **Data Visualization:** `seaborn, matplotlib`
- **Machine Learning:** `sklearn, scipy, catboost, xgboost`

# Data

The project is divided into 4 parts. This division is consistent with the division proposed in the description provided by the authors.

## Source Data
In this section, I list all of the data that was used, along with the source link and a few lines that describe each data. You can also explain each of the data attributes in greater detail if you wish.

## Data Acquisition
Data collection is not always as simple as downloading from Kaggle or any open source website; it can also be gathered through API calls or online scraping. So you can elaborate on this step in this section so that the reader can obtain the dataset by following your instructions.

## Data Preprocessing
Acquired data is not always squeaky clean, so preprocessing them are an integral part of any data analysis. In this section you can talk about the same.

# Code structure
Project is divided

```bash
├── data
│   ├── data1.csv
│   ├── data2.csv
│   ├── cleanedData
│   │   ├── cleaneddata1.csv
|   |   └── cleaneddata2.csv
├── data_acquisition.py
├── data_preprocessing.ipynb
├── data_analysis.ipynb
├── data_modelling.ipynb
├── Img
│   ├── img1.png
│   ├── Headerheader.jpg
├── LICENSE
├── README.md
└── .gitignore
```

# Results and evaluation
Provide an overview of the results of your project, including any relevant metrics and graphs. Include explanations of any evaluation methodologies and how they were used to assess the quality of the model. You can also make it appealing by including any pictures of your analysis or visualizations.

# Future work
Outline potential future work that can be done to extend the project or improve its functionality. This will help others understand the scope of your project and identify areas where they can contribute.

# Acknowledgments/References
Acknowledge any contributors, data sources, or other relevant parties who have contributed to the project. This is an excellent way to show your appreciation for those who have helped you along the way.

For instance, I am referencing the image that I used for my readme header - 
- Image by [rashadashurov](https://www.vectorstock.com/royalty-free-vector/data-science-cartoon-template-with-flat-elements-vector-27984292)

# License
Specify the license under which your code is released. Moreover, provide the licenses associated with the dataset you are using. This is important for others to know if they want to use or contribute to your project. 

For this github repository, the License used is [MIT License](https://opensource.org/license/mit/).
