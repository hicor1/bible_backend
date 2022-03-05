import timeit
import psycopg2
import pandas as pd
import datetime
import os

## DB정보 불러오기 ##
ConnectInfo = {'host'     :os.environ.get("SQL_HOST",     "3.37.42.132"),
               'dbname'   :os.environ.get("SQL_DATABASE", "BIS"),
               'user'     :os.environ.get("SQL_USER",     "hicor"),
               'password' :os.environ.get("SQL_PASSWORD", "dlacodnr1!"),
               'port'     :os.environ.get("SQL_PORT",     "4040"),
               'options'  :'-c search_path=dbo,public'}

#%%
def DB_Read(SQL):

    #. 시작시간 체크
    tic=timeit.default_timer()
    
    #. DB 연결 열기
    conn = psycopg2.connect(host     = ConnectInfo['host'],
                            dbname   = ConnectInfo['dbname'],
                            user     = ConnectInfo['user'],
                            password = ConnectInfo['password'],
                            port     = ConnectInfo['port'],
                            options  = ConnectInfo['options'])
    cur = conn.cursor()
    
    
    try: # 쿼리결과가 없으면 에러발생, 예외처리 ㄱㄱ
        result = pd.read_sql(SQL, conn)

    except:
        result = pd.DataFrame() # 빈 데이터 프레임 리턴

    #. DB 연결 종료
    cur.close()
    conn.close()
    
    #. 종료시간 체크
    toc=timeit.default_timer()
    #. 프로세스 시간 산출 (ms)
    processtime = round((toc - tic)*1000,2)
    
    return {"processtime(ms)":processtime,
            "df" : result}

#%%

def GetBibleBookList():
    SQL = """
        SELECT *
        FROM bible_book
        """
        
    return DB_Read(SQL)


def GetVersesList():
    SQL = """
        SELECT "_id", "쉬운성경"
        FROM bible_verses
        """
        
    return DB_Read(SQL)


#%%
if __name__ == "__main__":
    #data = GetBibleBookList()
    data = GetVersesList()