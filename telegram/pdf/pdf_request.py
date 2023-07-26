import weasyprint

from io import BytesIO
from datetime import datetime

def create_pdf(work_list_answers: dict, abc_model_answers: dict, falling_arrow_answers: dict,
               work_list_questions: list, abc_model_questions: list, falling_arrow_questions: list) -> BytesIO:
    buffer = BytesIO()

    html_string = f"""
    <html>
    <head>
        <style>
            h1 {{
                color: #000000; 
                text-align: center;
            }}

            .question {{
                font-size: 18px;
                color: #008080; 
                margin-top: 20px;
                margin-bottom: 5px; 
            }}

            .answer {{
                font-size: 16px;
                color: #000000; 
                margin-bottom: 10px; 
            }}

            .datetime {{
                text-align: right;
                color: #000000; 
                margin-top: 50px;
            }}
        </style>
    </head>
    <body>
        <h1>Запит</h1>
    """

    html_string += "<h2>Робочий лист підготовки до терапії</h2>"

    for i, question in enumerate(work_list_questions):
        answer = work_list_answers[f"question_{i+1}"]
        html_string += f"""
        <div class="question"><strong>{question}</strong></div>
        <div class="answer">{answer}</div>
        """

    html_string += "<h2>АБС-модель</h2>"

    for i, question in enumerate(abc_model_questions):
        answer = abc_model_answers[f"question_{i+1}"]
        html_string += f"""
        <div class="question"><strong>{question}</strong></div>
        <div class="answer">{answer}</div>
        """

    html_string += "<h2>Падаюча стріла</h2>"

    for i, question in enumerate(falling_arrow_questions):
        answer = falling_arrow_answers[f"question_{i+1}"]
        html_string += f"""
        <div class="question"><strong>{question}</strong></div>
        <div class="answer">{answer}</div>
        """

    html_string += f"<p class='datetime'>Дата та час: {datetime.now().replace(second=0, microsecond=0)}</p>"

    html_string += """
    </body>
    </html>
    """

    weasyprint.HTML(string=html_string).write_pdf(buffer)
    buffer.seek(0)
    return buffer