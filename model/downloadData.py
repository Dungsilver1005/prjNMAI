import kagglehub
import os
import shutil

def setup_dataset():
    # 1. Tải dữ liệu từ Kaggle
    print("🚀 Đang tải dữ liệu từ Kaggle (FER2013)...")
    try:
        download_path = kagglehub.dataset_download("msambare/fer2013")
    except Exception as e:
        print(f"❌ Lỗi khi tải dữ liệu: {e}")
        return

    # 2. XÁC ĐỊNH ĐÍCH ĐẾN
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_dataset_dir = os.path.join(current_dir, "dataset")
    
    if not os.path.exists(target_dataset_dir):
        os.makedirs(target_dataset_dir)
        print(f"📁 Đã tạo thư mục mới: {target_dataset_dir}")

    # 3. DI CHUYỂN DỮ LIỆU
    items = os.listdir(download_path)
    for item in items:
        source_item = os.path.join(download_path, item)
        destination_item = os.path.join(target_dataset_dir, item)

        if os.path.exists(destination_item):
            if os.path.isdir(destination_item):
                shutil.rmtree(destination_item)
            else:
                os.remove(destination_item)

        try:
            shutil.move(source_item, destination_item)
            print(f"✔️ Đã chuyển: {item}")
        except Exception as e:
            print(f"⚠️ Không thể chuyển {item}: {e}")

    print("\n✨ Hoàn tất! Check folder 'dataset' nhé.")

if __name__ == "__main__":
    setup_dataset()