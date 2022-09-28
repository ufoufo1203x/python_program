from random import randint
import logging
logging.basicConfig(filename ='use_loggiingLog.txt', level=logging.DEBUG, format=" %(asctime)s - %(asctime)s - %(levelname)s - %(message)s")

def main():
    counter = 0
    while counter < 10:
        number = randint(1, 13)
        print("{0}回目は{1}。".format(counter+1, number))
        logging.debug("counter={0}, numebr={1}".format(counter, number))
        counter += 1
        
    if __name__ == '__main__':
        logging.debug("Program start")
        main()
        logging.debug("Program end")