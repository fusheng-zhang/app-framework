from ..basePage import BasePage
from ..locators.locator_add_note import AddNotePageLoacators

class AddNotePage(BasePage):
    def add_note_ok(self, title):
        BasePage.click_thing(self, AddNotePageLoacators.add_note)
        BasePage.click_thing(self, AddNotePageLoacators.add_icon)
        BasePage.set_value(self, AddNotePageLoacators.note_title, title)
        BasePage.click_thing(self, AddNotePageLoacators.submit_complete)