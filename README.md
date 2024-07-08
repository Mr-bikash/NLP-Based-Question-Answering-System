NLP-Based Question Answering System

Table of Contents
About the Project
Features
Getting Started
Prerequisites
Installation
Usage
Running the Project
Example Commands
Project Structure
Technologies Used
Contributing
Contact


Getting Started
Prerequisites
Python 3.x
Libraries (e.g., BeautifulSoup, MILVUS, Transformers)

Installation
Clone the repository:
git clone https://github.com/Mr-Bikash/NLP-Based-Question-Answering-System.git

Navigate to the project directory:
cd NLP-Based-Question-Answering-System

Install dependencies:
pip install -r requirements.txt

Usage
Running the Project

Run the web crawler:
python crawler.py

Chunk and store data:
python chunk_and_store.py

Perform retrieval and question answering:
python retrieval.py

python question_answering.py

Example Commands
python crawler.py
python question_answering.py --query "Example question"
Project Structure
kotlin
Copy code
.
├── README.md
├── crawler.py
├── chunk_and_store.py
├── retrieval.py
├── question_answering.py
├── data/
│   ├── crawled_data/
│   ├── embeddings/
│   └── ...
└── requirements.txt
Technologies Used
Python
MILVUS
Transformers
BeautifulSoup
...
Contributing
Feel free to contribute to this project. Please follow the CONTRIBUTING.md guidelines.

Contact
For questions or feedback, contact Bikash.