from ftplib import FTP

url = 'ftphost'
port = 21
username = 'username'
password = 'password'
file_path = '/layout/site/resource/cmpict/uar'
save_path = 'C:\\Users\\lwang\\Documents\\uar_img\\'


class Crawler():
    def __init__(self, url, port, username, password, file_path):
        self.__ftp = FTP()
        self.__ftp.set_pasv(True)
        self.__ftp.set_debuglevel(0)

        self.__ftp.connect(host=url, port=port)
        self.__ftp.login(user=username, passwd=password)
        self.__ftp.pwd()
        #self.__ftp.dir()
        self.__ftp.cwd(file_path)

    def crawl(self, file_name, save_path):

        path = save_path + file_name  # 文件保存路径
        f = open(path, 'wb')  # 打开要保存文件
        filename = 'RETR ' + file_name  # 保存FTP文件
        try:
            response_code = self.__ftp.retrbinary(filename, f.write)  # 保存FTP上的文件
        except:
            pass
        # ftp.retrlines('LIST')

    def close(self):
        self.__ftp.close()


if __name__ == '__main__':

    myCrawler = Crawler(url,port,username,password,file_path)

    f = open('filelist')
    line = f.readline()  # 1行を文字列として読み込む(改行文字も含まれる)

    while line:
        print(line)
        file_name = line.replace('\n', '')
        myCrawler.crawl(file_name,save_path)
        line = f.readline()
    f.close()
    myCrawler.close()
    # crawl()
