from datetime import datetime
from PySide6.QtWidgets import QLabel, QListWidget
from client.api.resolver import getAll

def update_statistics(complete: QLabel, avg: QLabel, types: QListWidget):
    data = getAll("Requests")
    complete.setText(f"Количество выполненных заявок: {complete_sum(data)}")
    avg.setText(f"Среднее время выполнения заявки: {avg_completion_time(data)} дней")

def complete_sum(data: list):
    complete: int = 0
    for item in data:
        if not item["date_completion"]: continue
        complete += 1
    return complete

def avg_completion_time(data: list):
    days: list = []
    date_format = "%d.%m.%Y"
    for item in data:
        if not item["date_completion"]: continue
        add = datetime.strptime(item["add_date"], date_format).date()
        end = datetime.strptime(item["date_completion"], date_format).date()
        delta = end - add
        days.append(delta.days)
    return sum(days) / len(days)

