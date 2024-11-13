from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel

class ASLApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation='horizontal', padding=20, spacing=20)

        # ASL Input Card
        asl_input_card = MDCard(orientation='vertical', padding=20, spacing=10, radius=[20, 20, 20, 20],
                                md_bg_color=(0.15, 0.15, 0.15, 1), size_hint=(0.5, 1))
        
        asl_input_label = MDLabel(
            text="ASL Input", 
            halign='center', 
            font_style='H5', 
            bold=True, 
            size_hint_y=0.1,
            theme_text_color="Custom", 
            text_color=(1, 1, 1, 1)  # Set text color to white
        )
        
        # ASL Input Area using MDLabel
        asl_input_area = MDLabel(
            text="Drag & Drop or Upload Image/Video", 
            halign="center",  # Center the text
            size_hint=(1, 0.7),
            font_size=20,  # Increase font size
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1)  # Set text color to black
        )
        
        # Buttons layout
        asl_input_buttons = MDBoxLayout(orientation='horizontal', spacing=20, padding=[0, 20, 0, 0], size_hint=(1, 0.1))
        
        media_button = MDRaisedButton(text="Media", md_bg_color=(0.2, 0.2, 1, 1), size_hint=(0.5, 1))
        live_button = MDRaisedButton(text="Live", md_bg_color=(0.2, 0.2, 1, 1), size_hint=(0.5, 1))
        
        asl_input_buttons.add_widget(media_button)
        asl_input_buttons.add_widget(live_button)

        # Add elements to ASL Input Card
        asl_input_card.add_widget(asl_input_label)
        asl_input_card.add_widget(asl_input_area)
        asl_input_card.add_widget(asl_input_buttons)

        # ASL Output Card
        asl_output_card = MDCard(orientation='vertical', padding=20, spacing=10, radius=[20, 20, 20, 20],
                                 md_bg_color=(0.15, 0.15, 0.15, 1), size_hint=(0.5, 1))
        
        asl_output_label = MDLabel(
            text="ASL Output", 
            halign='center', 
            font_style='H5', 
            bold=True, 
            size_hint_y=0.1,
            theme_text_color="Custom", 
            text_color=(1, 1, 1, 1)  # Set text color to white
        )
        
        # ASL Output Area using MDLabel
        asl_output_area = MDLabel(
            text="Recognition/Translation Output", 
            halign="center",  # Center the text
            size_hint=(1, 0.7),
            font_size=20,  # Increase font size
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1)  # Set text color to black
        )
        
        asl_output_buttons = MDBoxLayout(orientation='horizontal', spacing=20, padding=[0, 20, 0, 0], size_hint=(1, 0.1))
        
        recognition_button = MDRaisedButton(text="Recognition", md_bg_color=(0.2, 0.2, 1, 1), size_hint=(0.33, 1))
        translation_button = MDRaisedButton(text="Translation", md_bg_color=(0.2, 0.2, 1, 1), size_hint=(0.33, 1))
        text_asl_button = MDRaisedButton(text="Text to ASL", md_bg_color=(0.2, 0.2, 1, 1), size_hint=(0.33, 1))
        
        asl_output_buttons.add_widget(recognition_button)
        asl_output_buttons.add_widget(translation_button)
        asl_output_buttons.add_widget(text_asl_button)

        # Add elements to ASL Output Card
        asl_output_card.add_widget(asl_output_label)
        asl_output_card.add_widget(asl_output_area)
        asl_output_card.add_widget(asl_output_buttons)

        # Add both cards to the main layout
        layout.add_widget(asl_input_card)
        layout.add_widget(asl_output_card)

        return layout

ASLApp().run()
