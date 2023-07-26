import weasyprint

from io import BytesIO
from datetime import datetime

def create_pdf_emotions(answers: dict, questions: list, time: datetime) -> BytesIO:
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
        <h1>Емоції, яких я уникаю</h1>
    """

    for i, question in enumerate(questions):
        answer = answers[f"question_{i + 1}"]
        html_string += f"""
        <div class="question"><strong>{question}</strong></div>
        <div class="answer">{answer}</div>
        """

    html_string += f"<p class='datetime'>Дата та час: {time.replace(tzinfo=None)}</p>"

    html_string += """
    </body>
    </html>
    """

    weasyprint.HTML(string=html_string).write_pdf(buffer)
    buffer.seek(0)
    return buffer