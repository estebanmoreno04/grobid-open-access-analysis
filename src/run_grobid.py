from pathlib import Path
from grobid_client.grobid_client import GrobidClient


def main() -> None:
    input_dir = Path("data/raw_pdfs")
    output_dir = Path("data/tei_xml")

    output_dir.mkdir(parents=True, exist_ok=True)

    client = GrobidClient()

    client.process(
        "processFulltextDocument",
        input_path=str(input_dir),
        output=str(output_dir),
        n=4,
        force=True,
        verbose=True,
    )

    print("Grobid processing finished.")
    print(f"Input PDFs: {input_dir.resolve()}")
    print(f"Output TEI XML: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
