# def calendarscheluding(ls):
#     week = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
#     les = [i["lessonRequestId"] for i in ls]
#     dur = [i["duration"] for i in ls]
#     earn = [i["potentialEarnings"] for i in ls]
#     day = []
#     days = [len(i) for i in day]
#     sch = [0 for i in range(len(les))]
#     h = [12 for i in range(7)]
#     finc = 0
#     cont = True
#     fsch = sch.copy()
#     while sch[0] <= days[0]:
#         inc = 0
#         for i in range(len(sch)):
#             if h[day[i][sch[i]]] >= dur[i]:
#                 h[day[i][sch[i]]] -= dur[i]
#                 inc += earn[i]
            
#         sch[-1] += 1
#         for i in range(1, len(sch2)):
#             if sch2[-i] == days[-i]:
#                 schs[-i] = 0
#                 schs[-i-1] += 1
        
            
                
                
                
                
                
                
                
                
                
#                 if sch2[-i] == days[-i] - 1:
#                     for j in range(1, len(sch) + 1):
#                         if 
#                         if day[-i].index(sch2[-i]) == len(day[-i]) - 1
#                 else:
#                     sch2[-i] = day[day[-i].index(sch2[-i]) + 1]
#                 ind = len(sch2) - i
#                 break
#         for l in range(ind + 1, len(sch2)):
#             for d in day[l]:
#                 if h[d] >= dur[l]:
#                     h[d] -= dur[l]
#                     inc2 += earn[l]
#                     sch2[l] = d
#         if inc2 >= inc:
#             inc = inc2
#             fsch = sch2
#         sch = sch2.copy()
        
#     print(fsch)
        
                
    
    
    
# x = [{
#     "lessonRequestId": "LR1",
#     "duration": 1,
#     "potentialEarnings": 100,
#     "availableDays": ["monday", "wednesday"]
# }, {
#     "lessonRequestId": "LR2",
#     "duration": 2,
#     "potentialEarnings": 50,
#     "availableDays": ["monday"]
# }, {
#     "lessonRequestId": "LR3",
#     "duration": 12,
#     "potentialEarnings": 1000,
#     "availableDays": ["wednesday"]
# }, {
#     "lessonRequestId": "LR4",
#     "duration": 13,
#     "potentialEarnings": 10000,
#     "availableDays": ["friday"]
# }] 
# print(calendarscheluding(x))