from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.properties import OptionProperty, StringProperty, ObjectProperty, ListProperty, AliasProperty, \
    BooleanProperty, NumericProperty
from kivy.lang.builder import Builder
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

import kivy
kivy.require('1.11.1')


Window.size = (1020, 600)
# Window.fullscreen = True

# Progress Bar


class CroppedImage(Image):
    """CroppedImage : Image widget where texture can be cropped with Stencil Instructions"""
    # position and size of the stencil mask (internal use)
    rectangle_pos = ListProperty([0, 0])
    rectangle_size = ListProperty([1, 1])
    # direction of cropping (bt -> bottom to top, lr -> left to right, ...)
    direction = OptionProperty('bt', options=['bt', 'tb', 'lr', 'rl'])
    # visible percentage of the image [0,100]
    visible_percent = NumericProperty(0)
    # minimum position of the portion of the image corresponding to 0% and length of 0% to 100% (in pixel of the image file)
    min_pos = NumericProperty(0)
    max_length = NumericProperty(100)

    def on_visible_percent(self, inst, val):
        self.update_view()

    def update_view(self):
        """update_view : update the pos and size of the rectangle stencil mask"""
        if self.texture:
            # get how image is resized (zoom factor)
            zoom_ratio = self.norm_image_size[1] / float(self.texture.size[1])
            # where going from bottom (0%) to top (100%)
            if self.direction == 'bt':
                self.rectangle_pos = self.center_x - self.norm_image_size[0] / 2., self.center_y - self.norm_image_size[
                    1] / 2.
                self.rectangle_size = self.norm_image_size[0], (
                    self.min_pos + self.max_length * self.visible_percent / 100.0) * zoom_ratio
            # where going from top (0%) to bottom (100%)
            elif self.direction == 'tb':
                self.rectangle_pos = self.center_x - self.norm_image_size[0] / 2., (
                    self.center_y + self.norm_image_size[1] / 2.) - (
                    self.min_pos + self.max_length * self.visible_percent / 100.0) * zoom_ratio
                self.rectangle_size = self.norm_image_size[0], (
                    self.min_pos + self.max_length * self.visible_percent / 100.0) * zoom_ratio
            # where going from left (0%) to right (100%)
            elif self.direction == 'lr':
                self.rectangle_pos = self.center_x - self.norm_image_size[0] / 2., self.center_y - self.norm_image_size[
                    1] / 2.
                self.rectangle_size = (self.min_pos + self.max_length * self.visible_percent / 100.0) * zoom_ratio, \
                    self.norm_image_size[1]
            # where going from right (0%) to left (100%)
            elif self.direction == 'rl':
                self.rectangle_pos = (self.center_x + self.norm_image_size[0] / 2.) - (
                    self.min_pos + self.max_length * self.visible_percent / 100.0) * zoom_ratio, self.center_y - \
                    self.norm_image_size[1] / 2.
                self.rectangle_size = (self.min_pos + self.max_length * self.visible_percent / 100.0) * zoom_ratio, \
                    self.norm_image_size[1]

    def on_direction(self, inst, val):
        self.update_view()

    def on_size(self, inst, val):
        self.update_view()

    def on_pos(self, inst, val):
        self.update_view()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class ImageProgressBar(FloatLayout):
    # Images Properties
    source_front = StringProperty(None)
    color_front = ListProperty([1, 1, 1, 1])
    source_progress = StringProperty(None)
    color_progress = ListProperty([0.196, 0.643, 0.808, 1])
    draw_progress_background = BooleanProperty(True)
    color_progress_background = ListProperty([0.035, 0.118, 0.149, 1])
    min_pos = NumericProperty(0)
    max_length = NumericProperty(0)
    value = NumericProperty(0)
    direction = OptionProperty('bt', options=['bt', 'tb', 'lr', 'rl'])
    text_auto = BooleanProperty(True)
    text = StringProperty('')

    def get_text_label(self):
        return self.ids['text_lbl']

    def on_text(self, inst, val):
        if self.text_auto:
            self.ids['text_lbl'].text = '%d %%' % (val,)
        else:
            self.ids['text_lbl'].text = self.text

    def on_text_auto(self, inst, val):
        self.ids['progress_image'].update_view()
        if self.text_auto:
            self.ids['text_lbl'].text = '%d %%' % (val,)
        else:
            self.ids['text_lbl'].text = self.text

    def on_value(self, inst, val):
        self.ids['progress_image'].visible_percent = val
        if self.text_auto:
            self.ids['text_lbl'].text = '%d %%' % (val,)
        else:
            self.ids['text_lbl'].text = self.text

    def on_direction(self, inst, val):
        self.ids['progress_image'].direction = val

    def on_min_pos(self, inst, val):
        self.ids['progress_image'].min_pos = val

    def on_max_length(self, inst, val):
        self.ids['progress_image'].max_length = val

    def first_update(self):
        self.ids['progress_image'].update_view()
        if self.text_auto:
            self.ids['text_lbl'].text = '%d %%' % (self.value,)
        else:
            self.ids['text_lbl'].text = self.text

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.first_update(), 0.1)


class HomePage(BoxLayout):
    pass


class HomeApp(MDApp):
    def build(self):
        return HomePage()


if __name__ == '__main__':
    HomeApp().run()
