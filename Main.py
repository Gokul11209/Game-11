from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.icon_definitions import md_icons
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import ThreeLineAvatarIconListItem, IRightBodyTouch, OneLineListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.tab import MDTabsBase

Window.size = (310, 600)

KV = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "LENOVO"
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        right_action_items:[['alarm-note'],['wallet-outline']]
                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                    MDBottomNavigation:
                        id:bottom_nav
                        # on_tab_touch_down:app.on_tab_switch(*args)
                            # text: 'Mail'
                            # icon: 'gmail'
                            # badge_icon: "numeric-10"
                        
        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 0, 50, 50) 
            ContentNavigationDrawer:


<ContentNavigationDrawer>:                               #LEVEL===1
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 1, 1, 1, 1
        MDBoxLayout:
            orientation: 'vertical'
            size_hint: (1,.25)
            pos_hint:{"top":1}
            md_bg_color: .7, .7, .2, .5 #app.theme_cls.primary_color       
            padding: "8dp"
            spacing: "12dp"
            MDBoxLayout:
                radius: (50, 50, 50, 50)
                size_hint: (.2,.7)
                pos_hint:{"top":1}
                # md_bg_color: .7, .7, .2, .5
                Image:
                    id: profile_img_id
                    size_hint: (1,1)
                    source: "index.jpeg"
            MDBoxLayout:
                size_hint: (1,.8)
                # md_bg_color: .7, .7, .2, .5       
                MDLabel:
                    id:email_field
                    text: "gokulprasath5702@gmail.com"
                    size_hint: (1,1)
                        # font_style: "Caption"
            MDBoxLayout:
                size_hint: (1,.8)
                # md_bg_color: .7, .7, .2, .5       
                MDLabel:
                    id:phone_field
                    text: "6380298755"
                    size_hint: (1,1)
            MDBoxLayout:
                size_hint: (1,.8)
                # md_bg_color: .7, .7, .2, .5       
                MDLabel:
                    id:level_field
                    text: "Level :  3"
                    size_hint: (1,1)

        MDBoxLayout:                            #LEVEL:2
            orientation: 'vertical'
            size_hint: (1,.75)
            md_bg_color: 1,1,1,1 #app.theme_cls.primary_color       
            padding: "8dp"
            spacing: "20dp"
            MDBoxLayout:
                orientation: 'vertical'
                # md_bg_color: 0,1,1,1
                pos_hint:{"top":1}
                size_hint: (.75,.15)
                MDRectangleFlatIconButton:
                    text: "My Balance"
                    text_color: 0, 1, 0, 1
                    icon: "wallet-outline"
                    line_color: 0, 0, 0, 0
                    pos_hint: {"top":1}  
            
            MDBoxLayout:
                orientation: 'vertical'
                size_hint: (1,.15)
                # md_bg_color:1,0,1,1
                MDRectangleFlatIconButton:
                    text:"How To Play"
                    text_color: 0, 1, 0, 1
                    icon: "animation-play"
                    line_color: 0, 0, 0, 0
                    pos_hint: {"top":1}    
            MDBoxLayout:
                orientation: 'vertical'
                size_hint: (1,.15)
                # text_color: 0, 1, 0, 1
                MDRectangleFlatIconButton:
                    text: "My Friends"
                    text_color: 0, 1, 0, 1
                    icon: "account-multiple-plus-outline"
                    line_color: 0, 0, 0, 0
                    pos_hint: {"top":1}    
            MDBoxLayout:
                orientation: 'vertical'
                # md_bg_color: 0,1,1,1
                size_hint: (1,.15)
                MDRectangleFlatIconButton:
                    text: "Invite Eran 100"
                    text_color: 0, 1, 0, 1
                    icon: "account-cash-outline"
                    line_color: 0, 0, 0, 0
                    pos_hint: {"top":1}    
            MDBoxLayout:
                orientation: 'vertical'
                size_hint: (1,.15)
                MDRectangleFlatIconButton:
                    text: "INFO"
                    text_color: 0, 1, 0, 1
                    icon: "axis-arrow-info"
                    line_color: 0, 0, 0, 0
                    pos_hint: {"top":1}    
            MDBoxLayout:
                orientation: 'vertical'
                size_hint: (1,.15) 
                MDRectangleFlatIconButton:
                    text: "Settings"
                    text_color: 0, 1, 0, 1
                    icon: "account-settings"
                    line_color: 0, 0, 0, 0
                    pos_hint: {"top":1} 
            MDBoxLayout:
                orientation: 'vertical'
                size_hint: (1,.10)  
                       
                                   
<Tab>:
    ThreeLineAvatarIconListItem:
        id:matchs_id
        text: ""
        secondary_text:""
        tertiary_text: ""
        radius: [50, 50, 50, 50]
    
        IconLeftWidget:
            id:left_ico
            icon: ""
    
        IconRightWidget:
            id:right_ico
            icon: ""
    MDLabel:
        id: label
        text: "Tab 0"
        halign: "center"
  

<MDBottomNavigationItem>:
    MDLabel:
        id: label
        text: ""
        halign: "center"
 """


class ContentNavigationDrawer(MDBoxLayout):
    pass
    # screen_manager = ObjectProperty()
    # nav_drawer = ObjectProperty()


class Tab(MDFloatLayout,MDTabsBase):
    pass



class DemoApp(MDApp):
    sports = [["Cricket", "cricket"], ["Kabddi", "kabaddi"], ["Football", "football-australian"], ["Vollyball", "volleyball"],["Hocky","hockey-sticks"],["Basketball","basketball"]]
    bottom_navigation = [["Home", "home"], ["Match", "cricket"], ["Winner", "trophy-outline"], ["Chat", "chat-alert-outline"]]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        screen = Builder.load_string(KV)
        self.theme_cls.primary_palette = "Blue"
        return screen

    def on_start(self):
        for tab_name in self.sports:
            self.root.ids.tabs.add_widget(Tab(title_icon_mode="Lead", title=tab_name[0], icon=tab_name[1]))

        for bot_nav in self.bottom_navigation:
            self.root.ids.bottom_nav.add_widget(MDBottomNavigationItem(text=bot_nav[0], icon=bot_nav[1]))

        # for i in range(0,5):
        #     self.root.ids.matchs_id.add_widget(ThreeLineAvatarIconListItem(text="CSK VS MI"))
    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        count_icon = instance_tab.icon
        tab = tab_text.split(" ")
        tab= tab[::-1]
        # print(tab[0])
        instance_tab.ids.label.text = tab[0]
        instance_tab.ids.matchs_id.text="CSK   VS   MI"
        instance_tab.ids.matchs_id.secondary_text="Ipl 2023"
        instance_tab.ids.matchs_id.tertiary_text="07:30"
        instance_tab.ids.left_ico.icon="csk.ico"
        instance_tab.ids.right_ico.icon="csk.ico"

        print("gokul")
DemoApp().run()