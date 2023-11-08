FOLD_NAME = 'mskf_user'
FOLD_NUM = 5
RANDOM_STATE = 46

TARGET_TASK = '2'

XGB_MDOEL_PARAMS = {
    'max_depth': 10,
    'learning_rate': 0.1,
    'subsample': 1.0,
    'colsample_bytree': 0.30,
    'tree_method': 'hist',
    'seed': RANDOM_STATE,
    'nthread': 20,
}

XGB_TRAIN_PARAMS = {
    "num_boost_round": 5000,
    "early_stopping_rounds": 50,
    "verbose_eval": 100,
}

if TARGET_TASK == '1':
    XGB_MDOEL_PARAMS['eval_metric'] = ['logloss', 'auc', 'error@0.5']
    XGB_MDOEL_PARAMS['objective'] = 'binary:logistic'
if TARGET_TASK == '2':
    XGB_MDOEL_PARAMS['eval_metric'] = ['mlogloss', 'merror']
    XGB_MDOEL_PARAMS['objective'] = 'multi:softprob'
    XGB_MDOEL_PARAMS['num_class'] = 4


subject_id_list = [
    3,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
    51,
    52,
    53,
    54,
    55,
    56,
    57,
    58,
    59,
    60,
    61,
    62,
    63,
    64,
    65,
    66,
    67,
    68,
    69,
    70,
    71,
    72,
    73,
    74,
    75,
    76,
    77,
    78,
    79,
    80,
    81,
    83,
    84,
    85,
    86,
    87,
    88,
    89,
    90,
    91,
    92,
    93,
    94,
    95,
    96,
    97,
    98,
    99,
    100,
    101,
    102,
    103,
    104,
    105,
    106,
    107,
    108,
    109,
    110,
    111,
    112,
    113,
    114,
    115,
    116,
    117,
    118,
    119,
    120,
    126,
    128,
    129,
    130,
    131,
    137,
    139,
    140,
    141,
    142,
    144,
    146,
    149,
    151,
    152,
    153,
    154,
    156,
    157,
    158,
    159,
    160,
    163,
    164,
    165,
    166,
    167,
    168,
    171,
    172,
    173,
    174,
    175,
    176,
    177,
    178,
    179,
    180,
    181,
    182,
    183,
    184,
    185,
    186,
    187,
    188,
    189,
    190,
    191,
    192,
    193,
    195,
    196,
    197,
    198,
    199,
    200,
    202,
    203,
    204,
    205,
    206,
    207,
    208,
    209,
    210,
    211,
    212,
    213,
    214,
    215,
    216,
    217,
    218,
    219,
    220,
    221,
    222,
    223,
    224,
    225,
    226,
    227,
    228,
    229,
    230,
    231,
    232,
    233,
    234,
    235,
    236,
    237,
    238,
    239,
    240,
    241,
    242,
    243,
    244,
    245,
    246,
    247,
    248,
    249,
    250,
    251,
    252,
    253,
    254,
    255,
    256,
    257,
    258,
    259,
    260,
    261,
    262,
    263,
    264,
    265,
    266,
    267,
    268,
    269,
    270,
    271,
    272,
    273,
    274,
    275,
    276,
    277,
    278,
    279,
    280,
    281,
    282,
    283,
    284,
    298,
    313,
    315,
    317,
    331,
    332,
    334,
    335,
    336,
    337,
    338,
    339,
    340,
    341,
    342,
    343,
    344,
    348,
    349,
    350,
    351,
    352,
    353,
    354,
    355,
    361,
    365,
    366,
    367,
    369,
    370,
    371,
    372,
    374,
    375,
    376,
    377,
    388,
    406,
    407,
    408,
    409,
    410,
    411,
    412,
    416,
    417,
    418,
    430,
    431,
    432,
    434,
    435,
    436,
    437,
    439,
    441,
    442,
    446,
    447,
    448,
    451,
    453,
    462,
    474,
    480,
    487,
    539,
    540,
    649,
    654,
    655,
    656,
    657,
    692,
    698,
    700,
    1059,
    1076,
    1077,
    1078,
    1079,
    1080,
    1081,
    1082,
    1156,
    1157,
    1158,
    1159,
    1160,
    1161,
    1162,
    1163,
    1164,
    1165,
    1166,
    1167,
    1168,
    1169,
    1170,
    1171,
    1172,
    1173,
    1174,
    1175,
    1176,
    1177,
    1178,
    1179,
    1180,
    1181,
    1182,
    1183,
    1184,
    1185,
    1186,
    1187,
    1188,
    1189,
    1200,
    1201,
    1202,
    1203,
    1204,
    1207,
    1208,
    1209,
    1210,
    1211,
    1212,
    1213,
    1214,
    1215,
    1216,
    1217,
    1218,
    1219,
    1263,
    1264,
    1265,
    1266,
    1636,
    1642,
    1647,
    1648,
    1649,
    1650,
    1651,
    1675,
    1676,
    1750,
    1975,
    1976,
    1977,
    1980,
    1982,
    1983,
    1985,
    1987,
    1988
]

