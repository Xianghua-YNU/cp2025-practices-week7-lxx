import numpy as np
import scipy.ndimage as sim
import matplotlib.pyplot as plt
import os
from scipy import misc

def create_test_image():
    """创建测试图像"""
    os.makedirs('data', exist_ok=True)
    test_image = np.random.rand(100, 100)  # 创建100x100随机图像
    plt.imsave('data/test_image.tif', test_image, cmap='gray')

def create_small_filter():
    """创建3×3平均滤波器"""
    return np.ones((3, 3)) / 9

def create_large_filter():
    """创建15×15平均滤波器"""
    return np.ones((15, 15)) / (15*15)

def process_image(input_file='data/test_image.tif'):
    """处理图像并显示结果
    
    Args:
        input_file (str): 图像文件路径，默认为测试图像
    """
    # 检查文件是否存在
    if not os.path.exists(input_file):
        print(f"警告：文件 {input_file} 不存在，将创建测试图像")
        create_test_image()
    
    try:
        img = plt.imread(input_file)
        
        # 创建滤波器
        small_filter = create_small_filter()
        large_filter = create_large_filter()
        
        # 应用卷积
        small_result = sim.convolve(img, small_filter, mode='reflect')
        large_result = sim.convolve(img, large_filter, mode='reflect')
        
        # 显示结果
        plt.figure(figsize=(15, 5))
        
        plt.subplot(1, 3, 1)
        plt.imshow(img, cmap='gray')
        plt.title('Original Image')
        
        plt.subplot(1, 3, 2)
        plt.imshow(small_result, cmap='gray')
        plt.title('3×3 Filter Result')
        
        plt.subplot(1, 3, 3)
        plt.imshow(large_result, cmap='gray')
        plt.title('15×15 Filter Result')
        
        plt.tight_layout()
        plt.show()
        
        return True
    except Exception as e:
        print(f"图像处理失败: {str(e)}")
        return False

if __name__ == "__main__":
    # 主程序入口
    process_image('data/bwCat.tif')  # 优先尝试处理真实图像
    process_image()  # 使用默认测试图像
