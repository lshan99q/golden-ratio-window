import sys
import math
import pygetwindow as gw
import pyautogui

def calculate_golden_ratio_size(window):
    """根据黄金分割比例调整窗口尺寸"""
    golden_ratio = (1 + math.sqrt(5)) / 2  # 约1.618
    
    # 获取窗口当前尺寸
    current_width, current_height = window.size
    
    # 保持高度不变，按黄金比例调整宽度
    new_width = int(current_height * golden_ratio)
    
    # 计算新位置以保持窗口中心不变
    x = window.left + (current_width - new_width) // 2
    y = window.top
    
    return x, y, new_width, current_height

def get_screen_recommendation():
    """获取基于屏幕分辨率的推荐窗口尺寸"""
    screen_width, screen_height = pyautogui.size()
    golden_ratio = (1 + math.sqrt(5)) / 2
    
    # 推荐1: 黄金比例窗口(总面积占屏幕80%)
    area = screen_width * screen_height * 0.8
    rec1_h = int(math.sqrt(area / golden_ratio))
    rec1_w = int(rec1_h * golden_ratio)
    
    # 推荐2: 16:9比例窗口(高度为屏幕80%)
    rec2_h = int(screen_height * 0.8)
    rec2_w = int(rec2_h * 16/9)
    
    return [
        ("黄金比例", rec1_w, rec1_h),
        ("16:9宽屏", rec2_w, rec2_h)
    ]

def main():
    try:
        while True:
            print("\n窗口比例调整工具")
            print("1. 调整窗口比例")
            print("2. 查看推荐窗口尺寸") 
            print("3. 调整至黄金分割推荐大小")
            print("4. 退出")
            
            choice = input("请选择操作: ")
            
            if choice == "1":
                print("请从列表中选择要调整的窗口...")
                windows = gw.getAllWindows()
                if not windows:
                    print("没有找到可用窗口")
                    continue
                    
                print("\n可用窗口列表:")
                for i, window in enumerate(windows):
                    print(f"{i+1}. {window.title}")
                    
                try:
                    window_choice = int(input("请输入要选择的窗口编号: "))
                    if 1 <= window_choice <= len(windows):
                        target_window = windows[window_choice-1]
                        # 计算并调整窗口尺寸和位置
                        x, y, new_width, height = calculate_golden_ratio_size(target_window)
                        target_window.resizeTo(new_width, height)
                        target_window.moveTo(x, y)
                        print(f"已将窗口调整为黄金分割比例: {new_width}x{height} (位置: {x},{y})")
                    else:
                        print("无效的选择")
                except ValueError:
                    print("请输入有效的数字")
                    
            elif choice == "2":
                recommendations = get_screen_recommendation()
                print("\n基于当前屏幕的推荐窗口尺寸:")
                print("1. 黄金比例 (总面积80%)")
                print("2. 16:9宽屏 (高度80%)")
                for name, width, height in recommendations:
                    print(f"{name}: {width}x{height}")
                    
            elif choice == "3":
                print("请从列表中选择要调整的窗口...")
                windows = gw.getAllWindows()
                if not windows:
                    print("没有找到可用窗口")
                    continue
                    
                print("\n可用窗口列表:")
                for i, window in enumerate(windows):
                    print(f"{i+1}. {window.title}")
                    
                try:
                    window_choice = int(input("请输入要选择的窗口编号: "))
                    if 1 <= window_choice <= len(windows):
                        target_window = windows[window_choice-1]
                        # 获取推荐尺寸
                        rec_name, rec_width, rec_height = get_screen_recommendation()[0]
                        # 计算新位置以保持窗口中心
                        x = target_window.left + (target_window.width - rec_width) // 2
                        y = target_window.top + (target_window.height - rec_height) // 2
                        # 调整窗口
                        target_window.resizeTo(rec_width, rec_height)
                        target_window.moveTo(x, y)
                        print(f"已将窗口调整为{rec_name}推荐大小(总面积80%): {rec_width}x{rec_height} (位置: {x},{y})")
                    else:
                        print("无效的选择")
                except ValueError:
                    print("请输入有效的数字")
                    
            elif choice == "4":
                print("退出程序")
                break
            else:
                print("无效的选择，请输入1-4")
                
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    main()
