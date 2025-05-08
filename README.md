# CV Insights 🧠📄
A ResumeParser project using NLTK and Flask API with a user friendly interface web application.

CV Insights is an intelligent tool designed to extract, analyze, and provide meaningful insights from resumes. This project aims to help recruiters, HR professionals, and job seekers by parsing CVs and summarizing key information such as skills, experience, education, and more.

> 🚧 **Project Under Development**  
> This is a work-in-progress repo. Future versions will include NLP-powered insights and a Flask-based web interface.

---

## 🔍 Features (Planned)

- ✅ Basic text extraction from PDF resumes
- 🔜 Natural Language Processing (NLP) model for:
  - Skills extraction
  - Summarized profile view
- 🔜 React-based interactive web interface
- 🔜 Admin dashboard for viewing and filtering CV insights (later)
- 🔜 Support for batch uploads and exports

---

## 🧰 Tech Stack

| Layer        | Tech                                                     |
|--------------|----------------------------------------------------------|
| Backend      | Python, Flask *(planned)*                                |
| NLP Model    | spaCy / Hugging Face Transformers *(to be decided)*      |
| CV Parsing   | PyMuPDF / pdfminer *(to be decided)*                     |
| Frontend     | React via Flask templates *(planned)*                    |

---

## 🚀 Getting Started

### Clone the Repo

```bash
git clone https://github.com/kushagrasinghx/cv-insights.git
cd cv-insights
```

### Set Up Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

🔍 Note: requirements.txt will be updated as more modules are added.

## 📌 Roadmap / To-Do

- [x] Set up repo structure and planning 
- [x] Basic frontend for uploading PDFs
- [ ] Basic CV parsing using PDFs
- [ ] Skill and experience extraction via NLP 
- [ ] Flask backend with form-based CV upload
- [ ] Dashboard to view summarized CV insights
- [ ] Option to download insight reports

## 🤝 Contributing

Pull requests are welcome! Feel free to fork the repo and propose enhancements. For major changes, please open an issue first to discuss what you would like to change.

## 🙌 Acknowledgments

- Inspired by common HR tech tools and resume parsers
- Will utilize powerful NLP libraries like spaCy and Hugging Face in future versions
