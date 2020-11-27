from Locators.Locators import Locator


class LocatorsLocationSelectionScreen(Locator):
    # android
    search_bar_stay_android = "com.booking:id/disambiguation_search_edittext"
    search_bar_car_android = "com.booking:id/bookinggocars_activity_autocomplete_search_query"
    first_location_result_stay_android = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout' \
                                         '/android.widget''.FrameLayout/android.widget.LinearLayout/android.widget' \
                                         '.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[' \
                                         '2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget' \
                                         '.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget' \
                                         '.RecyclerView/android.widget.RelativeLayout[1] '
    first_location_result_car_android = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout' \
                                        '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget' \
                                        '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget' \
                                        '.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout '
