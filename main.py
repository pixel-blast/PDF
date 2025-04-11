import google.generativeai as genai
import markdown
import pdfkit
import os
import shlex
import platform

def gemini():
    model = genai.GenerativeModel('gemini-2.0-flash')
    apiKey = "AIzaSyB_-gYBfP33OuIgydhIbifPESp51tUCyzo"
    genai.configure(api_key=apiKey)
    topic = str(input("What do you want to learn today: "))
    level = "  Difficulty " + str(input('Enter a difficulty: '))
    pages = int(input('Enter number of pages: '))
    print()

    def learn():
        print('Generating Content...')
        learn_name_raw1 = model.generate_content(f'Give me a name for the pdf of topic {topic} and difficulty {level}. Give me only one name nothing else')
        learn_name_raw2 = learn_name_raw1.text.strip()
        learn_name = learn_name_raw2 + '.pdf'
        print(learn_name)
        responseLearn_raw1 = model.generate_content(f'I want to learn {topic} with difficulty {level}. Generate only text that I can convert into a pdf. Make text for {pages} pages')
        responseLearn_raw2 = responseLearn_raw1.text.strip()
        responseLearn = markdown.markdown(responseLearn_raw2)
        learnPdfPath = f"pdf/{learn_name}"
        pdfkit.from_string(responseLearn, learnPdfPath)
        print('Generating PDF...')

        exam_promp = str(input('Enter 1 to generate quiz, else press enter: '))
        if exam_promp == "1":
            exam()
        else:
            pass

        if platform.system() == 'Windows':
            os.startfile(learnPdfPath)
            os._exit(0)
        elif platform.system() == 'Darwin':
            os.system(f'open {shlex.quote(learnPdfPath)}')
            os._exit(0)
        elif platform.system() == 'Linux':
            os.system(f'xdg-open {shlex.quote(learnPdfPath)}')

    def exam():
        print('Generating Content...')
        exam_name_raw1 = model.generate_content(f'Give me a name for the quiz pdf of topic {topic} and difficulty {level}, include word quiz at end. Give me only one name nothing else.')
        exam_name_raw2 = exam_name_raw1.text.strip()
        exam_name = exam_name_raw2 + '.pdf'
        print(exam_name)
        responseExam_raw1 = model.generate_content(f'Generate a MCQ of topic {topic} with difficulty {level} Dont forget answer and explanation at the end. Make sure the options are at different line USE break line<br>.  Generate only text that I can convert into a pdf. Make text for {pages} pages')
        responseExam_raw2 = responseExam_raw1.text.strip()
        responseExam = markdown.markdown(responseExam_raw2)
        examPdfPath = f"pdf/{exam_name}"
        pdfkit.from_string(responseExam, examPdfPath)
        print('Generating PDF...')
        os.system('cls')
        os.system('clear')
        if platform.system() == 'Windows':
            os.startfile(examPdfPath)
            os._exit(0)
        elif platform.system() == 'Darwin':
            os.system(f'open {shlex.quote(examPdfPath)}')
            os._exit(0)
        elif platform.system() == 'Linux':
            os.system(f'xdg-open {shlex.quote(examPdfPath)}')


    condition = int(input('Enter 1 to learn the topic\nEnter 2 to give a exam \n')) 
    print()
    if condition == 1:
        learn()
    elif condition == 2:
        exam()

gemini()
