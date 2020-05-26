## numpy的基础属性
-  t1.shape #获取形状
- t1.size #获取个数
- t1.ndim #获取维数
- t1.dtype #获取数组中数据的类型

## numpy的基础方法
- t1.array([]) #创建数组
- t1.astype(np.float) #调整数组中数据的类型
- 创建全为1的数组：np.ones(shape)
- 创建全为0的数组：np.zeros(shape)
- np.asarray(array) #能够得到数组，指向之前的array
- np.copy(array) #重新创建一个数组，相互不影响
- np.arange(0,100,10)  #创建从0到100，步长为10的数组
- np.random.randint(10) #创建从0-10的随机整数
- np.randpm.normal(2,0.1,(3,4)) #创建23行4列的均值为2，标准差为0.1的服从正态分布的随机数组

## 正态分布
- 均值：描述的是数据的平均位置
- 标准差：描述的是数据的离散程度，数据之间的距离（变化)越大，标准差越大

## bool索引
- t1==10,t2<=20 #返回一个包含bool类型的数组
- t1[t1=100] #返回bool类型的数组中为True的位置的值

## 三元运算符
- np.where(t1>10,100,0) #把t1中大与10的替换为100，小于等于10的替换为0

## 逻辑与和逻辑或
- 包含bool类型的数组
- np.logical_and(条件1，条件2)
- np.logical_or(条件2，条件2)

## numpy中的常用统计方法
- np.max() #获取最大值
- np.min()
- np.mean()
- np.median()
- np.std()
- np.argmax(t1,axis=) #获取最大值的位置
- np.argmin(t1,axis) #获取最小值的位置

## 举证的运算
- np.matmul(a,b) #能够进行矩阵的运算
- a(m,n)* b(n,l) = ret(m,l)

## 数组的拼接
- np.concatenate([a,b],axis=1) #左右拼接  = np.hstack()
- np.concatenate([a,b],axis=0) #上下拼接  = np.vstack()

## np.nan的知识点
- 属性
  - np.nan 是float类型
  - np.nan !=np.nan

- nan出现的原因
  - 数据有缺失的时候
  - 数据进行不合适的类型转换
  