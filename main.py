from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class RevengeGame(App):
    def build(self):
        self.stage = 1
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.story_label = Label(
            text="=== INTIQAM: Tailor ki Wapsi ===\n\nMultan mein aap ki dukan chhin chuki hai.\nMubashir, Shiraz aur Maimoona ne aap ko nikala.\nAap gaaon mein hain. Badla kaise shuru karein?",
            halign="center",
            font_size='16sp'
        )
        self.layout.add_widget(self.story_label)
        
        self.btn1 = Button(text="1. Mubashir ka dukan system hack karein", size_hint=(1, 0.2))
        self.btn1.bind(on_press=self.process_choice_1)
        self.layout.add_widget(self.btn1)
        
        self.btn2 = Button(text="2. Shiraz ke khilaf saboot ikathay karein", size_hint=(1, 0.2))
        self.btn2.bind(on_press=self.process_choice_2)
        self.layout.add_widget(self.btn2)
        
        return self.layout

    def process_choice_1(self, instance):
        if self.stage == 1:
            self.stage = 2
            self.story_label.text = "Aap ne Mubashir ka system hack kar ke us ka business tabah kar diya!\n\nAb Multan wapsi ka waqt hai. Aage kya karenge?"
            self.btn1.text = "Multan ja kar dukan par sidha hamla karein"
            self.btn2.text = "Hacking aur Drone se teenon ko gher lein"
        elif self.stage == 2:
            self.stage = 3
            self.story_label.text = "Aap ne Multan ja kar Mubashir, Shiraz aur Maimoona ko zaleel kiya aur apna badla pura kiya!\n\nNazakanda aap ke sath hai aur dukan wapis mil gayi.\n\n*** GAME OVER (YOU WIN) ***"
            self.btn1.text = "Dobara Kholein (Restart)"
            self.btn2.text = "Khel Khatam"
        elif self.stage == 3:
            self.reset_game()

    def process_choice_2(self, instance):
        if self.stage == 1:
            self.stage = 2
            self.story_label.text = "Aap ne Shiraz ki khfiya baatein leak kar ke usey zaleel kar diya!\n\nAb Multan wapsi ka waqt hai. Aage kya karenge?"
            self.btn1.text = "Multan ja kar dukan par sidha hamla karein"
            self.btn2.text = "Hacking aur Drone se teenon ko gher lein"
        elif self.stage == 2:
            self.stage = 3
            self.story_label.text = "Drone aur Hacking se aap ne teeno dushmanon ka khatma kar diya!\n\nNazakanda ko wapis hasil kar ke aap ne apni nayi zindagi shuru ki.\n\n*** GAME OVER (YOU WIN) ***"
            self.btn1.text = "Dobara Kholein (Restart)"
            self.btn2.text = "Khel Khatam"
        elif self.stage == 3:
            App.get_running_app().stop()

    def reset_game(self):
        self.stage = 1
        self.story_label.text = "=== INTIQAM: Tailor ki Wapsi ===\n\nMultan mein aap ki dukan chhin chuki hai.\nMubashir, Shiraz aur Maimoona ne aap ko nikala.\nAap gaaon mein hain. Badla kaise shuru karein?"
        self.btn1.text = "1. Mubashir ka dukan system hack karein"
        self.btn2.text = "2. Shiraz ke khilaf saboot ikathay karein"

if __name__ == '__main__':
    RevengeGame().run()
