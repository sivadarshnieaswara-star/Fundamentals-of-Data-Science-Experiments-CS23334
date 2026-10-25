# Fundamentals of Data Science Experiments (CS23334)

Lab experiments for **CS23334 – Fundamentals of Data Science**.

Every experiment file is in the main folder, named by its experiment number:

| File / Folder | What it has |
|---|---|
| `expXX.ipynb` | Jupyter notebooks **already executed** – code, printed output and graphs are saved inside, so they display directly on GitHub |
| `expXX.py` | Plain Python scripts – run any of them live |
| [`pics/`](pics) | Output pictures (graphs and printed output) for every experiment |
| [`docs/`](docs) | Lab record PDFs with aim, description, code and sample output |
| [`data/`](data) | All datasets (CSV) used by the experiments |

## Experiments

| Exp | Title | Notebook | Script | Record |
|---|---|---|---|---|
| 1a | Trend of data science job postings over the last decade | [ipynb](exp01a.ipynb) | [py](exp01a.py) | [pdf](docs/exp01a.pdf) |
| 1b | Distribution of data science roles | [ipynb](exp01b.ipynb) | [py](exp01b.py) | [pdf](docs/exp01b.pdf) |
| 1c | Structured, unstructured and semi-structured data | [ipynb](exp01c.ipynb) | [py](exp01c.py) | [pdf](docs/exp01c.pdf) |
| 1d | Encrypt and decrypt sensitive data | [ipynb](exp01d.ipynb) | [py](exp01d.py) | [pdf](docs/exp01d.pdf) |
| 3a | Data visualization – line plot | [ipynb](exp03a.ipynb) | [py](exp03a.py) | [pdf](docs/exp03a.pdf) |
| 3b | Data visualization – bar chart | [ipynb](exp03b.ipynb) | [py](exp03b.py) | [pdf](docs/exp03b.pdf) |
| 3c | Data visualization – pie chart | [ipynb](exp03c.ipynb) | [py](exp03c.py) | [pdf](docs/exp03c.pdf) |
| 4 | Word frequency in a body of text (NLTK) | [ipynb](exp04.ipynb) | [py](exp04.py) | [pdf](docs/exp04.pdf) |
| 5 | Data collection and initial exploration (diabetes) | [ipynb](exp05.ipynb) | [py](exp05.py) | [pdf](docs/exp05.pdf) |
| 6 | Time series analysis of website traffic | [ipynb](exp06.ipynb) | [py](exp06.py) | [pdf](docs/exp06.pdf) |
| 7 | Random sampling and sampling distribution | [ipynb](exp07.ipynb) | [py](exp07.py) | [pdf](docs/exp07.pdf) |
| 8 | Z-test | [ipynb](exp08.ipynb) | [py](exp08.py) | [pdf](docs/exp08.pdf) |
| 9 | Matplotlib use cases (Iris dataset) | [ipynb](exp09.ipynb) | [py](exp09.py) | [pdf](docs/exp09.pdf) |
| 10 | NumPy array functions | [ipynb](exp10.ipynb) | [py](exp10.py) | [pdf](docs/exp10.pdf) |
| 11 | Pandas DataFrame use cases | [ipynb](exp11.ipynb) | [py](exp11.py) | [pdf](docs/exp11.pdf) |
| 12 | Outlier detection (IQR) | [ipynb](exp12.ipynb) | [py](exp12.py) | [pdf](docs/exp12.pdf) |
| 13 | Handling missing and inappropriate data | [ipynb](exp13.ipynb) | [py](exp13.py) | [pdf](docs/exp13.pdf) |
| 14 | Feature scaling | [ipynb](exp14.ipynb) | [py](exp14.py) | [pdf](docs/exp14.pdf) |
| 15 | Data preprocessing | [ipynb](exp15.ipynb) | [py](exp15.py) | [pdf](docs/exp15.pdf) |
| 16 | EDA – quantitative and qualitative analysis | [ipynb](exp16.ipynb) | [py](exp16.py) | [pdf](docs/exp16.pdf) |
| 17 | Linear regression | [ipynb](exp17.ipynb) | [py](exp17.py) | [pdf](docs/exp17.pdf) |
| 18 | KNN algorithm | [ipynb](exp18.ipynb) | [py](exp18.py) | [pdf](docs/exp18.pdf) |
| 19 | Logistic regression | [ipynb](exp19.ipynb) | [py](exp19.py) | [pdf](docs/exp19.pdf) |
| 20 | K-means clustering | [ipynb](exp20.ipynb) | [py](exp20.py) | [pdf](docs/exp20.pdf) |

## How to run

```bash
pip install -r requirements.txt
python3 exp08.py
```

Or open all notebooks with `jupyter notebook`.

## Output pictures

### Exp 1a – Trend of data science job postings over the last decade

![exp01a_output.png](pics/exp01a_output.png)
![exp01a_graph1.png](pics/exp01a_graph1.png)

### Exp 1b – Distribution of data science roles

![exp01b_graph1.png](pics/exp01b_graph1.png)

### Exp 1c – Structured, unstructured and semi-structured data

![exp01c_output.png](pics/exp01c_output.png)

### Exp 1d – Encrypt and decrypt sensitive data

![exp01d_output.png](pics/exp01d_output.png)

### Exp 3a – Data visualization – line plot

