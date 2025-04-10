import pandas as pd
import matplotlib.pyplot as plt

def create_frame():
    """
    创建一个包含学生信息的DataFrame并保存为CSV文件。
    """
    data = {
        '姓名': ['张三', '李四', '王五', '赵六', '陈七'],
        '年龄': [25, 30, None, 22, 28],
        '成绩': [85.5, 90.0, 78.5, 88.0, 92.0],
        '城市': ['北京', '上海', '广州', '深圳', '上海']
    }
    df = pd.DataFrame(data)
    df.to_csv('data/data.csv', index=False, encoding='utf-8')

def load_data():
    """任务1: 读取数据文件"""
    try:
        df = pd.read_csv('data/data.csv', encoding='utf-8')
        print("数据读取成功！")
        return df
    except FileNotFoundError:
        print("文件未找到，请先运行create_frame()创建数据文件")
        return None

def show_basic_info(data):
    """任务2: 显示数据基本信息"""
    print("\n=== 数据基本信息 ===")
    print(f"数据形状（行,列）: {data.shape}")
    print("\n前5行数据:")
    print(data.head())
    print("\n数据信息:")
    print(data.info())
    print("\n描述性统计:")
    print(data.describe(include='all'))

def handle_missing_values(data):
    """任务3: 处理缺失值"""
    print("\n=== 处理缺失值前 ===")
    print("缺失值统计:")
    print(data.isnull().sum())
    
    # 使用年龄列的中位数填充缺失值
    median_age = data['年龄'].median()
    data['年龄'].fillna(median_age, inplace=True)
    
    print("\n=== 处理缺失值后 ===")
    print("缺失值统计:")
    print(data.isnull().sum())
    return data

def analyze_statistics(data):
    """任务4: 统计分析数值列"""
    print("\n=== 数值列统计分析 ===")
    numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns
    for col in numeric_cols:
        print(f"\n列名: {col}")
        print(f"均值: {data[col].mean():.2f}")
        print(f"中位数: {data[col].median():.2f}")
        print(f"标准差: {data[col].std():.2f}")
    return data

def visualize_data(data, column_name='成绩'):
    """任务6: 数据可视化"""
    plt.figure(figsize=(8, 5))
    data[column_name].plot(kind='hist', bins=5, edgecolor='black')
    plt.title(f'{column_name}分布直方图')
    plt.xlabel(column_name)
    plt.ylabel('频数')
    plt.grid(True)
    plt.savefig('data/score_distribution.png')
    plt.show()

def save_processed_data(data):
    """任务7: 保存处理后的数据"""
    data.to_csv('data/processed_data.csv', index=False, encoding='utf-8')
    print("\n处理后的数据已保存为 data/processed_data.csv")

def main():
    """主函数，执行所有数据处理流程"""
    # 生成data.csv文件
    create_frame()
    
    # 任务1: 读取数据
    df = load_data()
    if df is None:
        return
    
    # 任务2: 显示基本信息
    show_basic_info(df)
    
    # 任务3: 处理缺失值
    df = handle_missing_values(df)
    
    # 任务4: 统计分析
    df = analyze_statistics(df)
    
    # 任务5: 数据可视化
    visualize_data(df)
    
    # 任务6: 保存处理后的数据
    save_processed_data(df)

if __name__ == "__main__":
    creat_frame = create_frame
    main()
