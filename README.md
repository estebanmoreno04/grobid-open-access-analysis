# Grobid Open Access Analysis

## Description
This repository contains a text extraction and analysis pipeline over 10 open-access scientific articles about artificial intelligence in healthcare.

The project uses Grobid to extract structured information from PDF files and Python scripts to answer three questions:

1. Draw a keyword cloud based on the abstract information.
2. Create a visualization showing the number of figures per article.
3. Create a list of the links found in each paper.

## Objectives
The main objectives of this project are:
- build a reproducible pipeline for extracting structured information from scientific PDFs
- analyze a collection of 10 open-access papers on artificial intelligence in healthcare
- generate visual and tabular outputs based on abstracts, figures, and links
- document the methodology and validation process clearly in the repository

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

## Methodology
The project follows this pipeline:

1. Select 10 open-access papers related to artificial intelligence in healthcare.
2. Store the original PDF files in `data/raw_pdfs/`.
3. Process the PDFs with Grobid to obtain structured TEI XML files.
4. Extract abstract text from the XML files.
5. Generate a keyword cloud from the combined abstract content.
6. Count the number of figures detected in each article.
7. Extract and clean external links found in each paper.
8. Save all generated results in the `results/` folder.

## Execution
1. Place the selected PDF files in `data/raw_pdfs/`
2. Run Grobid to generate TEI XML files in `data/tei_xml/`
3. Execute the Python scripts in `src/`
4. Store the results in `results/`

## Running example
Run Grobid in Docker:

```bash
docker pull grobid/grobid:0.8.2-crf
docker run --rm --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.8.2-crf
```

Then execute the pipeline:

```bash
python src/run_grobid.py
python src/extract_abstracts.py
python src/make_wordcloud.py
python src/count_figures.py
python src/extract_links.py
```

## Expected outputs
The project should generate the following outputs:
- `results/abstracts.csv`
- `results/keyword_cloud.png`
- `results/figures_per_article.csv`
- `results/figures_per_article.png`
- `results/links_per_article.csv`

## Results
The generated results are stored in the `results/` folder:
- `abstracts.csv`: extracted abstract text for each article
- `keyword_cloud.png`: keyword cloud built from all abstracts
- `figures_per_article.csv`: number of figures detected in each article
- `figures_per_article.png`: bar chart showing the number of figures per article
- `links_per_article.csv`: list of links extracted from each article

Example outputs are available in the `results/` directory.

## Validation

### 1. Keyword cloud from abstracts
To validate the keyword cloud, the extracted abstracts were manually compared against the original abstract sections in a subset of the PDFs. In addition, the most frequent words in the cloud were checked to ensure they were coherent with the selected topic, artificial intelligence in healthcare.

### 2. Number of figures per article
To validate the figure counts, the number of `<figure>` elements extracted from the TEI XML files was manually compared with the visible figures in a subset of the original PDF articles. Possible discrepancies may appear when publishers encode graphical material differently.

### 3. Links found in each paper
To validate the extracted links, the final CSV output was manually compared with links visible in a subset of the PDF articles. Internal TEI/XML references were filtered out so that the final output only retains external web links and DOI-based links when detected.

## Reproducibility
This repository includes:
- input metadata
- input PDF files
- extraction scripts
- analysis scripts
- generated outputs

The use of Grobid in Docker improves reproducibility by ensuring a consistent environment for PDF processing. The Python dependencies required to run the analysis are listed in `requirements.txt`.

## Limitations
Some limitations should be considered:
- Grobid extraction quality may vary depending on the PDF layout.
- Some figures may not be detected if they are not properly encoded in the PDF structure.
- Some links may be missed if they are broken across lines or not represented explicitly in the extracted XML.
- Different publishers may structure PDFs differently, which can affect extraction quality.

## Help
If Grobid does not respond, make sure the Docker container is running on `localhost:8070`.

## Future improvements
Possible improvements for future versions of the project include:
- adding Docker support for the full experiment
- including a `CITATION.cff` file
- adding richer software metadata such as `codemeta.json`
- extending the analysis with additional statistics or text mining steps

## Acknowledgements
Course: Open Science and AI in Research Software Engineering