level_cnum_list = [
    '0_8',
    '1_16',
    '3_0',
    '2_3',
    '2_4',
    '2_5',
    '2_10',
    '2_7',
    '1_14',
    '2_11',
    '2_6',
    '2_9',
    '2_8',
    '1_5',
    '1_12',
    '2_1',
    '2_13',
    '1_1',
    '1_4',
    '2_2',
    '2_14',
    '1_0',
    '2_0',
    '0_1'
]


subject_meta_cols = [
    'num',
    'max_level',
    'sum_level',
    'max_cnum',
    'sum_cnum',
]

subject_features = [f'subj_{f}' for f in subject_id_list]
level_cnum_features = [f'subj_{f}' for f in level_cnum_list]
subject_meta_features = [f'subj_{f}' for f in subject_meta_cols]

user_lag_num_features = [
    'DateAnswered_dt_diff',
    'DateAnswered_dt_diff_cumsum',
    'DateAnswered_dt_diff_shift',
    'DateAnswered_dt_diff_cumsum_shift',
    'answer_num',
    'answer_num_norm',
    'quiz_answer_num',
    'quiz_answer_num_norm',
    'quiz_unique_num',
    'subj_unique_num',
    'group_unique_num',
    'subjcat_unique_num',
]
user_lag_cat_features = [
    'answer_num_div5',
    'quiz_answer_num_div5',
    'change_subjcat',
    'answered_subjcat',
    'prev_question',
    'prev_subjcat',
]
user_lag_multicat_features = [
    'prev10_question',
    'prev10_subjcat',
]
user_lag_features = user_lag_num_features + user_lag_cat_features + user_lag_multicat_features

