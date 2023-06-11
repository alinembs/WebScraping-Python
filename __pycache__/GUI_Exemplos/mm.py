import PySimpleGUI as sg
import random
sg.theme("LightBlue")

def bubble_count(a_list):
    """    
  Sorts a_list in ascending order, returns number of comparisons and exchanges    
  """
    no_of_comparisons = 0
    no_of_exchanges = 0    
    for pass_num in range(len(a_list) - 1):        
        for index in range(len(a_list) - 1 - pass_num):
            no_of_comparisons += 1
            print(a_list)
            yield no_of_comparisons            
            if a_list[index] > a_list[index + 1]:
                no_of_exchanges += 1
                temp = a_list[index]                
                a_list[index] = a_list[index + 1]                
                a_list[index + 1] = temp
    
    return (no_of_comparisons, no_of_exchanges)

def generate_random_number_list(list_length):
    """Generate a list of random numbers, given a desired length"""
    random_int_list = []
    for i in range(0, list_length):
        random_number = random.randint(1, 10000)
        random_int_list.append(random_number)
    return random_int_list


layout=[[sg.Text("Enter size of list to sort",font='Lucida, 20'), sg.Input(key='-LIST_LENGTH-', font='Lucida, 20', size=(20, 10))],
        [sg.ProgressBar(50, orientation='h', size=(100, 20), border_width=4, key='-PROGRESS_BAR-', bar_color=("Blue","Yellow"))],
        [sg.Button('Sort'), sg.Button('Pause Sort'), sg.Button('Exit')]]

window =sg.Window("Progress Bar",layout)

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:break
    list_length = int(values['-LIST_LENGTH-'])
    random_number_list = generate_random_number_list(list_length)
    max = ((list_length)*(list_length - 1))/2

    if event == "Sort":
        for i in bubble_count(random_number_list):
            event, values = window.read(10)
            if event == 'Exit' or event == sg.WIN_CLOSED:break    
            window['-PROGRESS_BAR-'].update(max=max, current_count=i)
        
window.close()
