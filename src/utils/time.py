import datetime
import calendar

class get_time:
    time = datetime.date.today()
    days_num = calendar.monthrange(time.year, time.month)[1]

    # 当月第一天
    def first_day(self):
        first_day = datetime.date(self.time.year, self.time.month, 1) 
        return first_day      

    # 当月最后一天
    def last_day_of_current_month(self):
        last_day_of_current_month = datetime.date(self.time.year, self.time.month, self.days_num)    
        return last_day_of_current_month    

    # 前一个月最后一天
    def pre_month(self):
        pre_month = self.first_day() - datetime.timedelta(days = 1)  
        return pre_month

    # 前一个月的第一天
    def first_day_of_pre_month(self):
        first_day_of_pre_month = datetime.date(self.pre_month().year, self.pre_month().month, 1) 
        return first_day_of_pre_month  

    # 下个月的第一天
    def first_day_of_next_month(self):
        first_day_of_next_month = self.first_day() + datetime.timedelta(days = self.days_num)
        return first_day_of_next_month

    # 下个月的最后一天
    def next_month(self):
        next_month_days = calendar.monthrange(self.first_day_of_next_month().year, self.first_day_of_next_month().month)[1]  # 获取下个月有多少天
        next_month = self.first_day_of_next_month() + datetime.timedelta(days = next_month_days - 1)
        return next_month