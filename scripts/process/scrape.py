import bs4, csv
import markdownify

with open("./data/preprocess/tags.csv", "w") as fexport:
    writer = csv.DictWriter(fexport, fieldnames=["question", "tag"])
    writer.writeheader()
    with open("./data/raw/urls.txt") as furls:
        for i, file in enumerate(furls):
            file = file.strip()
            if not file: continue

            with open(f"./data/raw/{file}") as fpage:
                content = fpage.read()
            soup = bs4.BeautifulSoup(content, "html.parser")

            for qt in soup.select("#questions .s-post-summary"):
                # Question
                title = qt.select_one(".s-post-summary--content-title").text.strip()
                question =  qt.select_one(".s-post-summary--content-excerpt").text.strip()

                tag = qt.select_one(".s-tag").text

                writer.writerow({
                    "question": ' '.join([title, question]),
                    "tag": tag
                })
                print(i)


