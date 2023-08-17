import customtkinter
"""
opens a gui for parametes selection.
adds mode , trials num and blocks num in that order to the "output" argument
"""
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




    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)

    text = "Welcome to our experiment! \nPlease enter parameters in order to start.\n\n"

    label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.CENTER, text= text)
    label_1.pack(pady=10, padx=10)

    optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["TRAIN", "TEST"])
    optionmenu_1.pack(pady=10, padx=10)
    optionmenu_1.set("mode:")

    entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="trials number")
    entry_1.pack(pady=10, padx=10)

    entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="blocks number")
    entry_2.pack(pady=10, padx=10)


    submit_button = customtkinter.CTkButton(text = "Submit" , width= 200 ,  master=frame_1, command=button_callback , hover_color= "green")
    submit_button.pack(pady=10, padx=10)

    app.mainloop()


if __name__ == '__main__':
    main()