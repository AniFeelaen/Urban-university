team1_num = 5
team2_num = 6
team1_name = 'Мастера кода'
team2_name = "Волшебники данных"
print ('В команде %s, участников: %s' % (team1_name, team1_num))
print ("Итого сегодня в командах участников : %s и %s !" % (team1_num, team2_num))

score_2 = 42
print("Команда {} решила задач: {} !".format(team2_name, score_2))

team1_time = 1552.512
team2_time = 2153.31451
print("{} решили задачи за {} !".format(team2_name, team1_time))

score_1 = 40
print(f'Команды решили {score_1} и {score_2} задач.')
if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = team1_name
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = team2_name
else:
    challenge_result = "Ничья!"
print(f'Результат битвы: победа команды {challenge_result}')

tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) /tasks_total, 1)

print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")

