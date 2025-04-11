import numpy as np
import matplotlib.pyplot as plt

# 物理常数
k = 8.99e9  # 库仑常数 (N·m²/C²)
q_pos = 1e-9  # 正点电荷量 (C)
q_neg = -1e-9  # 负点电荷量 (C)

# 电荷位置 [x, y] 坐标 (m)
pos_charge_pos = np.array([0.05, 0])  # 正电荷位置
neg_charge_pos = np.array([-0.05, 0])  # 负电荷位置

def calculate_potential(X, Y):
    """
    计算二维空间电势分布
    
    参数:
        X, Y: 二维网格坐标矩阵 (numpy.ndarray)
        
    返回:
        V: 电势值矩阵 (numpy.ndarray)
    """
    # 计算每个点到正电荷的距离
    r_pos = np.sqrt((X - pos_charge_pos[0])**2 + (Y - pos_charge_pos[1])**2)
    # 计算每个点到负电荷的距离
    r_neg = np.sqrt((X - neg_charge_pos[0])**2 + (Y - neg_charge_pos[1])**2)
    
    # 计算电势 (叠加原理)
    V = k * (q_pos / r_pos + q_neg / r_neg)
    return V

def calculate_electric_field(V, spacing):
    """
    通过电势梯度计算电场强度
    
    参数:
        V: 电势值矩阵 (numpy.ndarray)
        spacing: 网格间距 (float)
        
    返回:
        Ex, Ey: 电场在x和y方向的分量 (numpy.ndarray, numpy.ndarray)
    """
    Ey, Ex = np.gradient(-V, spacing)  # 注意负号和顺序(y,x)
    return Ex, Ey

def main():
    """
    主函数: 计算并可视化电势和电场
    """
    # 创建计算网格
    x = np.linspace(-0.2, 0.2, 100)
    y = np.linspace(-0.2, 0.2, 100)
    X, Y = np.meshgrid(x, y)
    spacing = x[1] - x[0]  # 网格间距

    # 计算电势和电场
    V = calculate_potential(X, Y)
    Ex, Ey = calculate_electric_field(V, spacing)

    # 可视化
    plt.figure(figsize=(10, 8))
    
    # 绘制电势等高线
    levels = np.linspace(-800, 800, 20)
    contour = plt.contourf(X, Y, V, levels=levels, cmap='RdYlBu')
    plt.colorbar(contour, label='Electric Potential (V)')
    
    # 绘制电场线
    plt.streamplot(X, Y, Ex, Ey, color='black', density=1.5, linewidth=1, arrowsize=1)
    
    # 标记电荷位置
    plt.scatter(*pos_charge_pos, c='red', s=100, label='Positive Charge')
    plt.scatter(*neg_charge_pos, c='blue', s=100, label='Negative Charge')
    
    # 添加标签和标题
    plt.title('Electric Dipole: Potential and Field Lines')
    plt.xlabel('x position (m)')
    plt.ylabel('y position (m)')
    plt.legend()
    plt.grid(True)
    
    # 保存图像
    plt.savefig('dipole_field.png', dpi=300, bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    main()