![exp03a_graph1.png](pics/exp03a_graph1.png)

### Exp 3b – Data visualization – bar chart

![exp03b_graph1.png](pics/exp03b_graph1.png)

### Exp 3c – Data visualization – pie chart

![exp03c_graph1.png](pics/exp03c_graph1.png)

### Exp 4 – Word frequency in a body of text (NLTK)

![exp04_output.png](pics/exp04_output.png)

### Exp 5 – Data collection and initial exploration (diabetes)

![exp05_output.png](pics/exp05_output.png)
![exp05_graph1.png](pics/exp05_graph1.png)
![exp05_graph2.png](pics/exp05_graph2.png)

### Exp 6 – Time series analysis of website traffic

![exp06_output.png](pics/exp06_output.png)
![exp06_graph1.png](pics/exp06_graph1.png)
![exp06_graph2.png](pics/exp06_graph2.png)
![exp06_graph3.png](pics/exp06_graph3.png)
![exp06_graph4.png](pics/exp06_graph4.png)
![exp06_graph5.png](pics/exp06_graph5.png)

### Exp 7 – Random sampling and sampling distribution

![exp07_output.png](pics/exp07_output.png)
![exp07_graph1.png](pics/exp07_graph1.png)

### Exp 8 – Z-test

![exp08_output.png](pics/exp08_output.png)

### Exp 9 – Matplotlib use cases (Iris dataset)

![exp09_output.png](pics/exp09_output.png)
![exp09_graph1.png](pics/exp09_graph1.png)
![exp09_graph2.png](pics/exp09_graph2.png)
![exp09_graph3.png](pics/exp09_graph3.png)
![exp09_graph4.png](pics/exp09_graph4.png)
![exp09_graph5.png](pics/exp09_graph5.png)
![exp09_graph6.png](pics/exp09_graph6.png)
![exp09_graph7.png](pics/exp09_graph7.png)
![exp09_graph8.png](pics/exp09_graph8.png)

### Exp 10 – NumPy array functions

![exp10_output.png](pics/exp10_output.png)

### Exp 11 – Pandas DataFrame use cases

![exp11_output1.png](pics/exp11_output1.png)
![exp11_output2.png](pics/exp11_output2.png)

### Exp 12 – Outlier detection (IQR)

![exp12_output.png](pics/exp12_output.png)
![exp12_graph1.png](pics/exp12_graph1.png)
![exp12_graph2.png](pics/exp12_graph2.png)
![exp12_graph3.png](pics/exp12_graph3.png)
![exp12_graph4.png](pics/exp12_graph4.png)

### Exp 13 – Handling missing and inappropriate data

![exp13_output1.png](pics/exp13_output1.png)
![exp13_output2.png](pics/exp13_output2.png)
![exp13_output3.png](pics/exp13_output3.png)

### Exp 14 – Feature scaling

![exp14_output1.png](pics/exp14_output1.png)
![exp14_output2.png](pics/exp14_output2.png)

### Exp 15 – Data preprocessing

![exp15_output1.png](pics/exp15_output1.png)
![exp15_output2.png](pics/exp15_output2.png)

### Exp 16 – EDA – quantitative and qualitative analysis

![exp16_output.png](pics/exp16_output.png)
![exp16_graph1.png](pics/exp16_graph1.png)
![exp16_graph2.png](pics/exp16_graph2.png)
![exp16_graph3.png](pics/exp16_graph3.png)
![exp16_graph4.png](pics/exp16_graph4.png)
![exp16_graph5.png](pics/exp16_graph5.png)
![exp16_graph6.png](pics/exp16_graph6.png)
![exp16_graph7.png](pics/exp16_graph7.png)
![exp16_graph8.png](pics/exp16_graph8.png)
![exp16_graph9.png](pics/exp16_graph9.png)
![exp16_graph10.png](pics/exp16_graph10.png)
![exp16_graph11.png](pics/exp16_graph11.png)
![exp16_graph12.png](pics/exp16_graph12.png)
![exp16_graph13.png](pics/exp16_graph13.png)
![exp16_graph14.png](pics/exp16_graph14.png)
![exp16_graph15.png](pics/exp16_graph15.png)
![exp16_graph16.png](pics/exp16_graph16.png)

### Exp 17 – Linear regression

![exp17_output.png](pics/exp17_output.png)

### Exp 18 – KNN algorithm

![exp18_output.png](pics/exp18_output.png)

### Exp 19 – Logistic regression

![exp19_output1.png](pics/exp19_output1.png)
![exp19_output2.png](pics/exp19_output2.png)
![exp19_output3.png](pics/exp19_output3.png)
![exp19_output4.png](pics/exp19_output4.png)
![exp19_output5.png](pics/exp19_output5.png)
![exp19_output6.png](pics/exp19_output6.png)
![exp19_output7.png](pics/exp19_output7.png)
![exp19_output8.png](pics/exp19_output8.png)
![exp19_output9.png](pics/exp19_output9.png)
![exp19_output10.png](pics/exp19_output10.png)

### Exp 20 – K-means clustering

![exp20_output.png](pics/exp20_output.png)
![exp20_graph1.png](pics/exp20_graph1.png)
![exp20_graph2.png](pics/exp20_graph2.png)
![exp20_graph3.png](pics/exp20_graph3.png)