answer_date_features = [
    'DateAnswered_weekday',
    'DateAnswered_hour',
    'DateAnswered_day',
    'DateAnswered_wom'
]
count_encording_cat = [
    'QuestionId',
    'UserId',
    'Gender',
    'PremiumPupil',
    'Confidence',
    'GroupId',
    'QuizId',
    'SchemeOfWorkId',
    'age_years',
    'DateAnswered_weekday',
    'DateAnswered_hour',
    'DateAnswered_day',
    'DateAnswered_wom',
    'answer_num_div5',
    'quiz_answer_num_div5',
    'change_subjcat',
    'answered_subjcat',
    'prev_question',
    'prev_subjcat',
    'SubjectId_cat',
    'pri_to_high_stu',
    ['UserId', 'DateAnswered_weekday'],
    ['UserId', 'DateAnswered_hour'],
    ['UserId', 'DateAnswered_day'],
    ['UserId', 'DateAnswered_wom'],
    ['UserId', 'DateAnswered_weekday', 'DateAnswered_hour'],
    ['UserId', 'DateAnswered_weekday', 'DateAnswered_wom'],
    ['UserId', 'Confidence'],
    ['UserId', 'SchemeOfWorkId'],
    ['UserId', 'GroupId'],
    ['UserId', 'QuizId'],
    ['UserId', 'SubjectId_cat'],
    ['UserId', 'answer_num_div5'],
    ['UserId', 'quiz_answer_num_div5'],
    ['UserId', 'change_subjcat'],
    ['UserId', 'answered_subjcat'],
    ['UserId', 'age_years'],
    ['UserId', 'age_years', 'Confidence'],
    ['QuestionId', 'Confidence'],
    ['QuestionId', 'SchemeOfWorkId'],
    ['QuestionId', 'age_years'],
    ['QuestionId', 'Gender'],
    ['QuestionId', 'answer_num_div5'],
    ['QuestionId', 'quiz_answer_num_div5'],
    ['QuestionId', 'change_subjcat'],
    ['QuestionId', 'answered_subjcat'],
    ['QuestionId', 'PremiumPupil'],
    ['QuestionId', 'Gender', 'PremiumPupil'],
    ['QuestionId', 'age_years', 'Gender'],
    ['QuestionId', 'age_years', 'PremiumPupil'],
    ['QuestionId', 'age_years', 'Gender', 'PremiumPupil'],
    ['QuestionId', 'Confidence', 'PremiumPupil'],
    ['QuestionId', 'Confidence', 'Gender', 'PremiumPupil'],
    ['QuestionId', 'Confidence', 'age_years', 'Gender'],
    ['QuestionId', 'Confidence', 'age_years', 'PremiumPupil'],
    ['QuestionId', 'Confidence', 'age_years', 'Gender', 'PremiumPupil'],
    ['QuestionId', 'prev_question'],
    ['QuestionId', 'DateOfBirth_NaN'],
    ['QuestionId', 'pri_to_high_stu'],
    ['SubjectId_cat', 'Confidence'],
    ['SubjectId_cat', 'SchemeOfWorkId'],
    ['SubjectId_cat', 'age_years'],
    ['SubjectId_cat', 'Gender'],
    ['SubjectId_cat', 'answer_num_div5'],
    ['SubjectId_cat', 'quiz_answer_num_div5'],
    ['SubjectId_cat', 'change_subjcat'],
    ['SubjectId_cat', 'answered_subjcat'],
    ['QuestionId', 'GroupId'],
    ['QuestionId', 'QuizId'],
    ['SchemeOfWorkId', 'Confidence'],
    ['SchemeOfWorkId', 'GroupId'],
    ['SchemeOfWorkId', 'QuizId'],
    ['SchemeOfWorkId', 'age_years'],
    ['SchemeOfWorkId', 'Gender'],
    ['SchemeOfWorkId', 'answer_num_div5'],
    ['SchemeOfWorkId', 'quiz_answer_num_div5'],
    ['SchemeOfWorkId', 'change_subjcat'],
    ['SchemeOfWorkId', 'answered_subjcat'],
    ['SchemeOfWorkId', 'PremiumPupil'],
    ['SchemeOfWorkId', 'Gender', 'PremiumPupil'],
    ['SchemeOfWorkId', 'age_years', 'Gender'],
    ['SchemeOfWorkId', 'age_years', 'PremiumPupil'],
    ['SchemeOfWorkId', 'age_years', 'Gender', 'PremiumPupil'],
]
count_encording_features = []
for col in count_encording_cat:
    if not isinstance(col, list):
        col = [col]
    name = "_".join(col)
    count_encording_features.append(f'{name}_ce')

