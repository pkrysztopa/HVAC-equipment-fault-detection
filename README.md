# HVAC Equipment fault detection

<b> Most of the code, models and conclusions are done but project is still <u>in progress</u>. Things I'm currently working on: </b>
<ul>
<li>Thermostat sensor bias at notebook no. 4.</li>
<li>Expansion of the description with a graphical presentation of the analyzed data.</li>
<li>Expansion of the conclusions, especially in terms of practical applications of algorithms.</li>
</ul>

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


## Codes and Resources Used

- **Editor Used:**  Jupyter Notebook
- **Python Version:** 3.10

## Python Packages Used
- **General Purpose:** 'warnings, datetime, re'
- **Data Manipulation:** `pandas`
- **Data Visualization:** `seaborn, matplotlib`
- **Machine Learning:** `sklearn, scipy, catboost, xgboost`

# Data

The project is divided into 4 parts according to the division proposed by the authors in their description located in a file "LBNLDataSynthesisInventory.pdf". Each notebook uses slightly different data according to the diagram below:

```bash
├── 1. Simulated multi-zone variable air volume AHU data set - outside air temperature measurement bias.ipynb
│   ├── MZVAV-1.csv
├── 2. Experimental and simulated multi-zone variable air volume AHU data set.ipynb
│   ├── MZVAV-2-1.csv
│   ├── MZVAV-2-2.csv
├── 3. Experimental single-zone constant air volume AHU and single-zone variable air volume AHU dataset
│   ├── SZVAV.csv
│   ├── SZCAV.csv
├── 4. Experimental rooftop unit (RTU) data set
│   ├── RTU.csv
```

## Data Acquisition
Data was obtained from https://www.kaggle.com/datasets/claytonmiller/lbnl-automated-fault-detection-for-buildings-data.

# Code structure

```bash
├── data
│   ├── MZVAV-1.csv
│   ├── MZVAV-2-1.csv
│   ├── MZVAV-2-2.csv
│   ├── SZVAV.csv
│   ├── SZCAV.csv
│   ├── RTU.csv
├── notebooks
│   ├── 1. Simulated multi-zone variable air volume AHU data set - outside air temperature measurement bias.ipynb
│   ├── 2. Experimental and simulated multi-zone variable air volume AHU data set.ipynb
│   ├── 3. Experimental single-zone constant air volume AHU and single-zone variable air volume AHU dataset
│   ├── 4. Experimental rooftop unit (RTU) data set
├── src
│   ├── helper_functions.py
├── LBNLDataSynthesisInventory.pdf
├── README.md
```

# Results and evaluation
The notebooks contain a number of models for automatic fault detection in buildings using machine learning tools.
For most of the presented models, it was possible to find a practical application, with some exceptions or reservations, which will be discussed in detail later.

<b>1. Simulated multi-zone variable air volume AHU data set - outside air temperature measurement bias</b>

The introduced model has proven effective in addressing the challenge of Outside Air temperature sensor bias. It's important to acknowledge, however, that the applicability of this model is constrained to the specific system configuration. Attempting to employ such a model in alternative scenarios, such as where Air Handling Units (AHUs) provide a full 100 percent fresh air supply, would likely not yield good results.

It should also be borne in mind that the presented model was based on a simulated dataset and it is not obvious that the model will work correctly on data from a real building.

<b>2. Experimental and simulated multi-zone variable air volume AHU data set</b>
This notebook will contain an analysis of two distinct datasets, each corresponding to a different dataset type: experimental and simulated. Both datasets apply to a comparable building, which allows comparison between experimental and simulated scenarios.

The outcomes of the models had the remarkable performance of most models in this task, even without balancing or fine-tuning efforts. This trend suggests that the relationships between features and target data are easily recognizable, and the dataset is well-prepared. This implies that utilizing machine learning models for detecting such faults is likely to be straightforward and practical, as long as we have high quality data.

Regrettably, the limitation emerges that simulation data might not be suitable for model training. Models trained on an experimental data performed much worse on predicting outcomes based on simulated data and vice versa.
While generating data through simulation offers cost-effective benefits, the resulting model's efficacy is inherently constrained by the accuracy of the simulation model. This essentially creates a scenario where a model is based on another model, presenting limitations for real-world practicality. The ultimate requirement is to develop a model that closely mirrors reality, maximizing its usefulness in real-world applications.

In progress..

# Future work
In progress..

