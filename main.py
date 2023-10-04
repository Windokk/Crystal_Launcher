import ttkbootstrap as ttk
import ctypes as ct

def dark_title_bar(window):
    """
    Sets windows title bar to dark color
    For more infos:
    https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    """
    window.update()
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, 20, ct.byref(value),4)

dark_grey = "#292929"

root = ttk.Window(themename="darkly")
root.title("Kold Launcher")
root.geometry("900x700")
root.resizable(False, False)
dark_title_bar(root)

style = ttk.Style()
style.configure('lefttab.TNotebook', tabposition='wn')
tabController = ttk.Notebook(root, style='lefttab.TNotebook')

KV = ttk.Frame(tabController, width=500, height=300)
KV_Online = ttk.Frame(tabController, width=500, height=300)
KV_Competitive = ttk.Frame(tabController, width=500, height=300)

tabController.add(KV, text='Play Kold Vendetta')
tabController.add(KV_Online, text='Play Kold Vendetta : Online Mode')
tabController.add(KV_Competitive, text='Play Kold Vendetta : Competitive')
tabController.pack(expand=1, fill="both")

root.mainloop()