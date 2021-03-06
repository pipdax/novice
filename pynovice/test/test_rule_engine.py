# coding=utf-8
# /usr/bin/env python

'''
Author: wenqiangw
Email: wenqiangw@opera.com
Date: 2020-04-24 15:40
Desc:
'''
from pynovice.rule_engine import RuleParser

def rule_pattern(_iterm):
    age = _iterm.get('profile_age',0)
    sms_len = _iterm.get('sms_len',0)
    micro_loan_len = _iterm.get('micro_loan_len', 0)
    endBillsLen = _iterm.get('endBillsLen', 0)
    maxDueday = _iterm.get('maxDueday', 0)
    this_apply_dueday_predicted_score = _iterm.get('this_apply_dueday_predicted_score', 0)

    _pattern = [
        'OR#old#',
            ['between#rule_10',age,18,55],
            ['>#rule_11',sms_len,50],
            ['<#rule_12',micro_loan_len,8],
            ['<', micro_loan_len, -99],
            ['and#rule_40',
                ['>',endBillsLen,4],
                ['>',maxDueday,20],
                ['>',this_apply_dueday_predicted_score,20]
             ]
    ]
    return _pattern


if __name__ == '__main__':
    iterm = {'age': 30.00, 'sms_len': 70, 'micro_loan_len': 10, 'endBillsLen': 5, 'maxDueday': 20,
             'this_apply_dueday_predicted_score': 10}

    iterm = {'userId': '154306317635289088',
               'history_loan_status': True,
               'salary': 'above 25000',
               'loan_num_1day': 1,
               'hit_device_bl': True,
               'hit_mac_bl': False,
               'hit_mobile_bl': False,
               'hit_white_list': False,
               'age': 0.0,
               'nationalId_match_name': False,
               'nationalId_used': False,
               'hit_credit_bl': False,
               'contacts_len': 3037,
               'sms_len': 1875,
               'contain_mpesa': True,
               'contain_username': True,
               'mobile_in_applicantDB': False,
               'mobile_match_set_status': True,
               'mobile_match_set_len': 0,
               'referee_in_applicantDB': False,
               'referee_match_set_status': False,
               'referee_in_applicantDB_referee': True,
               'referee_match_referee_set_status': True,
               'referee_match_referee_set_len': 3,
               'online_duration': 400,
               'company': 'Metropol',
               'gender': 'M',
               'mobiLoanScore': 0,
               'is_unemployed': False,
               'micro_loan_len': 0,
               'user_category': 'old',
               'apply_hour': 0,
               'frequent_contact': 0,
               'simi_score': 0.0,
               'faceNum': -1,
               'faceLiveness': 0.0,
               'max_levenshtein': 0,
               'opesa_maxdueday': -1,
               'opesa_waitdueday': -1,
               'total_borrowing': 2500.0,
               'is_smsmsg': 0,
               'interaction_order': 1,
               'score': 0,
               'pass': True,
               'reason': 'ok',
               'apply_period_length': 91,
               'tags': '[]',
               'gaid_cnt': 2,
               'email_duplicate_cnt': 2,
               'referee_mobile_duplicate_cnt': 3,
               'today_passed_risk_info': 0,
               'latest_balance_in_sms': 0.84,
               'idTimes': 0,
               'maritalStatus': 'Single',
               'hasOutstandingLoan': 'No',
               'employmentDetails': 'Permanent',
               'residentialStatus': 'Rented',
               'eduLevel': 'Graduate',
               'mobile_no': '254703818484',
               'isBtc': 0,
               'isAdmin': 0,
               'num_is_admin_apply': 0,
               'num_is_admin_passed': 0,
               'num_is_btc_apply': 0,
               'num_is_btc_passed': 0,
               'gps_cell_token': '182f476c',
               'apply_term': 2,
               'hit_grey_mobile': False,
               'zh_sms_len': 0,
               'apply_amount': 2500.0,
               'profile_age': 26.063013698630137,
               'gps_tile_new_apply_change_rate': -0.9999850002249967,
               'gps_tile_new_apply_passrate_change_rate': 0.0,
               'gps_tile_today_new_apply': 0.0,
               'gps_tile_today_new_passrate': 0.0,
               'has_android_root_tools': None,
               'app_contains_whatsapp': True,
               'sms_sent_cnt': 778,
               'sms_sent_ratio': 0.41,
               'hit_sensitive_content': True,
               'hit_multiple_loans': 0.0,
               'hit_multiple_loans_d15': 0.0,
               'hit_student_content': True,
               'sms_contains_username': False,
               'affiliate_waitduebill_cnt': 0,
               'affiliate_waitbill_cnt': 0,
               'loan_history_service_is_live': True,
               'affiliate_maxdueday': -1,
               'affiliate_endbills_cnt_max': 1,
               'hit_sensitive_title': False,
               'num_firstloan_passed': 0,
               'num_reloan_passed': 0,
               'num_longperiod_passed': 0,
               'num_reloan_longperiod_passed': 0,
               'num_rule_19_passed': 0,
               'num_rule_38_passed': 0,
               'num_ok_19_passed': 0,
               'num_ok_38_passed': 0,
               'num_ok_passed': 0,
               'num_old_passed': 0,
               'num_old_19_passed': 0,
               'hit_internal_bl': True,
               'hit_internal_bl_by_manual': False,
               'black_nationalid_service_is_live': True,
               'emergency_is_self': False,
               'emergency_contact_in_contacts': True,
               'gps_is_empty': False,
               'gps_cheat': False,
               'gps_covid19': False,
               'hours_passed_since_apply': 1.985,
               'hit_loaned_content': 0,
               'bank_transfer_in_times': 1,
               'overpaid_amount': 0,
               'kenya': {'num_firstloan_passed': 2, 'num_reloan_passed': 0},
               '_risk_scene': 'ReLoanRiskEvent',
               'risk_passed': True,
               'maxDueday': 50,
               'endBillsLen': 2,
               'is_manual': False,
               'this_apply_dueday_predicted': -999,
               'this_apply_dueday_predicted_score': 0.0,
               'cache': {'okash': {'stats:pass': {'num_firstloan_passed': 0,
                                                  'num_reloan_passed': 0,
                                                  'num_longperiod_passed': 0,
                                                  'num_reloan_longperiod_passed': 0,
                                                  'num_rule_19_passed': 0,
                                                  'num_rule_38_passed': 0,
                                                  'num_ok_19_passed': 0,
                                                  'num_ok_38_passed': 0,
                                                  'num_ok_passed': 0,
                                                  'num_old_passed': 0,
                                                  'num_old_19_passed': 0,
                                                  'app': 'OKash'}},
                         'opesa': {'loan:history': {'maxdueday': -1,
                                                    'waitduebill_cnt': 0,
                                                    'waitbill_cnt': 0,
                                                    'waitmaxdueday': -999,
                                                    'waitbilltotal': '0.0',
                                                    'endbill_cnt': 1,
                                                    'app': 'OPesa'},
                                   'stats:pass': {'num_firstloan_passed': 0,
                                                  'num_reloan_passed': 0,
                                                  'num_longperiod_passed': 0,
                                                  'num_reloan_longperiod_passed': 0,
                                                  'num_rule_19_passed': 0,
                                                  'num_rule_38_passed': 0,
                                                  'num_ok_19_passed': 0,
                                                  'num_ok_38_passed': 0,
                                                  'num_ok_passed': 0,
                                                  'num_old_passed': 0,
                                                  'num_old_19_passed': 0,
                                                  'app': 'OPesa'}},
                         'credithela': {'loan:history': {'maxdueday': -999,
                                                         'waitduebill_cnt': 0,
                                                         'waitbill_cnt': 0,
                                                         'waitmaxdueday': -999,
                                                         'waitbilltotal': -999,
                                                         'endbill_cnt': 0,
                                                         'app': 'CreditHela'},
                                        'stats:pass': {'num_firstloan_passed': 2,
                                                       'num_reloan_passed': 0,
                                                       'num_longperiod_passed': 0,
                                                       'num_reloan_longperiod_passed': 0,
                                                       'num_rule_19_passed': 0,
                                                       'num_rule_38_passed': 0,
                                                       'num_ok_19_passed': 0,
                                                       'num_ok_38_passed': 0,
                                                       'num_ok_passed': 2,
                                                       'num_old_passed': 0,
                                                       'num_old_19_passed': 0,
                                                       'app': 'CreditHela'}}}}

    rule = rule_pattern(iterm)

    engine = RuleParser()
    out = engine.evaluate(_rule=rule)
    print(engine.get_hit_rules())
    print(out)