te_smooth_factor = 5
target_encording_cat = [
    'QuestionId',
    'UserId',
    'Gender',
    'PremiumPupil',
    'Confidence',
    'GroupId',
    'QuizId',
    'SchemeOfWorkId',
    'age_years',
    'DateAnswered_weekday',
    'DateAnswered_hour',
    'DateAnswered_day',
    'DateAnswered_wom',
    'answer_num_div5',
    'quiz_answer_num_div5',
    'change_subjcat',
    'answered_subjcat',
    'prev_question',
    'prev_subjcat',
    'SubjectId_cat',
    'DateOfBirth_NaN',
    'pri_to_high_stu',
    ['DateAnswered_day', 'DateAnswered_hour'],
    ['DateAnswered_weekday', 'DateAnswered_hour'],
    ['DateAnswered_weekday', 'DateAnswered_wom'],
    ['UserId', 'DateAnswered_weekday'],
    ['UserId', 'DateAnswered_hour'],
    ['UserId', 'DateAnswered_day'],
    ['UserId', 'DateAnswered_wom'],
    ['UserId', 'DateAnswered_weekday', 'DateAnswered_hour'],
    ['UserId', 'DateAnswered_weekday', 'DateAnswered_wom'],
    ['UserId', 'Confidence'],
    ['UserId', 'SchemeOfWorkId'],
    ['UserId', 'GroupId'],
    ['UserId', 'QuizId'],
    ['UserId', 'SubjectId_cat'],
    ['UserId', 'answer_num_div5'],
    ['UserId', 'quiz_answer_num_div5'],
    ['UserId', 'change_subjcat'],
    ['UserId', 'answered_subjcat'],
    ['UserId', 'age_years'],
    ['UserId', 'age_years', 'Confidence'],
    ['QuestionId', 'Confidence'],
    ['QuestionId', 'SchemeOfWorkId'],
    ['QuestionId', 'age_years'],
    ['QuestionId', 'Gender'],
    ['QuestionId', 'PremiumPupil'],
    ['QuestionId', 'Gender', 'PremiumPupil'],
    ['QuestionId', 'age_years', 'Gender'],
    ['QuestionId', 'age_years', 'PremiumPupil'],
    ['QuestionId', 'age_years', 'Gender', 'PremiumPupil'],
    ['QuestionId', 'Confidence', 'PremiumPupil'],
    ['QuestionId', 'Confidence', 'Gender', 'PremiumPupil'],
    ['QuestionId', 'Confidence', 'age_years', 'Gender'],
    ['QuestionId', 'Confidence', 'age_years', 'PremiumPupil'],
    ['QuestionId', 'Confidence', 'age_years', 'Gender', 'PremiumPupil'],
    ['QuestionId', 'answer_num_div5'],
    ['QuestionId', 'quiz_answer_num_div5'],
    ['QuestionId', 'GroupId'],
    ['QuestionId', 'QuizId'],
    ['QuestionId', 'change_subjcat'],
    ['QuestionId', 'answered_subjcat'],
    ['QuestionId', 'prev_question'],
    ['QuestionId', 'DateOfBirth_NaN'],
    ['QuestionId', 'pri_to_high_stu'],
    ['SubjectId_cat', 'Confidence'],
    ['SubjectId_cat', 'SchemeOfWorkId'],
    ['SubjectId_cat', 'age_years'],
    ['SubjectId_cat', 'Gender'],
    ['SubjectId_cat', 'answer_num_div5'],
    ['SubjectId_cat', 'quiz_answer_num_div5'],
    ['SubjectId_cat', 'change_subjcat'],
    ['SubjectId_cat', 'answered_subjcat'],
    ['SchemeOfWorkId', 'Confidence'],
    ['SchemeOfWorkId', 'GroupId'],
    ['SchemeOfWorkId', 'QuizId'],
    ['SchemeOfWorkId', 'age_years'],
    ['SchemeOfWorkId', 'Gender'],
    ['SchemeOfWorkId', 'answer_num_div5'],
    ['SchemeOfWorkId', 'quiz_answer_num_div5'],
    ['SchemeOfWorkId', 'change_subjcat'],
    ['SchemeOfWorkId', 'answered_subjcat'],
    ['SchemeOfWorkId', 'PremiumPupil'],
    ['SchemeOfWorkId', 'Gender', 'PremiumPupil'],
    ['SchemeOfWorkId', 'age_years', 'Gender'],
    ['SchemeOfWorkId', 'age_years', 'PremiumPupil'],
    ['SchemeOfWorkId', 'age_years', 'Gender', 'PremiumPupil'],
]
target_encording_features = []
for tar in ['IsCorrect']:
    for col in target_encording_cat:
        if not isinstance(col, list):
            col = [col]
        name = "_".join(col)
        target_encording_features.append(f'TE_s{te_smooth_factor}_{name}_{tar}')

