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
