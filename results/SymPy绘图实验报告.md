# SymPy 绘图实验报告

## 一、实验信息

- 小组名称：李欣欣
- 成员：李欣欣
- 实验日期：4.10

---

## 二、实验目的

- 熟悉SymPy的plot、plot_implicit、和plot3d_parametric_surface函数；
- 掌握曲线、隐函数和参数曲面的绘制方法。

---

## 三、实验内容与方法

分别说明三个问题的具体绘图方法和使用的函数接口。
问题1: 使用 sympy.plot() 绘制显式函数曲线。首先定义符号变量x和表达式，然后调用plot函数指定绘图区间和标签。

问题2: 使用 sympy.plot_implicit() 绘制隐函数曲线。需要避开x=0的奇点，设置足够采样点保证曲线平滑。

问题3: 使用 plot3d_parametric_surface() 绘制三维参数曲面。定义三个参数方程并指定参数范围。
---

## 四、实验结果与分析

### 问题1: 函数曲线 $\cos(\tan(\pi x))$ 绘制结果

![image](https://github.com/user-attachments/assets/a8e68414-3ed1-442f-a8ce-f1d518e40f58)

曲线在x接近±0.5时出现剧烈震荡，因为tan(πx)在这些点趋向于无穷大

在x=0处函数值为cos(0)=1

整体呈现对称的震荡衰减模式
### 问题2: 隐函数曲线 $e^y + \frac{\cos x}{x} + y = 0$ 绘制结果

![image](https://github.com/user-attachments/assets/d94b6e06-401a-490a-bd48-4facac501762)

曲线在x<0区域有多条分支

当x接近0时曲线趋向于无穷

曲线呈现周期性变化，与cos(x)的周期性相关
### 问题3: 参数曲面绘制结果

![image](https://github.com/user-attachments/assets/22213219-595a-44da-9039-8161f0c719c4)

曲面呈螺旋下降形状

z值随t线性增长

x,y分量随s增大呈指数衰减

整体形成类似锥形螺旋的结构
---

## 五、实验总结与讨论

- 通过本实验你掌握了哪些绘图技巧？
- 实验中你遇到了哪些问题？如何解决？
- 你对SymPy的绘图功能有什么建议或意见？
隐函数绘图时遇到x=0处的奇点，通过调整区间避开

三维曲面参数范围设置需要多次尝试才能获得最佳效果

通过增加采样点解决了隐函数曲线不平滑的问题
---

## 六、参考文献

- SymPy官方文档：https://docs.sympy.org/latest/modules/plotting.html