target_encording_ansval_features = []
for tar in ['AnswerValue_1', 'AnswerValue_2', 'AnswerValue_3', 'AnswerValue_4']:
    for col in target_encording_cat:
        if not isinstance(col, list):
            col = [col]
        name = "_".join(col)
        target_encording_ansval_features.append(f'TE_s{te_smooth_factor}_{name}_{tar}')

subj_conbi_cols = [
    'UserId',
    'age_years',
    'answered_subjcat',
    'SchemeOfWorkId',
    'Confidence',
]
target_encording_subj_conbi_cat = []
for col in subject_features:
    for col2 in subj_conbi_cols:
        target_encording_subj_conbi_cat.append([col, col2])

target_encording_subj_conbi_features = []
for tar in ['IsCorrect']:
    for col in target_encording_subj_conbi_cat:
        if not isinstance(col, list):
            col = [col]
        name = "_".join(col)
        target_encording_subj_conbi_features.append(f'TE_s{te_smooth_factor}_{name}_{tar}')

target_encording_subj_agg_features = []
for agg_func in ['sum', 'mean', 'std', 'max', 'min']:
    target_encording_subj_agg_features.append(f'TE_s{te_smooth_factor}_subj_agg_{agg_func}_IsCorrect')
for agg_func in ['sum', 'mean', 'std', 'max', 'min']:
    for conbi_col in subj_conbi_cols:
        target_encording_subj_agg_features.append(f'TE_s{te_smooth_factor}_subj_{conbi_col}_agg_{agg_func}_IsCorrect')

svd_n_components = 5
svd_features = []
svd_features += [f'ques_subj_svd_{i}' for i in range(svd_n_components)]
svd_features += [f'user_subj_svd_{i}' for i in range(svd_n_components)]

