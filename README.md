# Fundamentals of Data Science Experiments (CS23334)

Lab experiments for **CS23334 – Fundamentals of Data Science**.

Every experiment is available in three forms:

| Folder | What it has |
|---|---|
| [`notebooks/`](notebooks) | Jupyter notebooks **already executed** – code, printed output and graphs are saved inside, so they display directly on GitHub |
| [`code/`](code) | Plain Python scripts (`.py`) – run any of them live |
| [`docs/`](docs) | Lab record PDFs with aim, description, code and sample output |
| [`data/`](data) | All datasets (CSV) used by the experiments |

## Experiments

| Exp | Title | Notebook | Script | Record |
|---|---|---|---|---|
| 1a | Trend of data science job postings over the last decade | [ipynb](notebooks/exp01a_job_postings_trend.ipynb) | [py](code/exp01a_job_postings_trend.py) | [pdf](docs/01a-FDS_Experiment.pdf) |
| 1b | Distribution of data science roles | [ipynb](notebooks/exp01b_roles_distribution.ipynb) | [py](code/exp01b_roles_distribution.py) | [pdf](docs/01b-FDS_Experiment.pdf) |
| 1c | Structured, unstructured and semi-structured data | [ipynb](notebooks/exp01c_structured_unstructured.ipynb) | [py](code/exp01c_structured_unstructured.py) | [pdf](docs/01c-FDS_Experiment.pdf) |
| 1d | Encrypt and decrypt sensitive data | [ipynb](notebooks/exp01d_encrypt_decrypt.ipynb) | [py](code/exp01d_encrypt_decrypt.py) | [pdf](docs/01d-FDS_Experiment.pdf) |
| 3a | Data visualization – line plot | [ipynb](notebooks/exp03a_line_plot.ipynb) | [py](code/exp03a_line_plot.py) | [pdf](docs/03a-FDS_Experiment.pdf) |
| 3b | Data visualization – bar chart | [ipynb](notebooks/exp03b_bar_chart.ipynb) | [py](code/exp03b_bar_chart.py) | [pdf](docs/03b-FDS_Experiment.pdf) |
| 3c | Data visualization – pie chart | [ipynb](notebooks/exp03c_pie_chart.ipynb) | [py](code/exp03c_pie_chart.py) | [pdf](docs/03c-FDS_Experiment.pdf) |
| 4 | Word frequency in a body of text (NLTK) | [ipynb](notebooks/exp04_word_frequency.ipynb) | [py](code/exp04_word_frequency.py) | [pdf](docs/04-FDS_Experiment.pdf) |
| 5 | Data collection and initial exploration (diabetes) | [ipynb](notebooks/exp05_diabetes_exploration.ipynb) | [py](code/exp05_diabetes_exploration.py) | [pdf](docs/05-FDS_Experiment.pdf) |
| 6 | Time series analysis of website traffic | [ipynb](notebooks/exp06_website_traffic_timeseries.ipynb) | [py](code/exp06_website_traffic_timeseries.py) | [pdf](docs/06-FDS_Experiment.pdf) |
| 7 | Random sampling and sampling distribution | [ipynb](notebooks/exp07_sampling_distribution.ipynb) | [py](code/exp07_sampling_distribution.py) | [pdf](docs/07-FDS_Experiment.pdf) |
| 8 | Z-test | [ipynb](notebooks/exp08_z_test.ipynb) | [py](code/exp08_z_test.py) | [pdf](docs/08-FDS_Experiment.pdf) |
| 9 | Matplotlib use cases (Iris dataset) | [ipynb](notebooks/exp09_matplotlib_iris.ipynb) | [py](code/exp09_matplotlib_iris.py) | [pdf](docs/09-FDS_Experiment.pdf) |
| 10 | NumPy array functions | [ipynb](notebooks/exp10_numpy_arrays.ipynb) | [py](code/exp10_numpy_arrays.py) | [pdf](docs/10-FDS_Experiment.pdf) |
| 11 | Pandas DataFrame use cases | [ipynb](notebooks/exp11_pandas_dataframes.ipynb) | [py](code/exp11_pandas_dataframes.py) | [pdf](docs/11-FDS_Experiment.pdf) |
| 12 | Outlier detection (IQR) | [ipynb](notebooks/exp12_outlier_detection.ipynb) | [py](code/exp12_outlier_detection.py) | [pdf](docs/12-FDS_Experiment.pdf) |
| 13 | Handling missing and inappropriate data | [ipynb](notebooks/exp13_missing_inappropriate_data.ipynb) | [py](code/exp13_missing_inappropriate_data.py) | [pdf](docs/13-FDS_Experiment.pdf) |
| 14 | Feature scaling | [ipynb](notebooks/exp14_feature_scaling.ipynb) | [py](code/exp14_feature_scaling.py) | [pdf](docs/14-FDS_Experiment.pdf) |
| 15 | Data preprocessing | [ipynb](notebooks/exp15_data_preprocessing.ipynb) | [py](code/exp15_data_preprocessing.py) | [pdf](docs/15-FDS_Experiment.pdf) |
| 16 | EDA – quantitative and qualitative analysis | [ipynb](notebooks/exp16_eda_quantitative_qualitative.ipynb) | [py](code/exp16_eda_quantitative_qualitative.py) | [pdf](docs/16-FDS_Experiment.pdf) |
| 17 | Linear regression | [ipynb](notebooks/exp17_linear_regression.ipynb) | [py](code/exp17_linear_regression.py) | [pdf](docs/17-FDS_Experiment.pdf) |
| 18 | KNN algorithm | [ipynb](notebooks/exp18_knn.ipynb) | [py](code/exp18_knn.py) | [pdf](docs/18-FDS_Experiment.pdf) |
| 19 | Logistic regression | [ipynb](notebooks/exp19_logistic_regression.ipynb) | [py](code/exp19_logistic_regression.py) | [pdf](docs/19-FDS_Experiment.pdf) |
| 20 | K-means clustering | [ipynb](notebooks/exp20_kmeans_clustering.ipynb) | [py](code/exp20_kmeans_clustering.py) | [pdf](docs/20-FDS_Experiment.pdf) |

## How to run

```bash
pip install -r requirements.txt
cd code
python3 exp08_z_test.py
```

Or open all notebooks with `jupyter notebook notebooks/`.
