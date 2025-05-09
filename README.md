# Projet - dataset Stackoverflow

Ce projet vise à construire un corpus de questions/réponses obtenues sur la plateforme Stackoverflow. Ce corpus est construit pour fine-tuner un modèle de base GPT, afin d'en faire un chatbot utile pour répondre à des questions de programmation.

## Besoins du projet

La finalité du projet est de construire un chatbot à destination des développeurs. L'idée est de leur permettre de poser une question en lien avec python, puis d'obtenir une réponse à leur question. Pour cela, nous devons trouver une source de données qui propose cette fonctionnalité : des questions de programmation et une réponse pertinente associée.

Dans le cadre de notre projet, nous utiliserons la plateforme Stackoverflow comme source de données. Stackoverflow est un forum pour et par les développeurs. Il permet à tout à chacun de poser une question et la communauté est libre de lui répondre. Stackoverflow présente plusieurs avantages pour notre projet :

* La plupart des questions ont une réponse unique et de qualité mise en avant : cela facilite la construction de paires question/réponse.
* les réponses aux questions sont détaillées et pédagogiques.
* le contenu de la plateforme est sous licence creative commons CC BY-SA, nous pouvons donc réutiliser les données tout en mentionnant leur source.

Nous allons donc construire un crawler qui s'occupera de naviguer à travers les meilleurs Q/A de la plateforme sur le sujet "Python". Les documents HTML récupérées feront l'objet d'une extraction, d'un nettoyage et d'une augmentation.

## Récupération des données

Les données sont scrapées grâce à la bibliothèque python [SeleniumBase](https://seleniumbase.io/) basée sur Selenium, une bibliothèque python permettant d'automatiser la manipulation de navigateurs webs. Le passage par selenium plutôt que des requêtes HTTP standards est nécessaire car StackOverflow se protège derrière un proxy CloudFlare. Celui-ci protège StackOverflow des crawlers.

Le processus de crawl se divise en plusieurs étapes :
- navigation à travers l'index des publications ayant le tag `python` (sur 100 pages)
- enregistrement de chacune des pages au format HTML
- ouverture de ces pages, récupération des liens vers les publications, enregistrement des publications au format HTML

Le script du crawl se trouve dans `./scripts/process/crawl.py`.Les fichiers sont placés dans le sous-dossier `./data/raw`. Notre collecte prévoyait initialement 5000 pages, nous nous sommes arrêté à 1200 pages.

## Extraction et nettoyage

Les pages HTML bruts ne sont pas directement utilisables pour notre entraînement. Pour chaque fichier HTML (un par publication), il faut extraire la question et la réponse la plus pertinente. On utilise pour cela la bibliothèque BeautifulSoup : différents sélecteurs CSS permettent de récupérer le HTML du contenu de la question et celui de la première réponse (la mieux votée).

Par la suite, pour rendre nos données plus propres, nous appliquons à notre HTML une traduction vers le Markdown. Cela permettra à notre chatbot de retourner une réponse au format Markdown, une format de mise en page plus souple que le HTML.

Le script permettant cette extraction et ce nettoyage se trouve dans `./scripts/process/scrape.py`. Le script génère un fichier CSV (une colonne _question_, une colonne _answer_) placé dans `./data/preprocess/qa.csv`.

## Fine-tuning

### Choix de l'architecture du modèle

Nous souhaitons construire un chatbot se rapprochant de ChatGPT. Pour cela, nous optons pour le fine-tuning d'un modèle GPT (General Pretrained Transformers). Fine-tuner un GPT implique de choisir un modèle de base et de poursuivre son entraînement sur un contenu texte qui respecte une forme spécifique semblable à un enchaînement de questions/réponses.

### Trouver un modèle de base


### Fine-tuner le modèle de base


