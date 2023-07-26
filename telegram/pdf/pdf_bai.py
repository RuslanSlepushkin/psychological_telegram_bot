import weasyprint

from io import BytesIO
from datetime import datetime


def create_pdf_bai(answers: dict, questions: list, result: int, time: datetime) -> BytesIO:
    buffer = BytesIO()

    html_string = f"""
    <html>
    <head>
        <style>
            table {{
                border-collapse: collapse;
                width: 100%;
            }}

            th, td {{
                border: 1px solid black;
                padding: 8px;
                text-align: center;
            }}

            .header {{
                text-align: center;
                font-weight: bold;
                font-size: 24px;
            }}

            .result {{
                text-align: left;
                font-weight: bold;
            }}

            .datetime {{
                text-align: right;
            }}
        </style>
    </head>
    <body>
        <p class="header">Шкала тривоги Бека</p>
        <table>
            <tr>
                <th style="text-align: left;">Запитання</th>
                <th>Відповідь</th>
            </tr>
    """

    for i, question in enumerate(questions):
        answer = answers[f"question_{i+1}"]
        html_string += f"<tr><td style='text-align: left;'>{question}</td><td>{answer}</td></tr>"

    html_string += """
        </table>
    """

    if result <= 5:
        html_string += f"<p class='result'>Результат: {result} - норма </p>"
    elif result <= 8:
        html_string += f"<p class='result'>Результат: {result} - легкий рівень тривоги</p>"
    elif result <= 18:
        html_string += f"<p class='result'>Результат: {result} - середній рівень тривоги</p>"
    elif result > 18:
        html_string += f"<p class='result'>Результат: {result} - високий рівень тривоги</p>"

    html_string += f"<p class='datetime'>Дата та час: {time.replace(tzinfo=None)}</p>"

    html_string += """
    </body>
    </html>
    """

    weasyprint.HTML(string=html_string).write_pdf(buffer)
    buffer.seek(0)
    return buffer
