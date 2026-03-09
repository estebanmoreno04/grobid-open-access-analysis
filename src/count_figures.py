from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


def count_figures_in_tei(xml_path: Path) -> int:
    with open(xml_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "xml")

    figures = soup.find_all("figure")
    return len(figures)


def main() -> None:
    input_dir = Path("data/tei_xml")
    output_dir = Path("results")
    output_dir.mkdir(parents=True, exist_ok=True)

    rows = []

    for xml_file in sorted(input_dir.glob("*.xml")):
        figure_count = count_figures_in_tei(xml_file)

        article_name = xml_file.name.replace(".tei.xml", "")
        article_name = article_name.replace(".grobid", "")
        rows.append(
            {
                "article": article_name,
                "num_figures": figure_count,
            }
        )

    df = pd.DataFrame(rows)
    df.to_csv(output_dir / "figures_per_article.csv", index=False, encoding="utf-8")

    plt.figure(figsize=(10, 6))
    plt.bar(df["article"], df["num_figures"])
    plt.xlabel("Article")
    plt.ylabel("Number of figures")
    plt.title("Number of figures per article")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_dir / "figures_per_article.png", dpi=300, bbox_inches="tight")
    plt.close()

    print("Figure counting finished.")
    print(f"Saved CSV: {(output_dir / 'figures_per_article.csv').resolve()}")
    print(f"Saved plot: {(output_dir / 'figures_per_article.png').resolve()}")


if __name__ == "__main__":
    main()
