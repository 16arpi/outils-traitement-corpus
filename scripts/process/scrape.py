import bs4, csv
import markdownify

with open("./data/preprocess/qa.csv", "w") as fexport:
    writer = csv.DictWriter(fexport, fieldnames=["question", "answer"])
    writer.writeheader()
    with open("./data/raw/pages/urls.txt") as furls:
        for i, file in enumerate(furls):
            file = file.strip()
            if not file: continue

            with open(f"./data/raw/pages/{file}") as fpage:
                content = fpage.read()
            soup = bs4.BeautifulSoup(content)

            # Question
            question = soup.select_one("#question .s-prose")
            for notice in question.select(".s-notice"):
                notice.decompose()

            question_md = markdownify.markdownify(question.encode_contents())

            # Anwser
            answer = soup.select_one("#answers .answer .s-prose")
            for notice in question.select(".s-notice"):
                notice.decompose()

            answer_md = markdownify.markdownify(answer.encode_contents())
            writer.writerow({
                "question": question_md,
                "answer": answer_md
            })
            print(i)


