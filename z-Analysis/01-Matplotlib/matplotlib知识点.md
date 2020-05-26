## jupyter notebook的使用
- 安装：pip install jupyter
- 启动：jupyter notebook
- 常用操作命令：
	- 通用的命令：shift+enter 执行代码，跳转到下一行
	- 命令模式下的命令：esc进入命令模式
		- b：在当前的下一行插入单元
		- a: 在当前的上一行插入单元
		- dd: 删除当前的单元
		- m: 切换到marketdown模式
- 编辑模式下的命令：enter进入编辑模式
	- 代码后面加上";"，屏蔽当前行的输出

## matplotlib绘制折线图的基础方法
- 开启notebook对matplotlib的支持：%matplotlib inline
	- 代码后面加上";"，屏蔽当前行的输出
- 导入模块：
	`from matplotlib import pyplot as plt`
	`import matplotlib.pyplot as plt`
- 设置图形大小：plt.figure(figsize,dpi)
	- figsize 图形的宽高
	- dpi:分辨率
- 绘制折线图：plt.figure(x,y)
	- x:需要绘制的点的x值的列表，或者是可迭代对象
	- y:需要绘制的点的y值的列表
- 展示图形：plt.show()
- 保存图形：plt.savefig("")
	- 保存图形必须在展示图形之前

## 设置x轴y轴的刻度
- 刻度设置：
	- plt.xticks(x_ticks,x_tick_label,color='',linstyle='_.')
		- x_ticks :
		传入一个包含数字的列表，能够在x上展示你对应别的数字
		- x_ticks,x_tick_label: xtick	
	label: 包含字符串的列表，能够在x轴展示对应位置的字符串
- 设置x轴,y轴的label
	- plt.xlabel()
	- plt.ylabel()
- 设置图形的标题
	- plt.title()
- 设置图例
	- 首选在调用绘图方法的时候，添加label参数
	- plt.legend(loc='')
- 设置网格
	- plt.grid(aplha.linestyle)
	- alpha 控制透明度
	- linestyle 网格线条的样式
- 设置折线图的线条颜色
	- 添加color参数
- 设置折线图的样式
	- 添加linestyle参数来完成


## matplotlib 绘制子图
- api:
	- fig,axes = matplotlib.pyplot.subplots(nrows,ncols,figsize,dpi)
		- axes 数组 axes[行][列]
		- axes[0][0].plot(x,y)
		- axes[0][1].set_title() # 设置标题
		- axes[1][0].set_xlable() # 设置x轴label
		- axes[1][1].set_xticks() # 设置y轴的刻度
		- axes[1][2].legend(loc='')

## matplotlib 绘制柱状图
- api:
	- plt.bar(x,y,width,label,color) # 绘制竖着的条形图
	- plt.barh(x,y,height,label,color) # 绘制横着的条形图
	