fs_features = [
    "Confidence_ce",
    "DateAnswered_dt_diff",
    "DateAnswered_dt_diff_cumsum",
    "DateAnswered_dt_diff_cumsum_shift",
    "DateAnswered_dt_diff_shift",
    "GroupId_ce",
    "QuestionId_GroupId_ce",
    "QuestionId_QuizId_ce",
    "QuestionId_ce",
    "QuestionId_quiz_answer_num_div5_ce",
    "QuizId_ce",
    "SchemeOfWorkId_GroupId_ce",
    "SchemeOfWorkId_QuizId_ce",
    "SubjectId_cat",
    "TE_s5_DateAnswered_day_AnswerValue_1",
    "TE_s5_DateAnswered_day_DateAnswered_hour_IsCorrect",
    "TE_s5_GroupId_IsCorrect",
    "TE_s5_QuestionId_AnswerValue_1",
    "TE_s5_QuestionId_AnswerValue_2",
    "TE_s5_QuestionId_AnswerValue_3",
    "TE_s5_QuestionId_AnswerValue_4",
    "TE_s5_QuestionId_Confidence_AnswerValue_1",
    "TE_s5_QuestionId_Confidence_AnswerValue_2",
    "TE_s5_QuestionId_Confidence_AnswerValue_3",
    "TE_s5_QuestionId_Confidence_AnswerValue_4",
    "TE_s5_QuestionId_Confidence_Gender_PremiumPupil_IsCorrect",
    "TE_s5_QuestionId_Confidence_IsCorrect",
    "TE_s5_QuestionId_Confidence_PremiumPupil_IsCorrect",
    "TE_s5_QuestionId_Confidence_age_years_Gender_IsCorrect",
    "TE_s5_QuestionId_Confidence_age_years_Gender_PremiumPupil_IsCorrect",
    "TE_s5_QuestionId_Confidence_age_years_PremiumPupil_IsCorrect",
    "TE_s5_QuestionId_DateOfBirth_NaN_AnswerValue_3",
    "TE_s5_QuestionId_Gender_AnswerValue_1",
    "TE_s5_QuestionId_Gender_AnswerValue_2",
    "TE_s5_QuestionId_Gender_AnswerValue_4",
    "TE_s5_QuestionId_Gender_PremiumPupil_AnswerValue_1",
    "TE_s5_QuestionId_Gender_PremiumPupil_AnswerValue_2",
    "TE_s5_QuestionId_Gender_PremiumPupil_AnswerValue_3",
    "TE_s5_QuestionId_Gender_PremiumPupil_AnswerValue_4",
    "TE_s5_QuestionId_Gender_PremiumPupil_IsCorrect",
    "TE_s5_QuestionId_GroupId_AnswerValue_1",
    "TE_s5_QuestionId_GroupId_AnswerValue_2",
    "TE_s5_QuestionId_GroupId_AnswerValue_3",
    "TE_s5_QuestionId_GroupId_AnswerValue_4",
    "TE_s5_QuestionId_GroupId_IsCorrect",
    "TE_s5_QuestionId_IsCorrect",
    "TE_s5_QuestionId_PremiumPupil_AnswerValue_3",
    "TE_s5_QuestionId_QuizId_AnswerValue_1",
    "TE_s5_QuestionId_QuizId_AnswerValue_2",
    "TE_s5_QuestionId_QuizId_AnswerValue_3",
    "TE_s5_QuestionId_QuizId_AnswerValue_4",
    "TE_s5_QuestionId_QuizId_IsCorrect",
    "TE_s5_QuestionId_SchemeOfWorkId_AnswerValue_1",
    "TE_s5_QuestionId_SchemeOfWorkId_AnswerValue_2",
    "TE_s5_QuestionId_SchemeOfWorkId_AnswerValue_3",
    "TE_s5_QuestionId_SchemeOfWorkId_AnswerValue_4",
    "TE_s5_QuestionId_SchemeOfWorkId_IsCorrect",
    "TE_s5_QuestionId_age_years_Gender_IsCorrect",
    "TE_s5_QuestionId_age_years_Gender_PremiumPupil_IsCorrect",
    "TE_s5_QuestionId_change_subjcat_AnswerValue_4",
    "TE_s5_QuestionId_prev_question_IsCorrect",
    "TE_s5_QuestionId_pri_to_high_stu_AnswerValue_1",
    "TE_s5_QuestionId_pri_to_high_stu_AnswerValue_4",
    "TE_s5_QuestionId_pri_to_high_stu_IsCorrect",
    "TE_s5_QuestionId_quiz_answer_num_div5_AnswerValue_1",
    "TE_s5_QuestionId_quiz_answer_num_div5_AnswerValue_2",
    "TE_s5_QuestionId_quiz_answer_num_div5_AnswerValue_3",
    "TE_s5_QuestionId_quiz_answer_num_div5_AnswerValue_4",
    "TE_s5_QuestionId_quiz_answer_num_div5_IsCorrect",
    "TE_s5_QuizId_IsCorrect",
    "TE_s5_SchemeOfWorkId_GroupId_IsCorrect",
    "TE_s5_SchemeOfWorkId_IsCorrect",
    "TE_s5_SchemeOfWorkId_QuizId_IsCorrect",
    "TE_s5_SchemeOfWorkId_age_years_PremiumPupil_IsCorrect",
    "TE_s5_SchemeOfWorkId_answered_subjcat_IsCorrect",
    "TE_s5_SchemeOfWorkId_change_subjcat_IsCorrect",
    "TE_s5_SchemeOfWorkId_quiz_answer_num_div5_IsCorrect",
    "TE_s5_SubjectId_cat_SchemeOfWorkId_IsCorrect",
    "TE_s5_SubjectId_cat_quiz_answer_num_div5_AnswerValue_3",
    "TE_s5_UserId_AnswerValue_4",
    "TE_s5_UserId_Confidence_AnswerValue_1",
    "TE_s5_UserId_Confidence_AnswerValue_4",
    "TE_s5_UserId_Confidence_IsCorrect",
    "TE_s5_UserId_DateAnswered_day_AnswerValue_1",
    "TE_s5_UserId_DateAnswered_day_AnswerValue_3",
    "TE_s5_UserId_DateAnswered_day_AnswerValue_4",
    "TE_s5_UserId_DateAnswered_day_IsCorrect",
    "TE_s5_UserId_DateAnswered_hour_IsCorrect",
    "TE_s5_UserId_DateAnswered_weekday_DateAnswered_hour_AnswerValue_1",
    "TE_s5_UserId_DateAnswered_weekday_DateAnswered_hour_AnswerValue_3",
    "TE_s5_UserId_DateAnswered_weekday_DateAnswered_hour_AnswerValue_4",
    "TE_s5_UserId_DateAnswered_weekday_DateAnswered_hour_IsCorrect",
    "TE_s5_UserId_DateAnswered_weekday_DateAnswered_wom_IsCorrect",
    "TE_s5_UserId_DateAnswered_weekday_IsCorrect",
    "TE_s5_UserId_DateAnswered_wom_IsCorrect",
    "TE_s5_UserId_GroupId_AnswerValue_1",
    "TE_s5_UserId_GroupId_AnswerValue_4",
    "TE_s5_UserId_GroupId_IsCorrect",
    "TE_s5_UserId_IsCorrect",
    "TE_s5_UserId_QuizId_AnswerValue_1",
    "TE_s5_UserId_QuizId_AnswerValue_2",
    "TE_s5_UserId_QuizId_AnswerValue_3",
    "TE_s5_UserId_QuizId_AnswerValue_4",
    "TE_s5_UserId_QuizId_IsCorrect",
    "TE_s5_UserId_SchemeOfWorkId_IsCorrect",
    "TE_s5_UserId_SubjectId_cat_AnswerValue_1",
    "TE_s5_UserId_SubjectId_cat_IsCorrect",
    "TE_s5_UserId_age_years_AnswerValue_1",
    "TE_s5_UserId_age_years_Confidence_AnswerValue_1",
    "TE_s5_UserId_age_years_Confidence_AnswerValue_4",
    "TE_s5_UserId_age_years_Confidence_IsCorrect",
    "TE_s5_UserId_age_years_IsCorrect",
    "TE_s5_UserId_answer_num_div5_AnswerValue_4",
    "TE_s5_UserId_answer_num_div5_IsCorrect",
    "TE_s5_UserId_answered_subjcat_AnswerValue_3",
    "TE_s5_UserId_quiz_answer_num_div5_IsCorrect",
    "TE_s5_prev_question_IsCorrect",
    "TE_s5_subj_Confidence_agg_max_IsCorrect",
    "TE_s5_subj_Confidence_agg_min_IsCorrect",
    "TE_s5_subj_Confidence_agg_sum_IsCorrect",
    "TE_s5_subj_SchemeOfWorkId_agg_sum_IsCorrect",
    "TE_s5_subj_UserId_agg_max_IsCorrect",
    "TE_s5_subj_UserId_agg_min_IsCorrect",
    "TE_s5_subj_UserId_agg_std_IsCorrect",
    "UserId_Confidence_ce",
    "UserId_DateAnswered_day_ce",
    "UserId_DateAnswered_hour_ce",
    "UserId_DateAnswered_weekday_DateAnswered_hour_ce",
    "UserId_GroupId_ce",
    "UserId_QuizId_ce",
    "UserId_SchemeOfWorkId_ce",
    "UserId_SubjectId_cat_ce",
    "UserId_age_years_Confidence_ce",
    "quiz_answer_num",
    "quiz_answer_num_norm",
    "user_subj_svd_0",
    "user_subj_svd_1",
    "user_subj_svd_2",
    "user_subj_svd_4",
]

