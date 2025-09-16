import subprocess
import os
import shutil
import glob


def copy_to_usr_local_bin():
    source_dir = 'bin'
    target_dir = '/usr/local/bin'
    try:
        for file_path in glob.glob(os.path.join(source_dir, '*')):
            if os.path.isfile(file_path):
                file_name = os.path.basename(file_path)
                dest_path = os.path.join(target_dir, file_name)
                
                # Копируем файл
                shutil.copy2(file_path, dest_path)
                
                # Делаем файл исполняемым
                os.chmod(dest_path, 0o755)  # rwxr-xr-x
                print(f"Скопирован и сделан исполняемым: {file_name} -> {dest_path}")
        
        return True
    except Exception as e:
        print(f"Ошибка: {e}")
        return False


def copy_configs_content_to_home():
    source_dir = 'configs'
    home_dir = os.path.expanduser('~')
    
    try:
        for item in os.listdir(source_dir):
            source_path = os.path.join(source_dir, item)
            dest_path = os.path.join(home_dir, item)
            
            if os.path.isdir(source_path):
                shutil.copytree(source_path, dest_path)
            else:
                shutil.copy2(source_path, dest_path)
                
        print("Содержимое папки configs успешно скопировано в домашнюю директорию")
    except Exception as e:
        print(f"Ошибка при копировании: {e}")

def install_packages_pacman(file_path="packages.txt"):
    try:
        if not os.path.exists(file_path):
            print(f"Ошибка: Файл {file_path} не найден")
            return False
        
        with open(file_path, 'r') as file:
            packages = [pkg.strip() for pkg in file.readlines() if pkg.strip()]
        
        if not packages:
            print("Файл не содержит пакетов для установки")
            return False
        
        print(f"Найдено {len(packages)} пакетов для установки")
        
        installed = 0
        for pkg in packages:
            print(f"\nУстановка пакета: {pkg}")
            try:
                result = subprocess.run(
                    ['sudo', 'pacman', '-S', '--noconfirm', pkg],
                    check=True,
                    text=True
                )
                installed += 1
                print(f"✓ {pkg} установлен")
            except subprocess.CalledProcessError:
                print(f"✗ Ошибка при установке {pkg}")
                continue
        
        print(f"\nУстановлено {installed} из {len(packages)} пакетов")
        return installed > 0
        
    except Exception as e:
        print(f"Ошибка: {e}")
        return False

def install_paru():
    subprocess.run("git clone https://aur.archlinux.org/paru.git")
    subprocess.run("cd paru")
    subprocess.run("makepkg -si")
    print("Paru установлен!")

def install_aur_packages(file_path="aur_packages.txt"):
     try:
        if not os.path.exists(file_path):
            print(f"Ошибка: Файл {file_path} не найден")
            return False
        
        with open(file_path, 'r') as file:
            packages = [pkg.strip() for pkg in file.readlines() if pkg.strip()]
        
        if not packages:
            print("Файл не содержит пакетов для установки")
            return False
        
        print(f"Найдено {len(packages)} пакетов для установки")
        
        installed = 0
        for pkg in packages:
            print(f"\nУстановка пакета: {pkg}.")
            try:
                result = subprocess.run(
                    ['paru', '-S', '--noconfirm', pkg],
                    check=True,
                    text=True
                )
                installed += 1
                print(f"✓ {pkg} установлен")
            except subprocess.CalledProcessError:
                print(f"✗ Ошибка при установке {pkg}")
                continue
        
        print(f"\nУстановлено {installed} из {len(packages)} пакетов")
        return installed > 0
        
    except Exception as e:
        print(f"Ошибка: {e}")
        return False

def main():
    if os.getuid() != 0:
        print("Скрипту требуются права суперпользователя!")
        return False
    else:
        copy_configs_content_to_home()
        install_packages_pacman("packages.txt")
        install_paru()
        install_aur_packages("aur_packages.txt")
        copy_bin()

if __name__ == "__main__":
    main()
