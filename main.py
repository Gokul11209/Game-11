from kivy.properties import ObjectProperty, StringProperty
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.icon_definitions import md_icons
from kivymd.uix.bottomnavigation import MDBottomNavigationItem
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

Window.size = (310, 600)

navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDBoxLayout:
                    orientation: 'vertical'
                    MDBoxLayout:
                        orientation: 'vertical'
                        size_hint:(1,.2)
                        # md_bg_color: app.theme_cls.primary_color
                        MDToolbar:
                            title: "LENOVO"
                            left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                            # pos_hint:{"top":1}
                        MDTabs:
                            id: tabs
                            on_tab_switch: app.on_tab_switch(*args)
                        MDBottomNavigation:
                            id:bottom_nav
                            # on_tab_touch_down:app.on_tab_switch(*args)
                                # text: 'Mail'
                                # icon: 'gmail'
                                # badge_icon: "numeric-10"
                    # Homepage: 
                    
        MDNavigationDrawer:
            id: nav_drawer
            # radius: (50, 50, 50, 50) 
            ContentNavigationDrawer:
                            
    
        # panel_color: "#eeeaea"
        # selected_color_background: "#97ecf8"
        # text_color_active: 0, 0, 0, 1

        
        #     name: 'screen 1'
        #     
                     
<ContentNavigationDrawer>:
    MDBoxLayout:
        orientation: 'horizontal'
        size_hint: (1,.25)
        pos_hint:{"top":1}
        md_bg_color: app.theme_cls.primary_color       
        padding: "8dp"
        spacing: "8dp"
<Tab>:
    MDLabel:
        id: label
        text: "Tab 0"
        halign: "center"
        
<MDBottomNavigationItem>:
    MDLabel:
        id: label
        text: ""
        halign: "center"
        

<Homepage>:
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color:.2,.4,.6,.9
        size_hint:(1,1)
        md_bg_color: 1,0,.5,.6
        padding: "8dp"
        spacing: "8dp"
        MDBoxLayout:
            orientation: 'vertical'
            md_bg_color:.2,.4,.1,.3
            size_hint:(1,.2)
        MDBoxLayout:
            orientation: 'vertical'
            md_bg_color:0,0,0,1
            size_hint:(1,.2)
        MDLabel:
            text: "gokulprasath@gmail.com"
            size_hint_y: None
            font_style: "Caption"
            pos_hint:{"top":1}
          
                       
 """

class ContentNavigationDrawer(MDBoxLayout):
    pass
    # screen_manager = ObjectProperty()
    # nav_drawer = ObjectProperty()

class Tab(MDFloatLayout, MDTabsBase):
    pass
class Homepage(MDBoxLayout):
    pass

class DemoApp(MDApp):
    sports= [["cric","cricket"],["kab","kabaddi"],["Foot","football-australian"],["Volly","volleyball"]]
    bottom_navigation=[["Home","home"],["Match","database"],["Winner","zodiac-libra"],["Chat","chat-alert"]]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        screen = Builder.load_string(navigation_helper)
        self.theme_cls.primary_palette = "Pink"
        return screen

    def on_start(self):
        for tab_name in self.sports:
            self.root.ids.tabs.add_widget(Tab(title_icon_mode="Lead",title=tab_name[0],icon=tab_name[1]))

        for bot_nav in self.bottom_navigation:
            self.root.ids.bottom_nav.add_widget(MDBottomNavigationItem(text=bot_nav[0],icon=bot_nav[1]))
    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        count_icon = instance_tab.icon
        instance_tab.ids.label.text = tab_text
        print("gokul")
DemoApp().run()
print('😇😁😚😜🐴🐹')
