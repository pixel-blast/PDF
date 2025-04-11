import google.generativeai as genai # Gemini AI
import markdown # Font formatting
import pdfkit # PDF

def gemini():
    # Google Gemini AI
    model = genai.GenerativeModel('gemini-2.0-flash') # Specifing Gemini Model
    apiKey = "AIzaSyB_-gYBfP33OuIgydhIbifPESp51tUCyzo" # API Key
    genai.configure(api_key=apiKey)

    # User Input
    topic = str(input("What do you want to learn today: "))
    level = "  Difficulty " + str(input('Enter a difficulty: '))
    pages = int(input('Enter number of pages: '))
    print()

    def learn():
        # Learning section
        # Name of PDF
        print('Generating Content...')
        learn_name_raw1 = model.generate_content(f'Give me a name for the pdf of topic {topic} and difficulty {level}. Give me only one name nothing else, dont include .pdf at last')
        learn_name_raw2 = learn_name_raw1.text.strip()
        learn_name = learn_name_raw2 + '.pdf'
        print(learn_name)
        # Generating the PDF
        responseLearn_raw1 = model.generate_content(f'I want to learn {topic} with difficulty {level}. Generate only text that I can convert into a pdf. Make text for {pages} pages')
        responseLearn_raw2 = responseLearn_raw1.text.strip()
        responseLearn = markdown.markdown(responseLearn_raw2)
        # Saving output as PDF
        learnPdfPath = f"pdf/{learn_name}"
        pdfkit.from_string(responseLearn, learnPdfPath)
        print('Generating PDF...')

        # Conditional Statement to handle quiz generation
        exam_promp = str(input('Enter 1 to generate quiz, else press enter: '))
        if exam_promp == "1":
            exam()
        else:
            pass

    def exam():
        # Quiz section
        # Generating Name for PDF
        print('Generating Content...')
        exam_name_raw1 = model.generate_content(f'Give me a name for the quiz pdf of topic {topic} and difficulty {level}, include word quiz at end. Give me only one name nothing else.')
        exam_name_raw2 = exam_name_raw1.text.strip()
        exam_name = exam_name_raw2 + '.pdf'
        print(exam_name)
        # Generating output for PDF
        responseExam_raw1 = model.generate_content(f'Generate a MCQ of topic {topic} with difficulty {level} Dont forget answer and explanation at the end. Make sure the options are at different line USE break line \n.  Generate only text that I can convert into a pdf. Make text for {pages} pages')
        responseExam_raw2 = responseExam_raw1.text.strip()
        responseExam = markdown.markdown(responseExam_raw2)
        # Saving PDF
        examPdfPath = f"pdf/{exam_name}"
        pdfkit.from_string(responseExam, examPdfPath)
        print('Generating PDF...')

    # Conditional Statement to handle first input
    condition = int(input('Enter 1 to learn the topic\nEnter 2 to give a exam \n')) 
    print()
    if condition == 1:
        learn()
    elif condition == 2:
        exam()

# Main function
gemini()
