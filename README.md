# AI Gen and RAG Bibliographic Review Assistant

![License](https://img.shields.io/badge/license-GPLv3-blue)
![Python Version](https://img.shields.io/badge/python-3.8%2B-brightgreen)

An automated assistant for literature review using Generative AI (Gen AI) and Retrieval Augmented by Generation (RAG) techniques. The project searches for articles in the arXiv database and generates automatic abstracts with two method options:
- **BART (local)**: Uses the BART model from Hugging Face for offline generation.
- **OpenAI GPT**: Uses the OpenAI API for abstract generation.


## 💻 Dashboard Demo
Veja abaixo uma prévia da interface do projeto:
![Dashboard Example 1](dashboard_example1.png)
![Dashboard Example 2](dashboard_example2.png)

---

## 🚀 How to Run the Project
### Prerequisites
- Python 3.8+
- Streamlit
- Hugging Face Transformers
- OpenAI API (optional)

### Installation
1. Clone the repository:
```git
git clone https://github.com/GabrielWendell/AI-Gen-RAG-Bibliographic-Review-Assistant.git
cd AI-Gen-RAG-Bibliographic-Review-Assistant
```
2. Install the dependencies:
```git
pip install -r requirements.txt
```
3. Execute the project:
```git
streamlit run main.py
```
4. To use the OpenAI version:
```git
streamlit run main.py -- --method openai
```
## 📚 Technologies Used
- Python
- Streamlit
- Transformers (Hugging Face)
- OpenAI API
- Dash and Plotly for visualization

``` Repository Structure
AI-Gen-RAG-Bibliographic-Review-Assistant/
├── README.md               # Project description and instructions for use
├── requirements.txt        # Project dependencies
├── main.py                 # Main script
├── modules/                # Project modules
│   ├── data_fetch.py
│   ├── dashboard.py
│   ├── text_summarization.py
│   └── text_summarization_openai.py
└── LICENSE                 # License to use
```

## 🤝 Contributions
Contributions are welcome! Feel free to submit pull requests or open issues.

## 📝 License
This project is licensed under the [GPL 3.0 License](https://github.com/GabrielWendell/AI-Gen-RAG-Bibliographic-Review-Assistant/blob/main/LICENSE).

## 🧑‍💻 Author
This project was developed by [**Gabriel Wendell**](https://github.com/GabrielWendell) as part of a challenge for the trainee researcher selection process at Itaú.
