import random

def time(start_time, end_time):
    #Define Parameters
    lst = []
    s_hour = ''
    s_min = ''
    final = {}
    
    e_hour = ''
    e_min = ''
    
    #Seperating hour and minute
    for i in range(len(start_time)):
        if start_time[i] != ':':
            s_hour += str(start_time[i])
        else:
            s_min += str(start_time[i + 1:])
            break
        
    for i in range(len(end_time)):
        if end_time[i] != ':':
            e_hour += str(end_time[i])
        else:
            e_min += str(end_time[i + 1:])
            break
        
    c_time = 0
    #Changes e_hour into military time
    if int(e_hour) < int(s_hour):
        e_hour = int(e_hour)
        e_hour += 12
    
    for i in range(int(s_hour), int(e_hour)+1):
        for j in range(0, 60, 5):
            #Return statement
            if len(str(j)) == 1:
                if (str(i) + ':' + '0' + str(j)) == str(e_hour) + ':' + e_min:
                    if (i-12) > 0:
                        lst.append(str(i-12)+ ':' + '0' + str(j))
                    else:
                        lst.append(str(i) + ':' + '0' + str(j))
                    return (lst)
            else:
                if (str(i) + ':' + str(j)) == str(e_hour) + ':' + e_min:
                    if (i-12) > 0:
                        lst.append(str(i-12)+ ':' + str(j))
                    else:
                        lst.append(str(i) + ':' + str(j))
                    return (lst)
            
            #In the event of a single digit minute
            if len(str(j)) == 1:
                c_time = int(str(i) + '0' + str(j))
            else:
                c_time = int(str(i) + str(j))
            
            #Outputs time
            if int(s_hour + s_min) <= c_time:
                if i > 12:
                    if len(str(j)) == 1:
                        lst.append(str(i-12)+ ':0' + str(j))
                    else:
                        lst.append(str(i-12)+ ':' + str(j))
                else:
                    if len(str(j)) == 1:
                        lst.append(str(i)+ ':0' + str(j))
                    else:
                        lst.append(str(i)+ ':' + str(j))
                    

def find_lunch():
    #Parameters
    d = {}
    grades = ['K', '1', '2', '3', '4', '5', 'LAMP']
    final = {}
    m_slots = [['10:40', '11:10'], ['11:40', '12:10'], ['12:45', '1:15']]
    
    #Variables
    opt = 0
    tru = 0
    
    #Initalizing final dictionary
    for i in grades:
        final[i] = 1
        
    while len(d) != 3:
        #Checks validity of K and LAMP for ease
        if 'K' not in d:
            d['K'] = m_slots[random.choice(range(len(m_slots)))]
            m_slots.pop(m_slots.index(d['K']))
            grades.pop(grades.index('K'))
            
        if 'LAMP' not in d:
            d['LAMP'] = m_slots[random.choice(range(len(m_slots)))]
            m_slots.pop(m_slots.index(d['LAMP']))
            grades.pop(grades.index('LAMP'))
        
        #Inputs random grade level into list
        opt = random.choice(range(len(grades)))
        d[str(opt+1)] = m_slots[random.choice(range(len(m_slots)))]
        grades.pop(grades.index(grades[opt]))
        m_slots.pop(m_slots.index(d[str(opt+1)]))
    
    #Selects time slot options
    opt = False
    
    #Going throuhg based on Kindergarden timeslots
    if d['K'] == ['11:40', '12:10']:
        l_time = time('10:55', d['K'][0])
        opt = time(d['K'][1], '1:00')
        
        while len(grades) != 0:
            if len(l_time) >=4:
                tru = random.choice(range(len(grades)))
                #In event of index error break
                try:
                    d[grades[tru]] = [l_time[0], l_time[5]]
                    
                except IndexError:
                    break
                #Randomizing choices for template variety
                l_time = l_time[4:]
                grades.pop(grades.index(grades[tru]))
                tru = random.choice(range(len(grades)))
                d[grades[tru]] = [opt[0], opt[5]]
                opt = opt[4:]
                grades.pop(grades.index(grades[tru]))
    else:
        if d['K'] == ['12:45', '1:15']:
            l_time = time('10:50', '11:45')
            opt = time('12:00', d['K'][0])
            while len(grades) != 0:
                if len(l_time) >= 5 :
                    tru = random.choice(range(len(grades)))
                    try:
                        d[grades[tru]] = [l_time[0], l_time[6]]
                    except IndexError:
                        break
                    l_time = l_time[4:]
                    grades.pop(grades.index(grades[tru]))
                else:
                    tru = random.choice(range(len(grades)))
                    d[grades[tru]] = [opt[0], opt[5]]
                    opt = opt[4:]
                    grades.pop(grades.index(grades[tru]))
        else:
            l_time = time('11:10', '11:45')
            opt = time('12:05', '1:05')
            while len(grades) != 0:
                tru = random.choice(range(len(grades)))
                d[grades[tru]] = [l_time[0], l_time[5]]
                tru = random.choice(range(len(grades)))
                try:
                    d[grades[tru]] = [opt[0], opt[5]]
                except IndexError:
                    break
                opt = opt[4:]
                grades.pop(grades.index(grades[tru]))
    
    for i in d:
        final[i] = d[i]
    return(final)    
find_lunch()
        
def sched_format(csv_file, start_time, end_time):
    #Initalizes headers
    grades = ['K', '1', '2', '3', '4', '5', 'LAMP']
    
    #states a variable using the definition of time
    s_day = time(start_time, end_time)
    
    with open(csv_file, "w") as file:
        file.write("," + ",".join(grades) + "\n")
        
        #Writes the lines in each column according to order
        for i in range(len(s_day)):
            file.write(s_day[i] + "," + ",".join([""] * len(grades)) + "\n")

def seek(csv_file, period):
    grades = ['K', '1', '2', '3', '4', '5', 'LAMP']
    start = '8:40'
    end = '3:20'
    
    period = period.lower()
    if period == 'lunch':
        period = find_lunch()

    lst = []
    tempo = 0
    new_lst = []
     
    file = open(csv_file, 'r')
    lines = file.readlines()
 
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(',')
        if end in lines[i]:
            break
         
        else:
            for j in range(len(lines[i])):
                if j != 0 and i != 0:
                    if [grades[j-1], period.get(grades[j-1])] not in lst:
                        lst.append([grades[j-1], period.get(grades[j-1])])
                 
                for k in range(len(lst)):
                    tempo = time(lst[k][1][0], lst[k][1][1])
                    if not tempo in new_lst:
                        new_lst.append(tempo)
             
    with open(csv_file, "w") as f:
        for index in range(len(lines)):
            for i in range(1, len(lines[index])):
                for j in range(len(new_lst[i - 1])):
                    if lines[index][0] == new_lst[i - 1][j]:
                        col = lines[0].index(grades[i - 1])
                        lines[index][col] += 'Lunch'
            print(','.join(lines[index]), file=f)
    file.close()
    return lines
    
sched_format('schedule.csv', '8:40', '3:20')
seek('schedule.csv', 'Lunch')



