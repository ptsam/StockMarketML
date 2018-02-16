
# coding: utf-8

# In[1]:


from contextlib import contextmanager
import sqlite3
import os


# In[2]:


@contextmanager
def db(db_filename='stock.db'):
    
    conn = sqlite3.connect(os.path.join('..', 'data', db_filename), detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)

    cur = conn.cursor()
    
    yield conn, cur
    
    conn.close()


# In[3]:


def create_tables():
    
    with db() as (conn, cur):
    
        cur.execute('CREATE TABLE IF NOT EXISTS ticks (stock text, date text, open real, high real, low real, close real, adjclose real, volume integer, unique (stock, date))')
        conn.commit()
        
        cur.execute('CREATE TABLE IF NOT EXISTS headlines (stock text, date text, source text, content text UNIQUE ON CONFLICT IGNORE)')
        conn.commit()      
        
        cur.execute('CREATE TABLE IF NOT EXISTS specialwords (word UNIQUE ON CONFLICT IGNORE)')
        conn.commit()


# In[4]:


def add_stock_ticks(entries):
    
    with db() as (conn, cur):
    
        cur.executemany("INSERT OR IGNORE INTO ticks VALUES (?,?,?,?,?,?,?,?)", entries)
        conn.commit()
    
def add_headlines(entries):
    
    with db() as (conn, cur):
    
        cur.executemany("INSERT OR IGNORE INTO headlines VALUES (?,?,?,?)", entries)
        conn.commit()
        
def clean_ticks():
    
    with db() as (conn, cur):
    
        cur.execute("DELETE FROM ticks WHERE adjclose='null'")
        conn.commit()


# In[5]:


if __name__ == "__main__":
    
    create_tables()


# In[6]:


if __name__ == "__main__":
    
    special_words = [ # Words Not in Glove
        ["**STATISTIC**"], 
         
        ["**COMPANY**"], 
        ["**COMPANY**owned"],
        ["**COMPANY**s"],
        ["**COMPANY**stock"],
        ["ex**COMPANY**"],
        ["**COMPANY**made"],
        ["madeby**COMPANY**"],
        ["**COMPANY**com"],
        
        ["**PRODUCT**phones"],
        ["**PRODUCT**com"],
        ["**PRODUCT**"],
        ["**PRODUCT**powered"],
        ["team**PRODUCT**"],
        ["**PRODUCT**like"],
        ["**PRODUCT**tablet"],
        ["**PRODUCT**authority"],
        
        ["singlecore"],
        ["nowassistant"],
        ["assistantenabled"],
        ["deeplearning"],
        ["wannacry"],
        ["wannacrypt"],
        ["qualcomms"],
        ["smartglasses"],
        ["selfdriving"],
        ["pichai"],
        ["zuckerberg"],
        ["geekwire"],
        ["uscanada"],
        ["outofstock"],
        ["outofsale"],
        ["demonetizing"],
        ["hydrogenpowered"],
        ["homebutton"],
        ["electriccar"],
        ["xamarin"],
        ["wellcalibrated"],
        ["antitrump"],
        ["multigpu"],
        ["voicerecognition"],
        ["firstgen"],
        ["secondgeneration"],
        ["thirdgeneration"],
        ["investbuy"],
        ["nearzero"],
        ["techsavvy"],
        ["steamvr"],
        ["mostlycomplete"],
        ["anticlimate"],
        ["taxbonuses"],
        ["steamos"],
        ["specialedition"],
        ["testdriving"],
        ["oneplus"],
        ["airpods"],
        ["lyft"],
        ["stockbased"],
        ["multiadapter"],
        ["tvstick"],
        ["militarygrade"],
        ["kotlin"],
        ["stockindex"],
        ["marketmoving"],
        ["belkins"],
        ["subscriptionbased"],
        ["airpod"],
        ["chiprelated"],
        ["cheapbudget"],
        ["scaledup"],
        ["wirecutter"],
        ["wristworn"],
        ["biggerscreen"],
        ["employeeranking"],
        ["stockportfolio"],
        ["firetv"],
        ["floppydisk"],
        ["zerocommission"],
        ["zenwatch"],
        ["nsagov"],
        ["fbis"],
        ["smartpost"],
        ["conflictfree"],
        ["closedsource"],
        ["communityrun"],
        ["voiceactivated"],
        ["voiceordered"],
        ["safetynet"],
        ["gsync"],
        ["chromecast"],
        ["jpmorgans"],
        ["septupled"],
        ["liquidresistant"],
        ["brexit"],
        ["meltdownspectre"],
        ["multiwaypoint"],
        ["carplay"],
        ["hotword"],
        ["nearstock"],
        ["mindblank"],
        ["thermalpower"],
        ["datascience"],
        ["spotifys"],
        ["bigheavy"],
        ["stockpicks"],
        ["mediastore"],
        ["forceclosed"],
        ["trudeaus"],
        ["upgradekits"],
        ["autoorientation"]
    ]
    
    with db() as (conn, cur):
    
        cur.executemany("INSERT OR IGNORE INTO specialwords VALUES (?)", special_words)
        conn.commit()
    

