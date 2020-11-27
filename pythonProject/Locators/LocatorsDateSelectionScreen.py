import calendar
import datetime

from Locators.Locators import Locator


def generate_dates(time_between_dates):
    now = datetime.datetime.now()
    date_1 = f"{now.day + 1:02d} " + calendar.month_name[now.month] + " " + str(now.year)
    then = now + datetime.timedelta(days=time_between_dates)
    date_2 = f"{then.day:02d} " + calendar.month_name[then.month] + " " + str(then.year)
    return date_1, date_2


class LocatorsDateSelectionScreen(Locator):
    calendar_view = "com.booking:id/bui_calendar_view"
    confirm_button = "com.booking:id/calendar_confirm"
    date_1, date_2 = generate_dates(15)
    initial_date_android = '//android.view.View[@content-desc="' + date_1 + '"]'
    end_date_android = '//android.view.View[@content-desc="' + date_2 + '"]'
