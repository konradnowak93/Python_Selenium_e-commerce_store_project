import allure
import pytest
from allure_commons.types import AttachmentType
from shop.utils.driver_factory import DriverFactory

@pytest.fixture()
def setup(request):
    driver = DriverFactory.get_driver("chrome")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    failures_before_test = request.session.testsfailed
    yield
    if request.session.testsfailed != failures_before_test:
        allure.attach(driver.get_screenshot_as_png(), name="Test_failed", attachment_type=AttachmentType.PNG)
    driver.quit()