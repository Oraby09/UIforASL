from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class ASLApp(App):
    def build(self):
        # Create the main layout
        main_layout = BoxLayout(orientation='horizontal', padding=10, spacing=10)

        # ASL Input Box Layout
        asl_input_layout = BoxLayout(orientation='vertical', padding=20)
        asl_input_label = Label(text="ASL Input", size_hint=(1, 0.1), font_size=24)
        
        # ASL Input TextInput (drag and drop area)
        input_area = TextInput(text="Drag & Drop or Upload Image/Video",
                               readonly=True,
                               halign='center',
                               size_hint=(1, 0.7),
                               background_color=(0.2, 0.2, 0.2, 1),
                               foreground_color=(1, 1, 1, 1),
                               multiline=False)
        # Bind the size change to adjust vertical padding
        input_area.bind(size=self.update_padding)

        # ASL Input buttons
        input_buttons_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=10)
        media_button = Button(text="Media", size_hint=(0.5, 1), background_color=(0.2, 0.2, 1, 1))
        live_button = Button(text="Live", size_hint=(0.5, 1), background_color=(0.2, 0.2, 1, 1))
        input_buttons_layout.add_widget(media_button)
        input_buttons_layout.add_widget(live_button)

        # Add components to the input layout
        asl_input_layout.add_widget(asl_input_label)
        asl_input_layout.add_widget(input_area)
        asl_input_layout.add_widget(input_buttons_layout)

        # ASL Output Box Layout
        asl_output_layout = BoxLayout(orientation='vertical', padding=20)
        asl_output_label = Label(text="ASL Output", size_hint=(1, 0.1), font_size=24)
        
        # ASL Output TextInput (output area)
        output_area = TextInput(text="Recognition/Translation Output",
                                readonly=True,
                                halign='center',
                                size_hint=(1, 0.7),
                                background_color=(0.2, 0.2, 0.2, 1),
                                foreground_color=(1, 1, 1, 1),
                                multiline=False)
        output_area.bind(size=self.update_padding)  # Bind size to adjust padding

        # ASL Output buttons
        output_buttons_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=10)
        recognition_button = Button(text="Recognition", size_hint=(0.33, 1), background_color=(0.2, 0.2, 1, 1))
        translation_button = Button(text="Translation", size_hint=(0.33, 1), background_color=(0.2, 0.2, 1, 1))
        text_asl_button = Button(text="Text to ASL", size_hint=(0.33, 1), background_color=(0.2, 0.2, 1, 1))
        output_buttons_layout.add_widget(recognition_button)
        output_buttons_layout.add_widget(translation_button)
        output_buttons_layout.add_widget(text_asl_button)

        # Add components to the output layout
        asl_output_layout.add_widget(asl_output_label)
        asl_output_layout.add_widget(output_area)
        asl_output_layout.add_widget(output_buttons_layout)

        # Add input and output layouts to the main layout
        main_layout.add_widget(asl_input_layout)
        main_layout.add_widget(asl_output_layout)

        return main_layout

    # Update padding function for vertical centering
    def update_padding(self, instance, value):
        # Set padding_y based on the widget's height and text line height
        instance.padding_y = (instance.height - instance.line_height) / 2

if __name__ == '__main__':
    ASLApp().run()
