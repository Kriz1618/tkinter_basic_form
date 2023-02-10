from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title('Data Entry Form')

frame = Frame(window)
frame.pack()

user_info_frame = LabelFrame(frame, text='User Info')
user_info_frame.grid(row=0, column=0, padx=20, pady=20)

first_name_label = Label(user_info_frame, text='First Name')
first_name_label.grid(row=0, column=0)
last_name_label = Label(user_info_frame, text='Last Name').grid(row=0, column=1)

first_name_entry = Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry = Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title_label = Label(user_info_frame, text='Title')
title_combobox = ttk.Combobox(user_info_frame, values=['', 'Mr.', 'Ms.', 'Dr.'])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = Label(user_info_frame, text='Age')
age_spinbox = Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = Label(user_info_frame, text='Natinality')
nationality_combobox = ttk.Combobox(user_info_frame, values=['Africa', 'Antartica', 'Asia', 'Europe', 'North America', 'Oceania', 'South America'])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


courses_frame = LabelFrame(frame, text='Courses')
courses_frame.grid(row=1, column=0, sticky='news', padx=20, pady=20)

registered_label = Label(courses_frame,text='Registration Status')
reg_status_var = StringVar(value="Not Registered")
registered_check = Checkbutton(courses_frame,text='Currently Registered', variable=reg_status_var, onvalue="Registered", offvalue="Not registered")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

num_courses_label = Label(courses_frame, text='# Completed Courses')
num_courses_spinbox = Spinbox(courses_frame, from_=0, to='infinity')
num_courses_label.grid(row=0, column=1)
num_courses_spinbox.grid(row=1, column=1)

semester_label = Label(courses_frame, text='# Semesters')
semester_spinbox = Spinbox(courses_frame, from_=0, to='infinity')
semester_label.grid(row=0, column=2)
semester_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)



terms_frame = LabelFrame(frame, text='Terms & Conditions')
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = StringVar(value="Not Accepted")
terms_check = Checkbutton(terms_frame, text= "I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)


def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            
            # Course info
            registration_status = reg_status_var.get()
            numcourses = num_courses_spinbox.get()
            numsemesters = semester_spinbox.get()
            
            print("First name: ", firstname, "Last name: ", lastname)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
            print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
            print("Registration status", registration_status)
            print("------------------------------------------")
        else:
            messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        messagebox.showwarning(title= "Error", message="You have not accepted the terms")
        
        
# Button
button = Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