exp_list_t1 = [
    ('task1_lgbm', 'bbb432be523149369a5f95cdfd63578c'),  # lgb, all feature, te_smooth5
    ('task1_xgb_2', '69f2b85366b34198a1ea2dc512e05f3a'),  # xgb, all feature, te_smooth5
    ('task1_cat', 'b286e8fb8f824027869bf2ec6247b8ec'),  # cat, all feature, te_smooth5
    ('task1_lgbm_fs100', 'bf0bfd4d47664b349c02dd92eaa50fc4'),  # lgb, fs100, te_smooth5
    ('task1_xgb_fs100', '2cf16a7701da409daf40cbfe78b3b7bf'),  # xgb, fs100, te_smooth5 
    ('task1_mlp_fs100', '92598df31e9f4311adccbc8e267e7c01'),  # mlp, fs100, te_smooth5
    ('task12_multitask_mlp_fs100', '38a138a4ad5e49b999ec0eca380be5dc'),  # mlp multi, fs100, te_smooth5
    ('task1_cat_fs100', '468d28a067bc479caa65e12153965df4'),  # cat depth 8, fs100, te_smooth5
    ('task1_cat_fs100', 'e4950f4d436a4d58a89c5bd90e254428'),  # cat depth 10, fs100, te_smooth5
    ('task1_lgbm', 'c4def7cc4f3f4f44971ac474d2993e92'),  # lgb, all feature, te_smooth2
]

