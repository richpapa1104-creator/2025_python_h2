# 根據分數給予評語
def get_grade_comment(score):
    match score:
        case n if 90 <= n <= 100:
            return "優秀！"
        case n if 80 <= n < 90:
            return "良好！"
        case n if 70 <= n < 80:
            return "普通"
        case n if 60 <= n < 70:
            return "需要加油"
        case n if 0 <= n < 60:
            return "不及格，需要重修"
        case _:
            return "無效分數"

# 測試
scores = [95, 83, 75, 65, 45, 105]
for score in scores:
    print(f"分數 {score}: {get_grade_comment(score)}")
