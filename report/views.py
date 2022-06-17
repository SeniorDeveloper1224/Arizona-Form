from django.shortcuts import render
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json

def home(request):
    context = {}
    print(request.POST)
    if request.method == 'POST':
        manufacturer_id = request.POST.get('manufacturer_id')
        provider_id = request.POST.get('provider_id')
        installer_id = request.POST.get('installer_id')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        date_of_birth = request.POST.get('date_of_birth').replace("-","")
        dl = request.POST.get('dl')
        mvd_uninstall_date = request.POST.get('mvd_uninstall_date').replace("-","")
        report_type = request.POST.get('report_type')
        install_date = request.POST.get('install_date').replace("-","")
        removal_date = request.POST.get('removal_date').replace("-","")
        non_compliance_code = request.POST.get('non_compliance_code')
        bca_violation_count = request.POST.get('bca_violation_count')
        device_download_date = request.POST.get('device_download_date').replace("-","")
        device_download_time = request.POST.get('device_download_time') + ":00"
        bca_violation_date_1 = request.POST.get('bca_violation_date_1').replace("-","")
        bca_violation_time_1 = request.POST.get('bca_violation_time_1') + ":00"
        bca_violation_value_1 = request.POST.get('bca_violation_value_1')
        bca_violation_date_2 = request.POST.get('bca_violation_date_2').replace("-","")
        bca_violation_time_2 = request.POST.get('bca_violation_time_2') + ":00"
        bca_violation_value_2 = request.POST.get('bca_violation_value_2')
        bca_violation_date_3 = request.POST.get('bca_violation_date_3').replace("-","")
        bca_violation_time_3 = request.POST.get('bca_violation_time_3') + ":00"
        bca_violation_value_3 = request.POST.get('bca_violation_value_3')
        tampering_occurrence_date = request.POST.get('tampering_occurrence_date').replace("-","")
        device_id = request.POST.get('device_id')
        tech_id = request.POST.get('tech_id')
        bypass_approval = request.POST.get('bypass_approval')
        bypass_time = request.POST.get('bypass_time') + ":00"
        returned_error_code = request.POST.get('returned_error_code')
        vin = request.POST.get('vin')
        interlock_order = request.POST.get('interlock_order')
        tampering_violation_count = request.POST.get('tampering_violation_count')
        tampering_time_1 = request.POST.get('tampering_time_1') + ":00"
        tampering_time_2 = request.POST.get('tampering_time_2') + ":00"
        circumvention_count = request.POST.get('circumvention_count')
        circumvention_time_1 = request.POST.get('circumvention_time_1') + ":00"
        circumvention_time_2 = request.POST.get('circumvention_time_2') + ":00"
        missed_rolling_retest_count = request.POST.get('missed_rolling_retest_count')
        missed_rolling_retest_time_1 = request.POST.get('missed_rolling_retest_time_1') + ":00"
        missed_rolling_retest_time_2 = request.POST.get('missed_rolling_retest_time_2') + ":00"
        missed_rolling_retest_time_3 = request.POST.get('missed_rolling_retest_time_3') + ":00"
        missed_rolling_retest_time_4 = request.POST.get('missed_rolling_retest_time_4') + ":00"
        missed_rolling_retest_time_5 = request.POST.get('missed_rolling_retest_time_5') + ":00"
        missed_rolling_retest_time_6 = request.POST.get('missed_rolling_retest_time_6') + ":00"
        send_as_received = request.POST.get('send_as_received')

        scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
        ]
        credentials = ServiceAccountCredentials.from_json_keyfile_name("arizona-reporting-49bd39a9760f.json", scopes) #access the json key you downloaded earlier 
        file = gspread.authorize(credentials) # authenticate the JSON key with gspread
        sheet = file.open("Arizona Reporting")  #open sheet
        worksheet = sheet.sheet1  #replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1
        count = 1
        while True:
            row = worksheet.row_values(count)
            if len(row) <= 0:
                break
            count += 1
        worksheet.update_cell(count, 1, manufacturer_id)
        worksheet.update_cell(count, 2, provider_id)
        worksheet.update_cell(count, 3, installer_id)
        worksheet.update_cell(count, 4, last_name)
        worksheet.update_cell(count, 5, first_name)
        worksheet.update_cell(count, 6, middle_name)
        worksheet.update_cell(count, 7, date_of_birth)
        worksheet.update_cell(count, 8, dl)
        worksheet.update_cell(count, 9, install_date)
        worksheet.update_cell(count, 10, mvd_uninstall_date)
        worksheet.update_cell(count, 11, removal_date)
        worksheet.update_cell(count, 12, report_type)
        worksheet.update_cell(count, 13, non_compliance_code)
        worksheet.update_cell(count, 14, bca_violation_count)
        worksheet.update_cell(count, 15, returned_error_code)
        worksheet.update_cell(count, 16, device_download_date)
        worksheet.update_cell(count, 17, device_download_time)
        worksheet.update_cell(count, 18, tampering_occurrence_date)
        worksheet.update_cell(count, 19, bca_violation_date_1)
        worksheet.update_cell(count, 20, bca_violation_date_2)
        worksheet.update_cell(count, 21, bca_violation_date_3)
        worksheet.update_cell(count, 22, device_id)
        worksheet.update_cell(count, 23, tech_id)
        worksheet.update_cell(count, 24, bypass_approval)
        worksheet.update_cell(count, 25, bypass_time)
        worksheet.update_cell(count, 26, vin)
        worksheet.update_cell(count, 27, interlock_order)
        worksheet.update_cell(count, 28, bca_violation_time_1)
        worksheet.update_cell(count, 29, bca_violation_value_1)
        worksheet.update_cell(count, 30, bca_violation_time_2)
        worksheet.update_cell(count, 31, bca_violation_value_2)
        worksheet.update_cell(count, 32, bca_violation_time_3)
        worksheet.update_cell(count, 33, bca_violation_value_3)
        worksheet.update_cell(count, 34, tampering_violation_count)
        worksheet.update_cell(count, 35, tampering_time_1)
        worksheet.update_cell(count, 36, tampering_time_2)
        worksheet.update_cell(count, 37, circumvention_count)
        worksheet.update_cell(count, 38, circumvention_time_1)
        worksheet.update_cell(count, 39, circumvention_time_2)
        worksheet.update_cell(count, 40, missed_rolling_retest_count)
        worksheet.update_cell(count, 41, missed_rolling_retest_time_1)
        worksheet.update_cell(count, 42, missed_rolling_retest_time_2)
        worksheet.update_cell(count, 43, missed_rolling_retest_time_3)
        worksheet.update_cell(count, 44, missed_rolling_retest_time_4)
        worksheet.update_cell(count, 45, missed_rolling_retest_time_5)
        worksheet.update_cell(count, 46, missed_rolling_retest_time_6)
        worksheet.update_cell(count, 47, send_as_received)

        context["msg"] = "File Save Successfully!"
        return render(request, "report/home.html", context)
    return render(request, "report/home.html", context)