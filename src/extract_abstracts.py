from pathlib import Path
import pandas as pd
from bs4 import BeautifulSoup


def extract_abstract_from_tei(xml_path: Path) -> str:
    with open(xml_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "xml")

    abstract = soup.find("abstract")
    if abstract is None:
        return ""

    abstract_text = abstract.get_text(" ", strip=True)
    return abstract_text


def main() -> None:
    input_dir = Path("data/tei_xml")
    output_dir = Path("results")
    output_dir.mkdir(parents=True, exist_ok=True)

    rows = []

    for xml_file in sorted(input_dir.glob("*.xml")):
        abstract_text = extract_abstract_from_tei(xml_file)

        rows.append(
            {
                "article": xml_file.stem,
                "abstract": abstract_text,
            }
        )

    df = pd.DataFrame(rows)
    output_file = output_dir / "abstracts.csv"
    df.to_csv(output_file, index=False, encoding="utf-8")

    print("Abstract extraction finished.")
    print(f"Saved file: {output_file.resolve()}")


if __name__ == "__main__":
    main()
