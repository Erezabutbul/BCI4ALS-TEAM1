import customtkinter

def main(output):
        
    customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

    app = customtkinter.CTk()

    window_width = 600
    window_height = 400
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Set the window position and size
    app.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # app.geometry("600x780")
    app.title("Input Parameters Form")

    def button_callback():
        output.append(optionmenu_1.get())
        output.append(entry_1.get())
        output.append(entry_2.get())
        
        app.destroy()



    # def slider_callback(value):
    #     progressbar_1.set(value)


    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)

    # text_1 = customtkinter.CTkTextbox(master=frame_1, width=400, height=100)
    # text_1.pack(pady=10, padx=10)
    # text_1.insert("0.0", "Welcome to ")

    text = "Welcome to our experiment! \nPlease enter parameters in order to start.\n\n"

    label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.CENTER, text= text)
    label_1.pack(pady=10, padx=10)

    # progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
    # progressbar_1.pack(pady=10, padx=10)


    # slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=10, to=200)
    # slider_1.pack(pady=10, padx=10)
    # slider_1.set(0.5)


    optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["TRAIN", "TEST"])
    optionmenu_1.pack(pady=10, padx=10)
    optionmenu_1.set("mode:")

    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="trials number")
    entry_1.pack(pady=10, padx=10)

    entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="blocks number")
    entry_2.pack(pady=10, padx=10)


    submit_button = customtkinter.CTkButton(text = "Submit" , width= 200 ,  master=frame_1, command=button_callback , hover_color= "green")
    submit_button.pack(pady=10, padx=10)



    # combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
    # combobox_1.pack(pady=10, padx=10)
    # combobox_1.set("CTkComboBox")

    # checkbox_1 = customtkinter.CTkCheckBox(master=frame_1)
    # checkbox_1.pack(pady=10, padx=10)

    # radiobutton_var = customtkinter.IntVar(value=1)

    # radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1)
    # radiobutton_1.pack(pady=10, padx=10)

    # radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2)
    # radiobutton_2.pack(pady=10, padx=10)

    # switch_1 = customtkinter.CTkSwitch(master=frame_1)
    # switch_1.pack(pady=10, padx=10)


    # segmented_button_1 = customtkinter.CTkSegmentedButton(master=frame_1, values=["CTkSegmentedButton", "Value 2"])
    # segmented_button_1.pack(pady=10, padx=10)

    # tabview_1 = customtkinter.CTkTabview(master=frame_1, width=200, height=70)
    # tabview_1.pack(pady=10, padx=10)
    # tabview_1.add("CTkTabview")
    # tabview_1.add("Tab 2")

    app.mainloop()


if __name__ == '__main__':
    main()