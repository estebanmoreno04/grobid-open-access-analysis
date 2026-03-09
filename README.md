# Grobid Open Access Analysis

## Description
This repository contains a text extraction and analysis pipeline over 10 open-access scientific articles about artificial intelligence in healthcare.

The project uses Grobid to extract structured information from PDF files and Python scripts to answer three questions:

1. Draw a keyword cloud based on the abstract information.
2. Create a visualization showing the number of figures per article.
3. Create a list of the links found in each paper.

## Input dataset
The input dataset consists of 10 open-access articles in PDF format about artificial intelligence in healthcare.

The metadata of the selected papers is available in:
- `data/metadata/papers.csv`

The PDF files are stored in:
- `data/raw_pdfs/`

## Repository structure
- `data/raw_pdfs/`: input PDF articles
- `data/tei_xml/`: Grobid output in TEI XML format
- `data/metadata/`: metadata about selected articles
- `src/`: Python scripts for extraction and analysis
- `results/`: generated outputs
- `notebooks/`: optional exploratory notebooks

## Requirements
- Python 3.10+
- Grobid
- Python dependencies listed in `requirements.txt`

## Installation
Clone the repository and install dependencies:

```bash
git clone <your-repository-url>
cd grobid-open-access-analysis
pip install -r requirements.txt
```

## Execution
1. Place the selected PDF files in `data/raw_pdfs/`
2. Run Grobid to generate TEI XML files in `data/tei_xml/`
3. Execute the Python scripts in `src/`
4. Store the results in `results/`

## Expected outputs
The project should generate the following outputs:
- `results/keyword_cloud.png`
- `results/figures_per_article.csv`
- `results/figures_per_article.png`
- `results/links_per_article.csv`

## Validation
The validation strategy for each output is the following:

### 1. Keyword cloud from abstracts
The extracted abstracts will be manually compared with the original abstracts in a subset of papers to verify that Grobid correctly captures the abstract section.

The most frequent words will also be checked to ensure they are consistent with the topic of the selected articles.

### 2. Number of figures per article
The automatic figure count obtained from the TEI XML files will be manually compared against the visible figures in a subset of the PDF articles.

### 3. Links found in each paper
The extracted links will be manually checked against the original PDF content in a subset of papers to confirm that the URLs and identifiers were correctly detected.

## Reproducibility
This repository includes:
- input metadata
- input PDF files
- extraction scripts
- analysis scripts
- generated outputs

A computational environment and Docker support will be added in later steps.

## Acknowledgements
Course: Open Science and AI in Research Software Engineering
