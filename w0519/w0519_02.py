import pandas as pd

# 2차원 데이터 : DataFrame - 여러개의 column, 여러개의 indext 구성
# 데이터 구성 : 딕셔너리에 리스트 타입으로 구성

data = {
   '이름' : ['강나래', '강태원', '강호림', '김수찬', '김재욱', '박동현', '박혜정', '승근열'],
   '학교' : ['구로고', '구로고', '구로고', '구로고', '구로고', '디지털고', '디지털고', '디지털고'],
   '키' : [197, 184, 168, 187, 188, 202, 188, 190],
   '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
   '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
   '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
   '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
   '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
   'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}
# data 형태를 DataFrame 형태로 변경
df = pd.DataFrame(data)
# describe() : 데이터에서 숫자타입(int, float)으로 구성된 컬럼의 기본적인 통계를 보여줌
df.describe()
print(df.describe())        # 통계 출력
print(df['키'].mean())      # '키' 컬럼의 평균 출력
print(df['키'].sum())       # '키' 컬럼의 합계 출력

# info() : 데이터 유형을 보여줌
print(df.info())

# values : 데이터를 리스트 타입으로 변경해서 보여줌
print(df.values)

# index : 지정된 index를 보여줌
print(df.index)

# 지정된 컬럼을 보여줌
print(df.columns)

# index 지정
df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])
# df = pd.DataFrame(data)
# df.index = ['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번']     # 생성 후 index 변경
# index 이름 지정
df.index.name = '지원번호'
print(df)

## index 삭제 : reset_index() - index 정보가 column으로 변경
# drop 옵션 : index를 모두 삭제
# inplace 옵션 : index가 삭제된 것을 반영
print(df.reset_index())
print(df.reset_index(drop=True, inplace=True))
print(df)


# 1차원 데이터 : Series - 1개의 column, 여러개의 index 구성
# 리스트 타입
# temp = pd.Series([-20, -10, 0, 10, 20], index=['1월', '2월', '3월', '4월', '5월'])
# print(temp['1월'])    # index로 검색 가능
# print(temp)
# print(temp.sum())