from django.shortcuts import render
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
from django.conf import settings
from django.http import JsonResponse
import googleapiclient.discovery
from googleapiclient.http import MediaFileUpload

def home(request):
    context = {}
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
        credentials = ServiceAccountCredentials.from_json_keyfile_name(settings.BASE_DIR / "arizona-reporting-49bd39a9760f.json", scopes) #access the json key you downloaded earlier 
        file = gspread.authorize(credentials) # authenticate the JSON key with gspread
        sheet = file.open("Arizona Reporting")  #open sheet
        worksheet = sheet.sheet1  #replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1
        
        list_of_lists = worksheet.get_all_values()
        count = len(list_of_lists) + 1
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
        if len(device_download_time) > 3:
            worksheet.update_cell(count, 17, device_download_time)
        else:
            worksheet.update_cell(count, 17, "")
        worksheet.update_cell(count, 18, tampering_occurrence_date)
        worksheet.update_cell(count, 19, bca_violation_date_1)
        worksheet.update_cell(count, 20, bca_violation_date_2)
        worksheet.update_cell(count, 21, bca_violation_date_3)
        worksheet.update_cell(count, 22, device_id)
        worksheet.update_cell(count, 23, tech_id)
        worksheet.update_cell(count, 24, bypass_approval)
        if len(bypass_time) > 3:
            worksheet.update_cell(count, 25, bypass_time)
        else:
            worksheet.update_cell(count, 25, "")
        worksheet.update_cell(count, 26, vin)
        worksheet.update_cell(count, 27, interlock_order)
        if len(bca_violation_time_1) > 3:
            worksheet.update_cell(count, 28, bca_violation_time_1)
        else:
            worksheet.update_cell(count, 28, "")
        worksheet.update_cell(count, 29, bca_violation_value_1)
        if len(bca_violation_time_2) > 3:
            worksheet.update_cell(count, 30, bca_violation_time_2)
        else:
            worksheet.update_cell(count, 30, "")
        worksheet.update_cell(count, 31, bca_violation_value_2)
        if len(bca_violation_time_3) > 3:
            worksheet.update_cell(count, 32, bca_violation_time_3)
        else:
            worksheet.update_cell(count, 32, "")
        worksheet.update_cell(count, 33, bca_violation_value_3)
        worksheet.update_cell(count, 34, tampering_violation_count)
        if len(tampering_time_1) > 3:
            worksheet.update_cell(count, 35, tampering_time_1)
        else:
            worksheet.update_cell(count, 35, "")
        if len(tampering_time_2) > 3:
            worksheet.update_cell(count, 36, tampering_time_2)
        else:
            worksheet.update_cell(count, 36, "")
        worksheet.update_cell(count, 37, circumvention_count)
        if len(circumvention_time_1) > 3:
            worksheet.update_cell(count, 38, circumvention_time_1)
        else:
            worksheet.update_cell(count, 38, "")
        if len(circumvention_time_2) > 3:
            worksheet.update_cell(count, 39, circumvention_time_2)
        else:
            worksheet.update_cell(count, 39, "")
        worksheet.update_cell(count, 40, missed_rolling_retest_count)
        if len(missed_rolling_retest_time_1) > 3:
            worksheet.update_cell(count, 41, missed_rolling_retest_time_1)
        else:
            worksheet.update_cell(count, 41, "")
        if len(missed_rolling_retest_time_2) > 3:
            worksheet.update_cell(count, 42, missed_rolling_retest_time_2)
        else:
            worksheet.update_cell(count, 42, "")
        if len(missed_rolling_retest_time_3) > 3:
            worksheet.update_cell(count, 43, missed_rolling_retest_time_3)
        else:
            worksheet.update_cell(count, 43, "")
        if len(missed_rolling_retest_time_4) > 3:
            worksheet.update_cell(count, 44, missed_rolling_retest_time_4)
        else:
            worksheet.update_cell(count, 44, "")
        if len(missed_rolling_retest_time_5) > 3:
            worksheet.update_cell(count, 45, missed_rolling_retest_time_5)
        else:
            worksheet.update_cell(count, 45, "")
        if len(missed_rolling_retest_time_6) > 3:
            worksheet.update_cell(count, 46, missed_rolling_retest_time_6)
        else:
            worksheet.update_cell(count, 46, "")
        worksheet.update_cell(count, 47, send_as_received)

        context["msg"] = "File Save Successfully!"
        return render(request, "report/home.html", context)
    return render(request, "report/home.html", context)

