# import os
# from tkinter import Tk, filedialog, messagebox
# from ultralytics import YOLO

# model = YOLO(r"C:\Users\Hirad\Desktop\PRE\Traffic_Control.pt")

# def select_folder():
#     root = Tk()
#     root.withdraw() 
#     folder_selected = filedialog.askdirectory()  
#     return folder_selected


# def Run(input_folder, output_folder):
#     os.makedirs(output_folder, exist_ok=True)
#     for filename in os.listdir(input_folder):
#         if filename.endswith(('.jpg', '.png', '.jpeg')):
#             image_path = os.path.join(input_folder, filename)
#             results = model.predict(source=image_path, conf=0.5, save=True)  
#             print(f"Processed: {filename}")
#     messagebox.showinfo("Success", "All images processed successfully!")  

# input_folder = select_folder()

# if input_folder:  
#     output_folder = os.path.join(input_folder, 'predict')
#     Run(input_folder, output_folder)
# else:
#     messagebox.showerror("Error", "No folder selected!") 




















#بدون پوشه
# import os
# from ultralytics import YOLO
# model = YOLO(r"C:\Users\Hirad\Desktop\PRE\Traffic_Control.pt")

# def Run(input_folder, output_folder):
#     os.makedirs(output_folder, exist_ok=True) 
#     for filename in os.listdir(input_folder):
#         if filename.endswith(('.jpg', '.png', '.jpeg')):
#             image_path = os.path.join(input_folder, filename)
#             results = model.predict(source=image_path, conf=0.5, save=True) 
#             print(f"Processed: {filename}")
#     print("All images processed successfully!") 

# input_folder = r"C:\Users\Hirad\Desktop\predict"
# output_folder = os.path.join(input_folder, 'predict') 
# Run(input_folder, output_folder)







from ultralytics import YOLO

model = YOLO(r"C:\Users\Hirad\Desktop\PRE\Traffic_Control.pt")

image_path = r"C:\Users\Hirad\Desktop\predict\0000_14.jpg"
results = model.predict(source=image_path, conf=0.5, save=True)  
print(f"Processed: {image_path}")
