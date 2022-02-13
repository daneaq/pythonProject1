from weixin_ui_test.page.base import Base
from weixin_ui_test.page.contact import Contact


class Main(Base):

    def goto_contact(self):
        self.steps("../page/steps.yaml")

        return Contact(self._driver)

