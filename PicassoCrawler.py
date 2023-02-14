from Drivers import chromeDriver
import time


def goToPicasso():
    chromeDriver.get(r'https://picasso-27m8.onrender.com')

def refreshPicaso():
    chromeDriver.refresh()

def keepingPicassoAlive():
        goToPicasso()

        while True:
            print("refreshing")
            refreshPicaso 
            time.sleep(600)
            
        


if __name__ == '__main__':
    keepingPicassoAlive()