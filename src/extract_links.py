from pathlib import Path
import pandas as pd
from bs4 import BeautifulSoup
import re


URL_PATTERN = re.compile(r"https?://[^\s<>()]+")
DOI_URL_PATTERN = re.compile(r"10\.\d{4,9}/[^\s<>()]+")


def normalize_link(link: str) -> str:
    link = link.strip()
    link = link.rstrip(".,;)]}>\"'")
    return link


def is_valid_external_link(link: str) -> bool:
    if not link:
        return False

    # Excluir anclas internas y referencias locales del XML
    if link.startswith("#"):
        return False

    # Mantener solo URLs web reales
    if link.startswith("http://") or link.startswith("https://"):
        return True

    return False


def extract_links_from_tei(xml_path: Path) -> list[str]:
    with open(xml_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "xml")

    links = set()

    # 1. Buscar atributos target y filtrar solo enlaces externos reales
    for tag in soup.find_all(attrs={"target": True}):
        target = tag.get("target")
        if target:
            target = normalize_link(target)
            if is_valid_external_link(target):
                links.add(target)

    # 2. Buscar URLs directamente en el texto completo
    full_text = soup.get_text(" ", strip=True)

    for match in URL_PATTERN.findall(full_text):
        cleaned = normalize_link(match)
        if is_valid_external_link(cleaned):
            links.add(cleaned)

    # 3. Buscar DOI en texto y convertirlos en URL DOI
    for doi in DOI_URL_PATTERN.findall(full_text):
        doi = normalize_link(doi)
        doi_url = f"https://doi.org/{doi}"
        links.add(doi_url)

    return sorted(links)


def clean_article_name(filename: str) -> str:
    name = filename.replace(".tei.xml", "")
    name = name.replace(".grobid", "")
    return name


def main() -> None:
    input_dir = Path("data/tei_xml")
    output_dir = Path("results")
    output_dir.mkdir(parents=True, exist_ok=True)

    rows = []

    for xml_file in sorted(input_dir.glob("*.xml")):
        article_name = clean_article_name(xml_file.name)
        links = extract_links_from_tei(xml_file)

        if links:
            for link in links:
                rows.append(
                    {
                        "article": article_name,
                        "link": link,
                    }
                )
        else:
            rows.append(
                {
                    "article": article_name,
                    "link": "",
                }
            )

    df = pd.DataFrame(rows)
    output_file = output_dir / "links_per_article.csv"
    df.to_csv(output_file, index=False, encoding="utf-8")

    print("Link extraction finished.")
    print(f"Saved file: {output_file.resolve()}")


if __name__ == "__main__":
    main()
