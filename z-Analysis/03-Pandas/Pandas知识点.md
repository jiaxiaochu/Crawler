## pandas 的数据结构
- Series 一维的数据结构
- DataFrame 二维的数据结构
- Panel 三维的数据结构


## DataFrame的创建
- pd.DataFrame(array/list,index=[],columns=[])
  - index 是行索引
  - columns 列索引
- 传入列表，包含字典的列表
  - pd.DataFrame([{},{},{}])
- 传入字典
  - pd.DataFrame（{name:[],age:[],"":[]}

## DataFrame的索引
- df.index = []  #设置新索引
- df.reset_index() #删除索引，把索引作为新的一列数据
- df.reset_inde(drop=True) #删除索引
- df.set_inde("") #把某一列或者几列置为索引

## Series的属性和方法和创建
- 创建
  - pd.Series(array/[]/{"":"","":""})
- 属性
  - s1.index
  - s1.values
  - s1.shape
  - s1.ndim
  - s1.dtype
- 方法
  - s1.head()
  - s1.tail()

### pandas 取值的方法
- 直接取值
  - df[columns_1] #取一列
  - df[[columns_1,columns_2]] #取多列
- loc #根据索引的标签来取值
  - df.loc["",""]
- iloc #根据索引的位置来取值
  - df.iloc[int,int]
- ix #使用混合索引的方式来取值
  - df.ix[int/str,int/str]
## pandas中排序
默认按照升序的方式排序，ascending=False降序
- df.sort_values(by="") #按照某一列进行排序
- df.sort_index() #把索引进行排序

## pandas计算
- 逻辑计算
  - df["A"]>10 -->返回一个series，值是bool
  - df[df["A"]>10] -- >选择行，A列中值大于10的行
  - df[(df["A"]>10)&(df["A"]<20)] #选择a列中大>10,<20所有的行

- apply能够对dataframe中的每一列进行自定义的计算
