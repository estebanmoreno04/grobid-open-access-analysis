from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


def main() -> None:
    input_file = Path("results/abstracts.csv")
    output_dir = Path("results")
    output_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(input_file)

    all_text = " ".join(df["abstract"].fillna("").astype(str))

    custom_stopwords = set(STOPWORDS)
    custom_stopwords.update({
        "study", "results", "conclusion", "conclusions",
        "background", "methods", "method", "using",
        "used", "based", "paper", "article"
    })

    wordcloud = WordCloud(
        width=1200,
        height=600,
        background_color="white",
        stopwords=custom_stopwords,
        collocations=False
    ).generate(all_text)

    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout()

    output_file = output_dir / "keyword_cloud.png"
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    plt.close()

    print("Word cloud generated successfully.")
    print(f"Saved file: {output_file.resolve()}")


if __name__ == "__main__":
    main()
