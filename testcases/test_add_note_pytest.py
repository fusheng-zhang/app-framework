from datetime import datetime
import allure
import pytest
import yaml
from pageObjects.pages.page_first_open import FirstOpenPage
from pageObjects.pages.add_note_page import AddNotePage
from utils.get_path import PATH




@allure.feature("笔记功能")
class TestNotePytest(object):
    @allure.step("初始化，打开手机，同意权限")
    @pytest.fixture(scope='module', autouse=True)
    def agree_init(self, run_app):
        # 初始化driver，文件级通用
        # 先初始化页面，
        firstOpen = FirstOpenPage(run_app)
        # 操作的方法
        firstOpen.permission_allowandok()

    @allure.story("添加笔记功能")
    @pytest.mark.regression
    @allure.severity("critical")
    @pytest.mark.parametrize("add",
                             yaml.safe_load(open(PATH("../testdatas/" + "addnotedata.yaml"), 'r', encoding='utf8')))
    def test_addnote(self, add, run_app):
        note_title = add
        # 初始化添加笔记页
        with allure.step("初始化添加页面"):
            addnote = AddNotePage(run_app)
        # # 添加标题和内容
        addnote.add_note_ok(note_title)
        # # 截图
        # addnote.save_pic(PATH("../reports/screenshots/" + str(datetime.now())) + "addnote.png")

    @pytest.mark.sanity
    # @pytest.mark.skip
    def test_deletenote(self):
        pass
