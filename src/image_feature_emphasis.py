import numpy as np
import scipy.ndimage as sim
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def load_stress_fibers():
    """加载应力纤维数据"""
    try:
        data = np.loadtxt('data/stressFibers.txt')
        print("应力纤维数据加载成功，尺寸:", data.shape)
        return data
    except Exception as e:
        print(f"加载数据失败: {str(e)}")
        # 创建模拟数据
        x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
        data = np.sin(x**2 + y**2)  # 模拟应力纤维图案
        return data


def create_gauss_filter(sigma_x=5, sigma_y=45, size=50):
    """创建高斯滤波器
    
    参数:
        sigma_x: X方向方差参数
        sigma_y: Y方向方差参数
        size: 滤波器尺寸（奇数）
    
    返回:
        numpy.ndarray: size×size的高斯滤波器
    """
    if size % 2 == 0:
        size += 1  # 确保尺寸为奇数
    v = np.arange(-size//2, size//2 + 1)
    X, Y = np.meshgrid(v, v)
    return np.exp(-0.5*(X**2/sigma_x + Y**2/sigma_y))

def create_combined_filter(gauss_filter):
    """创建高斯-拉普拉斯组合滤波器
    
    参数:
        gauss_filter: 高斯滤波器
    
    返回:
        numpy.ndarray: 与输入相同尺寸的组合滤波器
    """
    laplace_filter = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    # 使用'same'模式保持输出尺寸不变
    return sim.convolve(gauss_filter, laplace_filter, mode='constant', output=np.float64)


def plot_filter_surface(filter, title):
    """绘制滤波器3D表面图"""
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(np.arange(filter.shape[1]), np.arange(filter.shape[0]))  # 修复了这里的括号
    ax.plot_surface(X, Y, filter, cmap='viridis')
    ax.set_title(title, fontsize=14)
    plt.show()

def process_and_display(image, filter, vmax_ratio=0.5, title=None):
    """处理图像并显示结果"""
    result = sim.convolve(image, filter, mode='reflect')
    
    plt.figure(figsize=(8, 6))
    plt.imshow(result, vmin=0, vmax=vmax_ratio*result.max(), cmap='gray')
    plt.colorbar(label='Intensity')
    if title:
        plt.title(title)
    plt.show()
    return result

def main():
    # 1. 加载数据
    stressFibers = load_stress_fibers()
    plt.imshow(stressFibers, cmap='gray')
    plt.title('Original Stress Fibers')
    plt.colorbar()
    plt.show()
    
    # 2. 创建并显示高斯滤波器
    gauss_filter = create_gauss_filter()
    plt.imshow(gauss_filter, cmap='hot')
    plt.title('Gaussian Filter (σ_x=√5, σ_y=√45)')
    plt.colorbar()
    plt.show()
    plot_filter_surface(gauss_filter, 'Gaussian Filter 3D Surface')
    
    # 3. 创建并显示组合滤波器
    combined_filter = create_combined_filter(gauss_filter)
    plt.imshow(combined_filter, cmap='coolwarm', origin='lower')
    plt.title('Combined Gauss-Laplace Filter')
    plt.colorbar()
    plt.show()
    plot_filter_surface(combined_filter, 'Combined Filter 3D Surface')
    
    # 4. 应用垂直滤波器
    vertical_result = process_and_display(
        stressFibers, combined_filter, 0.5,
        'Vertical Features Enhancement'
    )
    
    # 5. 应用水平滤波器
    combined_filter_horizontal = sim.rotate(combined_filter, angle=90)
    horizontal_result = process_and_display(
        stressFibers, combined_filter_horizontal, 0.4,
        'Horizontal Features Enhancement'
    )
    
    # 6. 45度方向滤波器
    combined_filter_45deg = sim.rotate(combined_filter, angle=45)
    result_45deg = process_and_display(
        stressFibers, combined_filter_45deg, 0.3,
        '45° Features Enhancement'
    )
    
    # 7. -45度方向滤波器
    combined_filter_neg45deg = sim.rotate(combined_filter, angle=-45)
    result_neg45deg = process_and_display(
        stressFibers, combined_filter_neg45deg, 0.3,
        '-45° Features Enhancement'
    )

if __name__ == "__main__":
    main()
