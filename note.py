#字符串

str.replace(old, new[, max])     
#把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

str.join([])    
#[]为序列，序列中元素必须都是字符串

string.split(str='',num)   
#通过指定分隔符str对字符串string进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串

str.isalpha()    
#检测字符串是否只由字母组成。

str.rjust(width, fillchar)
#返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。fillchar -- 填充的字符，默认为空格。

sorted(iterable, key=lambda x:x^2, reverse=False) 
#对所有可迭代的对象进行排序操作。key——具体的函数的参数。reverse——True 降序，False 升序（默认）


#列表

#偶数列、奇数列简单可得：
even_list = ls[::2]
odd_list = ls[1::2]

list.insert(index,object)
#在指定位置index插入指定对象object

list.index(obj)
#返回指定目标obj在list中的索引值


#break    #打破最小封闭for或while循环

#进制转换
#int转换为二/十六进制时会产生0b/0x，常用格式(只读取数值部分)：
bin()[2:]
hex()[2:]

##输入的数据可能不足n行

#栈：后进先出
stack.append()
stack.pop()

#队列：先进先出
queue.append()
queue.pop(0)

#BFS广度优先：
使用队列，逐层处理
找最短路径

#DFS深度优先
栈/递归
处理回溯问题