def export_text_file(request):
    if request.method == 'POST':
        scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
        ]
        credentials = ServiceAccountCredentials.from_json_keyfile_name(settings.BASE_DIR / "arizona-reporting-49bd39a9760f.json", scopes)
        file = gspread.authorize(credentials) 
        sheet = file.open("Arizona Reporting") 
        worksheet = sheet.sheet1
        rows = worksheet.get_all_values()
        # rows = rows[1:]
        with open(settings.BASE_DIR / 'media/toadot.txt', 'w') as f:
            for row in rows:
                f.write(row[0] + " "*(3-len(row[0])))
                f.write(row[1] + " "*(3-len(row[1])))
                f.write(row[2] + " "*(3-len(row[2])))
                f.write(row[3] + " "*(30-len(row[3])))
                f.write(row[4] + " "*(30-len(row[4])))
                f.write(row[5] + " "*(30-len(row[5])))
                f.write(row[6] + " "*(8-len(row[6])))
                f.write(row[7] + " "*(25-len(row[7])))
                f.write(row[8] + " "*(8-len(row[8])))
                f.write(row[9] + " "*(8-len(row[9])))
                f.write(row[10] + " "*(8-len(row[10])))
                f.write(row[11] + " "*(1-len(row[11])))
                f.write(row[12] + " "*(1-len(row[12])))
                f.write(row[13] + " "*(4-len(row[13])))
                f.write(row[14] + " "*(2-len(row[14])))
                f.write(row[15] + " "*(8-len(row[15])))
                f.write(row[16] + " "*(11-len(row[16])))
                f.write(row[17] + " "*(8-len(row[17])))
                f.write(row[18] + " "*(8-len(row[18])))
                f.write(row[19] + " "*(8-len(row[19])))
                f.write(row[20] + " "*(8-len(row[20])))
                f.write(row[21] + " "*(18-len(row[21])))
                f.write(row[22] + " "*(12-len(row[22])))
                f.write(row[23] + " "*(1-len(row[23])))
                f.write(row[24] + " "*(11-len(row[24])))
                f.write(row[25] + " "*(6-len(row[25])))
                f.write(row[26] + " "*(3-len(row[26])))
                f.write(row[27] + " "*(11-len(row[27])))
                f.write(row[28] + " "*(3-len(row[28])))
                f.write(row[29] + " "*(11-len(row[29])))
                f.write(row[30] + " "*(3-len(row[30])))
                f.write(row[31] + " "*(11-len(row[31])))
                f.write(row[32] + " "*(3-len(row[32])))
                f.write(row[33] + " "*(2-len(row[33])))
                f.write(row[34] + " "*(11-len(row[34])))
                f.write(row[35] + " "*(11-len(row[35])))
                f.write(row[36] + " "*(2-len(row[36])))
                f.write(row[37] + " "*(11-len(row[37])))
                f.write(row[38] + " "*(11-len(row[38])))
                f.write(row[39] + " "*(3-len(row[39])))
                f.write(row[40] + " "*(11-len(row[40])))
                f.write(row[41] + " "*(11-len(row[41])))
                f.write(row[42] + " "*(11-len(row[42])))
                f.write(row[43] + " "*(11-len(row[43])))
                f.write(row[44] + " "*(11-len(row[44])))
                f.write(row[45] + " "*(11-len(row[45])))
                f.write(row[46] + " "*(50-len(row[46])))
                f.write("\n")

        service = googleapiclient.discovery.build('drive', 'v3',credentials=credentials)
        folder_id = "1siDQTsb0mKRaJl6qYnW7yS6w3pE4Nice"
        file_names = ["toadot.txt"]
        mime_types = ["text/plain"]

        for file_name, mime_type in zip(file_names, mime_types):
            file_metadata = {
                "name": file_name,
                "parents": [folder_id],
            }
            media = MediaFileUpload(settings.BASE_DIR / "media/toadot.txt", mimetype="text/plain")
            service.files().create(
                body=file_metadata,
                media_body=media,
                fields="id"
            ).execute()
        
    return JsonResponse({"status":True})