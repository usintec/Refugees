# Refugee and Host Community Survey Analysis

## Overview

This repository contains an exploratory data analysis (EDA) and
statistical analysis of the **Questionnaire for Refugees and Host
Community Members** dataset.

### Objectives

-   Assess data quality and completeness.
-   Profile respondent demographics.
-   Explore perceptions of security, integration, and community
    relations.
-   Produce publication-ready tables and figures.

## Dataset Summary

  -----------------------------------------------------------------------
  Attribute                                                         Value
  ------------------------------ ----------------------------------------
  File                                                 Questionnaire.xlsx

  Responses                                                           185

  Variables                                                            17

  Format                                          Microsoft Excel (.xlsx)

  Population                       Cameroonian refugees and Nigerian host
                                                        community members
  -----------------------------------------------------------------------

> Some questionnaire items are intentionally unanswered because of
> **skip logic** (e.g., refugee-only or host-community-only questions).
> These should be interpreted as *Not Applicable* rather than missing
> data.

## Repository Structure

``` text
.
├── data/
├── notebooks/
├── scripts/
├── outputs/
│   ├── tables/
│   ├── figures/
│   └── reports/
├── requirements.txt
└── README.md
```

## Workflow

1.  Data import
2.  Data profiling
3.  Missing value assessment
4.  Demographic analysis
5.  Descriptive statistics
6.  Visualizations
7.  Inferential statistics
8.  Reporting

## Analyses

### Data Quality

-   Dataset dimensions
-   Variable types
-   Missing-value assessment
-   Duplicate detection
-   Completeness assessment

### Demographic Analysis

-   Age distribution
-   Gender
-   Nationality
-   Respondent category
-   Duration of residence

### Security and Social Analysis

-   Safety perception
-   Security threats
-   Crime and violence
-   Refugee-host relationships
-   Integration opportunities
-   Government support
-   Recommendations

## Planned Statistical Methods

  Objective                                   Method
  ------------------------------------------- ----------------------------------------
  Frequency summaries                         Frequency tables & percentages
  Association between categorical variables   Chi-square test
  Cross-group comparisons                     Crosstabulations
  Visualization                               Bar charts, pie charts, stacked charts
  Open-ended responses                        Thematic analysis

## Outputs

The project produces: - Frequency tables - Percentage distributions -
Missing-value summaries - Publication-quality charts - Statistical test
results

## Requirements

``` bash
pip install pandas numpy matplotlib seaborn openpyxl missingno jupyter scipy
```

## License

Academic and research use only.
