from . import helpers, models


class ExcelUtils:
    def __init__(self, year, month, wb, created_at_from, created_at_to, days_in_month_list):
        self.year = year
        self.month = month
        self.wb = wb
        self.created_at_from = created_at_from
        self.created_at_to = created_at_to
        self.days_in_month_list = days_in_month_list

    def report_market_func(self):
        ws_name = "Отчет по маркетам"
        ws = self.wb.create_sheet(ws_name)
        width = 0

        # HEADER
        row = 1

        cell = {
            "A": "Наименование магазина",
            "B": "Посетитель",
            "C": "Количество несоответствия",
        }

        width = helpers.excel_helper.get_max_width(cell, width)

        helpers.excel_helper.sheet_title(ws, cell, row)

        # BODY
        violations = models.Violation.objects.filter(
            created_at__gte=self.created_at_from,
            created_at__lte=self.created_at_to,
            is_no_violation=0,
        ).order_by("shop")
        data_list = []
        for violation in violations:
            data = {
                "shop": violation.shop.name,
                "client": violation.client.name,
            }

            if data not in data_list:
                data_list.append(data)

        for data in data_list:
            data["count"] = models.Violation.objects.filter(
                shop__name=data['shop'],
                client__name=data['client'],
            ).count()

        data_list = sorted(data_list, key=lambda d: d['count'], reverse=True)

        for data in data_list:
            row += 1
            cell = {
                "A": data['shop'],
                "B": data['client'],
                "C": data['count'],
            }
            width = helpers.excel_helper.get_max_width(cell, width)
            helpers.excel_helper.sheet_text(ws, cell, row)

        # FOOTER
        row += 1
        cell = {
            "A": "Общий итог",
            "B": "",
            "C": violations.count(),
        }
        width = helpers.excel_helper.get_max_width(cell, width)
        helpers.excel_helper.sheet_title(ws, cell, row)
        helpers.excel_helper.sheet_width(ws, cell, width=width + 1)

    def report_process_func(self):

        ws_name = "Отчет процессы"
        ws = self.wb.create_sheet(ws_name)
        width = 0

        # HEADER
        row = 1

        cell = {
            "A": "Процесс",
            "B": "Кол-во",
            "C": "100%",
            "D": f"{self.days_in_month_list[0][0]}-{self.days_in_month_list[0][-1]}.{self.month}.{self.year}",
            "E": "100%",
            "F": f"{self.days_in_month_list[1][0]}-{self.days_in_month_list[1][-1]}.{self.month}.{self.year}",
            "G": "100%",
            "H": f"{self.days_in_month_list[2][0]}-{self.days_in_month_list[2][-1]}.{self.month}.{self.year}",
            "I": "100%",
            "J": f"{self.days_in_month_list[3][0]}-{self.days_in_month_list[3][-1]}.{self.month}.{self.year}",
            "K": "100%",
            "L": f"{self.days_in_month_list[4][0]}-{self.days_in_month_list[4][-1]}.{self.month}.{self.year}",
            "M": "100%",
        }
        width = helpers.excel_helper.get_max_width(cell, width)
        helpers.excel_helper.sheet_width(ws, cell, width=width + 6)
        helpers.excel_helper.sheet_title(ws, cell, row)

        # BODY
        processes_values_list = models.Process.objects.values_list("id")
        processes = []
        for process in processes_values_list:
            processes.append(process[0])
        processes.append(None)

        # ALL COUNT
        violation_all_count = models.Violation.objects.filter(
            created_at__gte=self.created_at_from,
            created_at__lte=self.created_at_to,
        ).count()

        week_count_list = helpers.excel_helper.violation_weeks_count(
            year=self.year, month=self.month, days_in_month_list=self.days_in_month_list,
        )

        for process in processes:
            if process is None:
                process_title = "Не указан"
            else:
                process_title = models.Process.objects.get(id=process).title

            # PROCESS COUNT
            violation_process_all_count = models.Violation.objects.filter(
                created_at__gte=self.created_at_from,
                created_at__lte=self.created_at_to,
                process_id=process,
            ).count()

            week_process_count_list = helpers.excel_helper.violation_weeks_count(
                year=self.year, month=self.month, days_in_month_list=self.days_in_month_list,
                process_id=process,
            )

            row += 1
            cell = {
                "A": process_title,
                "B": violation_process_all_count,
                "C": f"{helpers.excel_helper.percent_count(violation_process_all_count, violation_all_count)}%",
                "D": week_process_count_list[0],
                "E": f"{helpers.excel_helper.percent_count(week_process_count_list[0], week_count_list[0])}%",
                "F": week_process_count_list[1],
                "G": f"{helpers.excel_helper.percent_count(week_process_count_list[1], week_count_list[1])}%",
                "H": week_process_count_list[2],
                "I": f"{helpers.excel_helper.percent_count(week_process_count_list[2], week_count_list[2])}%",
                "J": week_process_count_list[3],
                "K": f"{helpers.excel_helper.percent_count(week_process_count_list[3], week_count_list[3])}%",
            }
            try:
                cell.update({
                    "L": week_process_count_list[4],
                    "M": f"{helpers.excel_helper.percent_count(  week_process_count_list[4], week_count_list[4])}%",
                })
            except IndexError:
                pass
            helpers.excel_helper.sheet_text(ws, cell, row)

        # FOOTER SUM
        row += 1
        cell = {
            "B": violation_all_count,
            "D": week_count_list[0],
            "F": week_count_list[1],
            "H": week_count_list[2],
            "J": week_count_list[3],
        }
        try:
            cell.update({
                "L": week_count_list[4],
            })
        except IndexError:
            pass
        helpers.excel_helper.sheet_text(ws, cell, row)

    def report_department_func(self):
        ws_name = "Отчет по департаментам"
        ws = self.wb.create_sheet(ws_name)

        width = 0
        last_row_list = []
        # HEADER
        row = 1
        cell = {
            # BODY STATUS BLOCK
            "A": "Статус",
            "B": "Ответственный департамент",
            "C": "Имя магазина",
            "D": "Количество несоответствий",

            # BODY DEPARTMENT BLOCK
            "F": "Ответственный департамент",
            "G": "Количество несоответсвий",
        }

        width = helpers.excel_helper.get_max_width(cell, width)
        helpers.excel_helper.sheet_width(ws, cell, width=width + 6)
        helpers.excel_helper.sheet_title(ws, cell, row)

        # BODY

        # BODY STATUS BLOCK
        row = 1
        statuses = models.Status.objects.all()
        for status in statuses:
            violations_by_status = models.Violation.objects.filter(
                created_at__gte=self.created_at_from,
                created_at__lte=self.created_at_to,
                status_id=status.id,
            ).order_by("response_admin_id")
            violation_data = []
            for violation in violations_by_status:
                if violation.response_admin is None:
                    response_admin_id = None
                    response_admin_name = ""
                else:
                    response_admin_id = violation.response_admin.id
                    response_admin_name = violation.response_admin.name

                violation_by_status_admin_shop_count = models.Violation.objects.filter(
                    status_id=violation.status.id, response_admin_id=response_admin_id,
                    shop_id=violation.shop.id,
                ).count()

                violation_dict = {
                    "status": violation.status.title,
                    "response_admin_name": response_admin_name,
                    "shop_name": violation.shop.name,
                    "count": violation_by_status_admin_shop_count,
                }

                if violation_dict not in violation_data:
                    violation_data.append(violation_dict)

                    row += 1
                    cell = {
                        "A": violation_dict['status'],
                        "B": violation_dict['response_admin_name'],
                        "C": violation_dict['shop_name'],
                        "D": violation_dict['count'],
                    }
                    helpers.excel_helper.sheet_text(ws, cell, row)
        last_row_list.append(row)

        # BODY DEPARTMENT BLOCK
        row = 1
        admins = models.Admin.objects.filter(is_staff=1, is_superuser=0)
        for admin in admins:
            violation_by_admin_count = models.Violation.objects.filter(response_admin_id=admin.id).count()

            row += 1
            cell = {
                "F": admin.name,
                "G": violation_by_admin_count,
            }
            helpers.excel_helper.sheet_text(ws, cell, row)
        last_row_list.append(row)

        # FOOTER
        violations_count = models.Violation.objects.filter(
            created_at__gte=self.created_at_from,
            created_at__lte=self.created_at_to,
        ).count()
        row = max(last_row_list) + 1
        cell = {
            "A": "Общий итог",
            "B": "",
            "C": "",
            "D": violations_count,
        }
        helpers.excel_helper.sheet_title(ws, cell, row)

    def report_attendance_func(self):
        ws_name = "Отчет по посещаемости"
        ws = self.wb.create_sheet(ws_name)
        width = 0

        # HEADER
        row = 1
        cell = {
            "A": "Имя посещаемого",
            "B": "Кол-во посещений",
            "C": f"1 неделя ({self.days_in_month_list[0][0]}-{self.days_in_month_list[0][-1]}.{self.month}.{self.year})",
            "D": f"2 неделя ({self.days_in_month_list[1][0]}-{self.days_in_month_list[1][-1]}.{self.month}.{self.year})",
            "E": f"3 неделя ({self.days_in_month_list[2][0]}-{self.days_in_month_list[2][-1]}.{self.month}.{self.year})",
            "F": f"4 неделя ({self.days_in_month_list[3][0]}-{self.days_in_month_list[3][-1]}.{self.month}.{self.year})",
            "G": f"5 неделя ({self.days_in_month_list[4][0]}-{self.days_in_month_list[4][-1]}.{self.month}.{self.year})",
        }

        width = helpers.excel_helper.get_max_width(cell, width)
        helpers.excel_helper.sheet_width(ws, cell, width=width + 6)
        helpers.excel_helper.sheet_title(ws, cell, row)

        # BODY
        violations = models.Violation.objects.filter(
            created_at__gte=self.created_at_from,
            created_at__lte=self.created_at_to,
            is_no_violation=0,
        )

        client_list = []
        for violation in violations:
            if violation.client.name not in client_list:
                client_list.append(violation.client.name)

        for client in client_list:
            row += 1
            violation_count_by_client = models.Violation.objects.filter(client__name=client).count()

            shops_week_list = []
            for day_in_month in self.days_in_month_list:
                violations_week_list = models.Violation.objects.filter(
                    client__name=client, created_at__gte=f"{self.year}-{self.month}-{day_in_month[0]}",
                    created_at__lte=f"{self.year}-{self.month}-{day_in_month[-1]}",
                ).all()
                shops_week_string = ""
                shops_week_cycle_list = []
                for violations_week in violations_week_list:
                    if violations_week.shop.name not in shops_week_cycle_list:
                        if shops_week_cycle_list:
                            shops_week_string += "\n" + violations_week.shop.name
                        else:
                            shops_week_string += violations_week.shop.name
                        shops_week_cycle_list.append(violations_week.shop.name)

                shops_week_list.append(shops_week_string)

            cell = {
                "A": client,
                "B": violation_count_by_client,
                "C": shops_week_list[0],
                "D": shops_week_list[1],
                "E": shops_week_list[2],
                "F": shops_week_list[3],
                "G": shops_week_list[4],
            }
            helpers.excel_helper.sheet_text(ws, cell, row)

    def report_general_func(self):
        ws_name = "Общее"
        ws = self.wb.create_sheet(ws_name)

        width = 0

        # HEADER
        row = 1
        cell = {
            "A": "ID",
            "B": "Автор",
            "C": "Нет нарушений",
            "D": "Дата посещения",
            "E": "Регион",
            "F": "Магазин",
            "G": "Департамент",
            "H": "Проблема",
            "I": "Несоответствие",
            "J": "Коммент",
            "K": "Фото",
            "L": "Процесс",
            "M": "Ответственный отдел",
            "N": "Отчет от ответственного отдела",
            "O": "Отчет фото",
            "P": "Статус",
            "Q": "Дата закрытия нарушения",
        }

        width = helpers.excel_helper.get_max_width(cell, width)
        helpers.excel_helper.sheet_width(ws, cell, width=width + 6)
        helpers.excel_helper.sheet_title(ws, cell, row)

        # BODY
        violations = models.Violation.objects.filter(
            created_at__gte=self.created_at_from,
            created_at__lte=self.created_at_to,
            is_no_violation=0,
        )

        for violation in violations:
            if violation.response_admin is None:
                response_admin_name = ""
                process_title = ""
            else:
                response_admin_name = violation.response_admin.name
                process_title = violation.process.title

            if violation.is_no_violation == 0:
                department_title = violation.department.title
                problem_title = violation.problem.title
                disparity_title = violation.disparity.title
            else:
                department_title = ""
                problem_title = ""
                disparity_title = ""

            row += 1
            cell = {
                "A": violation.id,
                "B": violation.client.name,
                "C": helpers.excel_helper.is_no_violation_text(violation.is_no_violation),
                "D": helpers.excel_helper.datetime_to_text(violation.created_at),
                "E": violation.region.name,
                "F": violation.shop.name,
                "G": department_title,
                "H": problem_title,
                "I": disparity_title,
                "J": violation.comment,
                "K": str(violation.photo),
                "L": process_title,
                "M": response_admin_name,
                "N": violation.response_person_description,
                "O": str(violation.response_result_photo),
                "P": violation.status.title,
                "Q": helpers.excel_helper.datetime_to_text(violation.updated_at),
            }
            helpers.excel_helper.sheet_text(ws, cell, row, align_horizontal="center")


# def report_weeks_func(self):
#     week_list = helpers.excel_helper.days_in_month_func(  self.year, self.month)
#     for week in week_list:
#         week_sheet_name = f"{week_list[week][0]}-{week_list[week][-1]}.{self.month}.{self.year}"
#         week_sheet = self.wb.create_sheet(week_sheet_name)
