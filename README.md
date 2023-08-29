# HVAC Equipment fault detection

<b> Project still <u>in progress</u>. Things I'm currently working on: </b>
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

In progress...

## Source Data
In progress...

## Data Acquisition
In progress..

## Data Preprocessing
In progress..

# Code structure
The project is divided into 4 parts according to the division proposed by the authors in their description. Each notebook uses slightly different data.

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
├── README.md
```

# Results and evaluation
In progress..

# Future work
In progress..

# License
In progress..
