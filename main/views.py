import csv
import os
import shutil
import random
import datetime

from django.core.files.base import File
from django.db import connection
from django.shortcuts import redirect

from . import settings
from api.models import *

csv_file_path = os.path.join(settings.BASE_DIR, 'csv/')

def index(request):
    return redirect('admin/')


def check_foreign_key(check_num):
    cursor = connection.cursor()
    cursor.execute(f"SET FOREIGN_KEY_CHECKS = {check_num};")
    print(f"FOREIGN_KEY_CHECKS = {check_num}")


def truncate(table):
    cursor = connection.cursor()
    cursor.execute(f"TRUNCATE TABLE api_{table}")
    print(f"api_{table} truncated successfully")


def truncate_token():
    cursor = connection.cursor()
    cursor.execute(f"TRUNCATE TABLE authtoken_token")
    print(f"authtoken_token truncated successfully")


def processAdminSeed():
    # truncate("process")
    with open(os.path.join(csv_file_path + 'process.csv'), 'r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            Process.objects.create(
                title=line[0],
            )
    print("Process import successfully!", end="\n\n")


def statusAdminSeed():
    # truncate("status")
    with open(os.path.join(csv_file_path + 'status.csv'), 'r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            Status.objects.create(
                title=line[0],
            )
    print("Status import successfully!", end="\n\n")


def buttonSeed():
    # truncate("button")
    with open(os.path.join(csv_file_path + 'buttons.csv'), 'r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            Button.objects.create(
                key=line[1],
                title=line[2],
            )
    print("Buttons import successfully!", end="\n\n")


def contentSeed():
    # truncate("content")
    with open(os.path.join(csv_file_path + 'contents.csv'), 'r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            Content.objects.create(
                key=line[1],
                title=line[2],
            )
    print("Contents import successfully!", end="\n\n")


def shopRegionSeed():
    truncate("region")
    truncate("shop")
    with open(os.path.join(csv_file_path + 'shops_with_regions.csv'), 'r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            region, created = Region.objects.get_or_create(
                title_ru=line[2],
                title_uz=line[2],
            )

            Shop.objects.create(
                title_ru=line[1],
                region_id=region.id,
            )
    print("Shop with region import successfully!", end="\n\n")


def departmentSeed():
    # truncate("department")
    with open(os.path.join(csv_file_path + 'departments.csv'), 'r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            Department.objects.create(
                title=line[1],
            )
    print("Department import successfully!", end="\n\n")


def problemSeed():
    # truncate("problem")
    with open(os.path.join(csv_file_path + 'problems.csv'), 'r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            Problem.objects.create(
                title=line[1],
            )
    print("Problem import successfully!", end="\n\n")


