# modules/utilities.py
def show_frame(container, frame_name):
    for child in container.winfo_children():
        if hasattr(child, 'tkraise'):
            if child.__class__.__name__ == frame_name:
                child.tkraise()
