
# Gemini Learning & Quiz Generator 🧠📄

This Python script leverages Google's Generative AI (Gemini) to help users **learn any topic** by generating structured PDF content and **test their knowledge** with a generated quiz — all in a few interactive prompts.

## 🚀 Features

- Generate educational PDFs on any topic and difficulty level
- Create quizzes with multiple choice questions, answers, and explanations
- Cleanly formatted output in PDF format
- Markdown-powered content conversion
- Automatically saves outputs in a `pdf/` directory

## 🛠️ Requirements

Install the required Python packages:

```bash
pip install google-generativeai markdown pdfkit
```

You'll also need:

- A valid **Google Generative AI API key**.
- [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) installed and properly added to your system's PATH (used by `pdfkit`).

## 📂 Project Structure

```
project/
│
├── gemini_script.py      # The main script file
├── pdf/                  # Output directory for PDFs
└── README.md             # You're reading this!
```

## 🔑 Configuration

Set your API key in the script:

```python
apiKey = "YOUR_API_KEY"
```

## 📚 How to Use

Run the script:

```bash
python gemini_script.py
```

Follow the interactive prompts:

1. Enter the topic you want to learn.
2. Set difficulty level.
3. Choose number of pages for PDF content.
4. Choose whether to generate a quiz.

Outputs are saved as PDFs in the `pdf/` folder.

## 📌 Notes

- Make sure `wkhtmltopdf` is installed or `pdfkit` will fail.
- All content is generated using Google's Gemini 2.0 Flash model.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

Happy learning! 📘✨