def disparitySeed():
    # truncate("disparity")
    with open(os.path.join(csv_file_path + 'disparities.csv'), 'r', encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            Disparity.objects.create(
                title=line[1],
                problem_id=line[5],
            )
    print("Disparity import successfully!", end="\n\n")


def adminSeed():
    # truncate_token()
    # truncate("admin")

    admin_data = {"login": "admin"}

    admin = Admin.objects.create_superuser(
        phone=admin_data['login'],
        password=admin_data['login'],
        name=admin_data['login'],
    )

    for i in range(1, 5):
        Admin.objects.create_is_staff(
            phone=998971111110 + i,
            name=f"ali{i}",
            password=admin_data['login'],
        )

    print("Admin import successfully!", end="\n\n")


def clientSeed():
    # truncate("client")
    for i in range(1, 15):
        Client.objects.create(
            phone=998971111110 + i,
            tg_id=1 + i,
            name="client" + str(i)
        )
    print("Client was create successfully")


def delete_upload_folder(path):
    folder_path = settings.MEDIA_ROOT + path
    try:
        shutil.rmtree(folder_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (folder_path, e))


def violationSeed():
    truncate("violation")
    delete_upload_folder("/uploads/photo")

    with open("media/test/test.png", 'rb') as f:

        for i in range(1, 3000):
            client_list = Client.objects.values_list('id')
            client_id = random.choice(client_list)[0]

            region_list = Region.objects.values_list('id')
            region_id = random.choice(region_list)[0]

            shop_list = Shop.objects.filter(region_id=region_id).values_list('id')
            shop_id = random.choice(shop_list)[0]

            is_no_violation = random.choice([0, 1])
            if is_no_violation == 0:
                department_list = Department.objects.values_list('id')
                department_id = random.choice(department_list)[0]

                problem_list = Problem.objects.values_list('id')
                problem_id = random.choice(problem_list)[0]

                disparity_list = Disparity.objects.filter(problem_id=problem_id).values_list('id')
                disparity_id = random.choice(disparity_list)[0]

                comment = "test_comment"
            else:
                department_id = None
                problem_id = None
                disparity_id = None
                comment = "Нет нарушений"

            statuses = Status.objects.values_list('id')
            random_statuses_id = random.choice(statuses)[0]

            if random_statuses_id > 1:
                admins = Admin.objects.filter(is_staff=1, is_superuser=0).values_list('id')
                random_admins_id = random.choice(admins)[0]

                processes = Process.objects.values_list('id')
                random_process_id = random.choice(processes)[0]

                response_person_description = f"response_description {i}"
                result_action = f"result_action {i}"
            else:
                random_admins_id = None
                response_person_description = None
                result_action = None
                random_process_id = None

            Violation.objects.create(
                region_id=region_id,
                shop_id=shop_id,
                department_id=department_id,
                problem_id=problem_id,
                disparity_id=disparity_id,
                comment=comment,
                client_id=client_id,
                process_id=random_process_id,
                response_admin_id=random_admins_id,
                response_person_description=response_person_description,
                result_action=result_action,
                is_no_violation=is_no_violation,
                status_id=random_statuses_id,
                photo=File(f, name=f"test{i}.png"),
            )

    change_date_violation()
    print("Violation import successfully!", end="\n\n")


def change_date_violation():
    violation_last = Violation.objects.order_by("-id").first().id

    def week_day_func(year, month, day):
        intDay = datetime.date(year=year, month=month, day=day).weekday()

        return intDay

    start_pk = 1
    end_pk = 10
    day = 0
    month = 1
    year = 2021
    while True:
        if start_pk <= violation_last:
            day += 1
            try:
                week_day = week_day_func(year, month, day)
                if week_day not in [5, 6]:
                    violations = Violation.objects.filter(pk__gte=start_pk, pk__lte=end_pk).update(
                        created_at=f"{year}-{month}-{day} 05:13:11.887018",
                        updated_at=f"{year}-{month}-{day} 05:13:11.887018",
                    )
                else:
                    continue
                start_pk += 10
                end_pk += 10
            except ValueError:
                day = 0
                month += 1
                if month == 12:
                    month = 1
                    year += 1
        else:
            return False
    print("Violation date change successfully!", end="\n\n")


def fix_shops_name():
    shops = Shop.global_objects.all()
    for shop in shops:
        shop.name = f"M{shop.name[1:]}"
        shop.save()

    print("Shop name fixed successfully!", end="\n\n")


def new_shop_parse():
    shop_delete = Shop.objects.all().delete()

    def get_prefix_name(name):
        prefix = name.split(" ")[0]
        return prefix + " "

    with open("media/csv/shops_new.csv", 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for line in reader:
            shop_from_csv = get_prefix_name(line[0])
            try:
                shop_from_db = Shop.global_objects.filter(name__contains=shop_from_csv).get()
                shop_from_db.restore()
            except Shop.DoesNotExist:
                shop_create = Shop.objects.create(name=line[0], region_id=1)
    print("Shop parsed successfully!", end="\n\n")


def clear_data():
    truncate("client")
    truncate("violation")


def dbSeed():
    check_foreign_key(0)
    adminSeed()
    # clientSeed()
    # processAdminSeed()
    # statusAdminSeed()
    # buttonSeed()
    # contentSeed()
    # shopRegionSeed()
    # departmentSeed()
    # problemSeed()
    # disparitySeed()
    # violationSeed()
    # clear_data()
    check_foreign_key(1)
    print("OK!")
