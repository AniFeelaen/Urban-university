from datetime import datetime
from multiprocessing import Pool
def read_info(name):
    all_data = []
    with open(name, 'r',encoding= 'utf-8') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            all_data.append(line)

filenames = [f'project_urban_multi/file_{number}.txt' for number in range(1, 4)]
# filenames = ['file_1.txt', 'file_2.txt', 'file_3.txt','file_4.txt']
# Линейная обработка файлов
time_start = datetime.now()
for filename in filenames:
    data = read_info(filename)
time_end = datetime.now()
time_res = time_end - time_start
print(time_res)

# мультипроцессорная обработка файлов
if __name__ == '__main__':
    # time_start = datetime.now()
    with Pool(processes=4) as pool:
        time_start1 = datetime.now()
        results = pool.map(read_info, filenames)
        time_end1 = datetime.now()
        time_res = time_end1 - time_start1
        print(time_res)
    # time_end = datetime.now()
    # time_res = time_end - time_start
    # print(time_res)