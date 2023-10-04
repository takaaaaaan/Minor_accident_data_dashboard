import pandas as pd

# CSVファイルの読み込み
file_path = 'G:/내 드라이브/몰입형_12분반/0921_chart_dshi/data/2020사고 발생 데이터.csv'
df = pd.read_csv(file_path, encoding='utf-8')  # encodingの指定が必要な場合は調整してください

# '사고장소'の項目だけを取り出す
accident_locations = df['지역']

# 同じ項目が何個あったかカウントする
location_counts = accident_locations.value_counts()

# ランキングを追加
location_counts = location_counts.reset_index()
location_counts.columns = ['지역', '出現回数']
location_counts['ランキング'] = location_counts['出現回数'].rank(
    method='min', ascending=False).astype(int)

# 結果を表示
print("各項目の出現回数とランキング:")
print(location_counts)
# import pandas as pd
# import json

# # CSVファイルの読み込み
# file_path = 'G:/내 드라이브/몰입형_12분반/0921_chart_dshi/data/2020사고 발생 데이터.csv'
# df = pd.read_csv(file_path, encoding='utf-8')

# # 結果を保存するための辞書
# result_dict = {}

# # "구분"と"학교명"カラムを除外
# columns_to_analyze = [col for col in df.columns if col not in ["구분", "학교명"]]

# for column in columns_to_analyze:
#     column_data = df[column]

#     # '사고발생시간'の場合、分を除外して時間だけを使う
#     if column == '사고발생시간':
#         column_data = column_data.str.split(':').str[0]
#         column_data = column_data[column_data.apply(
#             lambda x: x not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])]

#     # 出現回数をカウント
#     value_counts = column_data.value_counts()

#     # ランキングを追加
#     value_counts = value_counts.reset_index()
#     value_counts.columns = [column, '出現回数']
#     value_counts['ランキング'] = value_counts['出現回数'].rank(
#         method='min', ascending=False).astype(int)

#     # 結果を辞書に保存
#     result_dict[column] = value_counts.to_dict(orient='records')

# # JSONに保存
# with open('column_value_counts_and_rankings.json', 'w', encoding='utf-8') as f:
#     json.dump(result_dict, f, ensure_ascii=False, indent=4)
