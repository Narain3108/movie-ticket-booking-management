import random
import mysql.connector 
conn=mysql.connector.connect(host = 'localhost',user='root',passwd='karthi',database="S2_CINEMAS")
c1=conn.cursor()
if conn.is_connected():
    print("========================================================================================")
    print ("                 ************** WELCOME TO S2 CINEMAS BOOKING (AC) ************")
    print("========================================================================================")
    print("")
    print ("                           S2 CINEMAS TICKET BOOKING PORTAL")
    print("")
    print('''LOGIN TO BOOK YOUR TICKETS
    DON'T HAVE AN ACCOUNT ? SIGN UP''')
    print ("SIGN UP")
    print ("LOG IN")
    opt=input("ENTER 'LOGIN' OR 'SIGNUP' TO PROCEED FURTHER :")
    if opt.upper()=='LOGIN':
        L_id=input("ENTER YOUR EMAIL ID : ")
        L_PWD=input("ENTER YOUR PASSWORD ")
    elif opt.upper()=="SIGNUP":
        s_id=input("ENTER YOUR EMAIL ID : ")
        s_pwd=input("ENTER YOUR PASSWORD : " )
        s_name=input("ENTER YOUR NAME : ")
        s_DOB=input("ENTER YOUR DATE OF BIRTH : ")
        s_age=int(input("ENTER YOUR AGE : " ))
        s_NO=int(input("ENETR YOUR PHONE NO : "))
        sig_ins="insert into Sign_up values( '{}','{}','{}','{}','{}','{}')".format(s_id,s_pwd,s_name,s_DOB,s_age,s_NO)
        c1.execute("CREATE TABLE IF NOT EXISTS Sign_up(s_id VARCHAR(30),s_pwd VARCHAR(30),s_name VARCHAR(40),s_DOB VARCHAR(15),s_age INT,s_NO INT(10)) ;")
        c1.execute(sig_ins)
        conn.commit()
        print("SUCCESSFULLY SIGNRD IN")
        print("")
        print("===================================================================================")
        print("")
        print ("                                   S2 CINEMAS")
        print("")
        print("===================================================================================")
        print
        print ('''SELECT FROM THE FOLLOWING
                          SCREENS      SHOWS
                        1. DIAMOND     4AM      7AM   11AM     3PM  6PM     9.30PM 
                        2. GOLD        4.30AM   8AM   11.30PM  2PM  5.30PM  9PM
                        3. RUBY        9AM                     3PM           
                        4. PEARL       8.30AM   12PM                6.30PM ''')
    ch=int(input("ENTER YOUR CHOICE :"))
    if ch==1:
        print("************ WELCOME TO SCREEN 1 (DIAMOND) ******************")
        v_mname = input("Enter the movie name :")
        v_date = input("Enter date :")
        v_tic = int(input("Enter total tickets :" ))
        v_fname = input ("Enter your first name :")
        v_lname = input ("Enter your last name :")
        v_userID = input ("Enter your EMAIL ID :")
        c1.execute("CREATE TABLE if not exists SCREEN_1(M_NAME VARCHAR(30),DATE VARCHAR(20),NO_OF_TICKETS INT,FIRST_NAME VARCHAR(40),LAST_NAME VARCHAR(40),USER_ID VARCHAR(50))")
        v_ins="insert into SCREEN_1 values( '{}','{}','{}','{}','{}','{}')".format(v_mname,v_date,v_tic,v_fname,v_lname,v_userID)
        c1.execute(v_ins)
        conn.commit()
        print (" SEATS RESERVED SUCCESSFULLY ")
        print ("THANK YOU FOR VISITING S2 CINEMAS")
    elif ch ==2:
        print("************ WELCOME TO SCREEN 2 (GOLD) ******************")
        S_mname = input("Enter the movie name :")
        S_date = input("Enter date :")
        S_tic = int(input("Enter total tickets :" ))
        S_fname = input ("Enter your first name :")
        S_lname = input ("Enter your last name :")
        S_userID = input ("Enter your EMAIL ID :")
        c1.execute("CREATE TABLE if not exists SCREEN_2(M_NAME VARCHAR(30),DATE VARCHAR(20),NO_OF_TICKETS INT,FIRST_NAME VARCHAR(40),LAST_NAME VARCHAR(40),USER_ID VARCHAR(50))")
        S_ins="insert into SCREEN_2 values( '{}','{}','{}','{}','{}','{}')".format(S_mname,S_date,S_tic,S_fname,S_lname,S_userID,)
        c1.execute(S_ins)
        conn.commit()
        print (" SEATS RESERVED SUCCESSFULLY ")
        print ("THANK YOU FOR VISITING S2 CINEMAS")
    elif ch==3:
        print("************ WELCOME TO SCREEN 3 (RUBY) ******************")
        R_mname = input("Enter the movie name :")
        R_date = input("Enter date :")
        R_tic = int(input("Enter total tickets :" ))
        R_fname = input ("Enter your first name :")
        R_lname = input ("Enter your last name :")
        R_userID = input ("Enter your EMAIL ID :")
        c1.execute("CREATE TABLE if not exists  SCREEN_3(M_NAME VARCHAR(30),DATE VARCHAR(20),NO_OF_TICKETS INT,FIRST_NAME VARCHAR(40),LAST_NAME VARCHAR(40),USER_ID VARCHAR(50))")
        R_ins="insert into SCREEN_3 values( '{}','{}','{}','{}','{}','{}')".format(R_mname,R_date,R_tic,R_fname,R_lname,R_userID)

        c1.execute(R_ins)
        conn.commit()
        print (" SEATS RESERVED SUCCESSFULLY ")
        print ("THANK YOU FOR VISITING S2 CINEMAS")
    elif ch==4:
        print("************ WELCOME TO SCREEN 4 (PEARL) ******************")
        c1.execute("CREATE TABLE if not exists SCREEN_4 (M_NAME VARCHAR(30),DATE VARCHAR(20),NO_OF_TICKETS INT,FIRST_NAME VARCHAR(40),LAST_NAME VARCHAR(40),USER_ID VARCHAR(50))")
        p_mname = input("Enter the movie name :")
        p_date = input("Enter date :")
        p_tic = int(input("Enter total tickets :" ))
        p_fname = input ("Enter your first name :")
        p_lname = input ("Enter your last name :")
        p_userID = input ("Enter your EMAIL ID :")
        p_ins="insert into SCREEN_4 values( '{}','{}','{}','{}','{}','{}')".format(p_mname,p_date,p_tic,p_fname,p_lname,p_userID)
        c1.execute(p_ins)
        conn.commit()
        print (" SEATS RESERVED SUCCESSFULLY ")
        print ("THANK YOU FOR VISITING S2 CINEMAS")
    else:
        print("***** YOU ENTERED A WRONG CHOICE ****")
        print("=================================================================================================================================")
    print("===============================================================================================")
    print("                                     S2 CINEMAS PAYMENT PORTAL" )
    print("===============================================================================================")
    print("")
    CF_NAME=input("ENTER YOUR FIRST NAME : ")
    CL_NAME=input("ENETR YOUR LAST NAME : ")
    C_ID=input("ENETR YOUR EMAIL ID : ")
    C_NO=int(input("ENTER YOUR MOBILE NO : " ))
    otp=random.randint(5000,10000)
    print(otp)
    OTP=int(input( "ENTER THE OTP WHICH WAS SENT TO YOUR MOBILE :"))
    if OTP==otp:
        print("VERIFIED SUCCESSFULLY")
    else :
        print("OTP NOT VERIFIED")
    sc=int(input("ENTER THE SCREEN YOU HAVE SELECTED : "))
    print("")
    print("WE HAVE THE FOLLOWING SEATS FOR YOU")
    print('''         SEATS              PRICE
                  1.   NORMAL(A-E)        90RS
                  2.   STANDARD(F-L)      120RS
                  3.   ROYAL(M-S)         200RS 
                  4.   ULTRA ROYAL(T-Z)   300RS
                        ''')
    Ch=input(" ENTER YOUR CHOICE : ")
    N=int(input(" ENTER TOTAL NO OF TICKETS : "))
    if ch==1:
        print("YOU HAVE OPTED NORMAL SEAT " )
        S=90*N
        print("PRICE=",S)
    elif ch==2:
        print("YOU OPTED STANDARD SEAT ")
        S=120*N
        print("PRICE=",S)
    elif ch==3:
        print("YOU OPTED ROYAL SEAT ")
        S=200*N
        print("PRICE=",S)
    elif ch==4:
        print("YOU OPTED ULTRA ROYAL SEAT")
        S=300*N
        print("PRICE=",S)
    else:
        print("ENTER CORRECT CHOICE ")
        print("THE TOTAL AMOUNT IS ",S)
    print('''PAYMENT METHODS
                 1.CASH/CARD
                 2.ONLINE PAYMENT''')
    pay_ins="INSERT INTO C_DETAILS VALUES( '{}','{}','{}','{}','{}')".format(CF_NAME,CL_NAME,C_ID,N,S)
    c1.execute("CREATE TABLE if not exists C_DETAILS(F_NAME VARCHAR(30),L_NAME VARCHAR(20),C_ID VARCHAR(50), NO_OF_TICKETS INT,AMOUNT INT)")
    c1.execute(pay_ins)
    conn.commit()

    PM=input("ENTER YOUR PAYMENT METHOD : ")
    if PM.upper()=="CASH" or "CARD" :
        print("PAY THE AMOUNT DIRECLY TO THE AUTHORITY")
        print("*** TICKET BOOKED ***")


    elif PM.upper()=="ONLINE PAYMENT" :
        print("***************** CASH PAYMENT ******************")
        print("https://www.bhimupi.org.in/")
        print("https://indianbank.in/#!")
        print("ENETR THE ABOVE LINK AND PAY THE FOLLOWING AMOUNT : ",S)
        print("*** TICKET BOOKED ***")
        print("")
        print("================= THANK YOU ==============")
    else :
        print("YOU ENTERED WRONG CHOICE")
    print("")    
    print("PLEASE RATE OUR SERVICE IN 1 TO 5 SCALE :")
    RATING=int(input("RATING : "))
