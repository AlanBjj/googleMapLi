import pyperclip
import time

def main():
    last_clipboard_content = ""
    file_path = "/Users/mac/code_stduy/googleMapLI/li.txt"  # 指定要粘贴内容的文件路径

    while True:
        time.sleep(0.1)  # 每0.1秒检查一次剪切板内容
        clipboard_content = pyperclip.paste()
        if clipboard_content != last_clipboard_content:
            with open(file_path, "a") as file:
                file.write(clipboard_content + "\n")
            print(f"新的剪切板内容已保存: {clipboard_content}")
            last_clipboard_content = clipboard_content

if __name__ == "__main__":
    main()