exp_list_t2 = [
    ('task2_lgbm', '90443d723c874103a4b1c68f2830446e'),  # lgb, all feature, te_smooth5
    ('task2_xgb_2', '19a82f5124d349ee9550b871a88025d2'),  # xgb, all feature, te_smooth5
    ('task2_lgbm_fs100', '751bb6f02e5746798740f2b90f183a92'),  # lgb, fs100, te_smooth5
    ('task2_xgb_fs100', '89909e8bf54443328830085dca5f26cc'),  # xgb, fs100, te_smooth5 
    ('task2_mlp_fs100', '2f1d7ef010874723a8dd70aa49891f5d'),  # mlp, fs100, te_smooth5
    ('task12_multitask_mlp_fs100', '38a138a4ad5e49b999ec0eca380be5dc'),  # mlp multi, fs100, te_smooth5
    ('task2_cat_fs100', '5f4c75b620ef4eccbb14581589340db6'),  # cat depth 8, fs100, te_smooth5
]

meta_pred_features = []
for ename, run_id in exp_list_t1:
    meta_pred_features.append(f't1_{ename}_{run_id}')
for ename, run_id in exp_list_t2:
    for idx in range(4):
        meta_pred_features.append(f't2_{ename}_{run_id}_{idx}')

meta_agg_t1 = [
    'preds_t1_mean_0',
    'preds_t1_std_0',
    'preds_t1_max_0',
    'preds_t1_min_0',
    'preds_t1_diff_0',
]

meta_agg_t2 = [
    'preds_t2_mean_0',
    'preds_t2_mean_1',
    'preds_t2_mean_2',
    'preds_t2_mean_3',
    'preds_t2_mean_max_0',
    'preds_t2_mean_min_0',
    'preds_t2_std_0',
    'preds_t2_std_1',
    'preds_t2_std_2',
    'preds_t2_std_3',
    'preds_t2_std_sum_0',
    'preds_t2_max_0',
    'preds_t2_max_1',
    'preds_t2_max_2',
    'preds_t2_max_3',
    'preds_t2_min_0',
    'preds_t2_min_1',
    'preds_t2_min_2',
    'preds_t2_min_3',
]

meta_mul = []
for i in range(4):
    meta_mul.append(f'preds_t1_mean_mul_t2_mean_{i}')
    meta_mul.append(f'preds_t1_std_mul_t2_std_{i}')
    meta_mul.append(f'preds_t1_std_mul_t2_mean_{i}')

################################################################
dense_features = [
    'age_days'
]
dense_features += count_encording_features
dense_features += target_encording_features
dense_features += subject_meta_features
dense_features += target_encording_ansval_features
dense_features += user_lag_num_features
dense_features += target_encording_subj_agg_features
dense_features += svd_features
dense_features = [f for f in dense_features if f in fs_features]
dense_features += meta_pred_features
dense_features += meta_agg_t1
dense_features += meta_agg_t2
dense_features += meta_mul

sparse_features = [
    # 'QuestionId',
    # 'UserId',
    'Gender',
    'PremiumPupil',
    'Confidence',
    # 'GroupId'
    # 'QuizId',
    'SchemeOfWorkId',
    'age_years',
    'SubjectId_cat',
    'DateOfBirth_NaN',
    'pri_to_high_stu',
]
sparse_features += answer_date_features
sparse_features += user_lag_cat_features
sparse_features = [f for f in sparse_features if f in fs_features]

varlen_sparse_features = [
    # 'SubjectId',
    # 'SubjectId_level'
]
# varlen_sparse_features = varlen_sparse_features + user_lag_multicat_features
################################################################