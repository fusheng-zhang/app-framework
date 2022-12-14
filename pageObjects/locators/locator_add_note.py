from appium.webdriver.common.mobileby import MobileBy


class AddNotePageLoacators(object):
    add_note = (MobileBy.ID, "com.youdao.note:id/add_note")
    add_icon = (MobileBy.ID, "com.youdao.note:id/add_icon")
    note_title = (MobileBy.ID, "com.youdao.note:id/note_title")
    note_editText = (MobileBy.XPATH, "//android.widget.EditText")
    submit_complete = (MobileBy.ID, "com.youdao.note:id/actionbar_complete_text")
