from time import sleep
# Install tdgm_gui from tqdm instead of just tqdm
from tqdm import tqdm_gui
list1 = ["My","Name","Is","Ashwini","Mandani"]
# Use tqdm_gui
list1 = [(sleep(2), print(i)) for i in tqdm_gui(list1)]