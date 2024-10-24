from multiprocessing import Pool

def square(x):
    return x * x

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        results = pool.map(square, range(10))
        
    print(results)
    
    
    
from multiprocessing import Process, Event

def wait_for_event(e):
    print('Process started')
    e.wait()
    print('Event received')

if __name__ == '__main__':
    event = Event()
    
    p1 = Process(target=wait_for_event, args=(event,))
    p1.start()
    
    input('Press Enter to set the event...')
    event.set()
    
    p1.join()